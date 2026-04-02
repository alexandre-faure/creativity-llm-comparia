"""
Estimation Bradley-Terry avec intervalles de confiance bootstrap
et diagnostic du nombre de répliques B optimal.
"""

from typing import NamedTuple

import numpy as np
from tqdm import tqdm


def estimate_bradley_terry(W: np.ndarray, tol: float = 1e-8, max_iter: int = 10000):
    """
    Estime les paramètres β du modèle de Bradley-Terry via l'algorithme
    itératif original (Bradley & Terry 1952 / Hunter 2004 MM).

    Args:
        W        : matrice (k, k), W[i,j] = nb de victoires de i sur j
        tol      : critère d'arrêt sur la variation max de β
        max_iter : garde-fou

    Returns:
        beta     : paramètres estimés (non normalisés)
        ranking  : indices triés par β décroissant
    """
    k = W.shape[0]
    beta = np.ones(k)

    # Wins totaux de chaque modèle
    W_wins = W.sum(axis=1)
    W_total = W + W.T

    for i in range(max_iter):
        beta_old = beta.copy()

        # Mise à jour simultanée de tous les β (forme vectorisée)
        # denom[i] = Σⱼ≠ᵢ  (Wᵢⱼ + Wⱼᵢ) / (βᵢ + βⱼ)
        denom = (W_total / (beta[:, None] + beta[None, :])).sum(axis=1)

        # Éviter division par zéro pour les modèles sans aucune victoire
        beta = np.where(W_wins > 0, W_wins / denom, 1e-10)

        # Normalisation pour fixer l'identifiabilité (sum = k)
        beta /= beta.mean()

        if np.max(np.abs(beta - beta_old)) < tol:
            break

    ranking = np.argsort(beta)[::-1]
    return beta, ranking


def _one_bootstrap(duels: np.ndarray, k: int, rng: np.random.Generator) -> np.ndarray:
    """
    duels : tableau (N, 3) — colonnes [winner_id, loser_id, weight]
    Retourne log(beta) estimé sur un rééchantillon.
    """
    idx = rng.integers(0, len(duels), size=len(duels))
    sample = duels[idx]

    wins = np.zeros((k, k))
    for winner, loser, w in sample:
        wins[int(winner), int(loser)] += w

    beta, _ = estimate_bradley_terry(wins)
    return np.log(beta)


class BTResult(NamedTuple):
    beta_hat: np.ndarray  # paramètres MLE sur données complètes
    log_beta: np.ndarray  # log(beta), échelle Elo-like
    ci_low: np.ndarray  # borne inférieure IC 95 % (sur log beta)
    ci_high: np.ndarray  # borne supérieure IC 95 % (sur log beta)
    se: np.ndarray  # erreur-type bootstrap de log beta
    B_used: int  # nombre de répliques effectivement utilisées
    B_trace: dict  # diagnostic de convergence (pour plot)


def bootstrap_bradley_terry(
    duels: np.ndarray,
    k: int,
    B: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
    convergence_check: bool = True,
    conv_window: int = 100,
    conv_tol: float = 0.005,
    kept_models_idx: list[int] = None,
) -> BTResult:
    """
    Paramètres
    ----------
    duels            : (N, 3) — [winner_id, loser_id, weight=1]
    k                : nombre de modèles
    B                : nombre max de répliques bootstrap
    alpha            : niveau de risque (0.05 → IC 95 %)
    convergence_check: stopper tôt si les SE stabilisent
    conv_window      : nb de répliques entre deux checks
    conv_tol         : variation relative max des SE pour déclarer convergence
    kept_models_idx  : indices des modèles à garder

    Retourne
    --------
    BTResult avec IC, SE et trace de convergence
    """
    rng = np.random.default_rng(seed)

    # Fit sur données complètes
    wins_full = np.zeros((k, k))
    for winner, loser, w in duels:
        wins_full[int(winner), int(loser)] += w
    beta_hat, _ = estimate_bradley_terry(wins_full)

    # Stockage des répliques
    boot_samples = np.empty((B, k))
    se_trace = {}  # {b: SE moyenne} pour diagnostic
    B_used = B

    se_prev = None
    for b in tqdm(range(B), desc="Bootstrap Bradley-Terry", unit="réplique"):
        boot_samples[b] = _one_bootstrap(duels, k, rng)

        # ── Diagnostic convergence tous les conv_window tirages ──
        if convergence_check and (b + 1) % conv_window == 0 and b > conv_window:
            se_now = boot_samples[: b + 1].std(axis=0)
            se_trace[b + 1] = se_now.mean()

            if se_prev is not None:
                rel_change = np.abs(se_now - se_prev).max() / (se_prev.max() + 1e-12)
                if rel_change < conv_tol:
                    B_used = b + 1
                    boot_samples = boot_samples[:B_used]
                    break

            se_prev = se_now

    # IC par quantiles (méthode percentile)
    q_low = (alpha / 2) * 100
    q_high = (1 - alpha / 2) * 100
    ci_low = np.percentile(boot_samples, q_low, axis=0)
    ci_high = np.percentile(boot_samples, q_high, axis=0)
    se = boot_samples.std(axis=0)

    if kept_models_idx is not None:
        ci_low = ci_low[kept_models_idx]
        ci_high = ci_high[kept_models_idx]
        se = se[kept_models_idx]
        beta_hat = beta_hat[kept_models_idx]
    return BTResult(
        beta_hat=beta_hat,
        log_beta=np.log(beta_hat),
        ci_low=ci_low,
        ci_high=ci_high,
        se=se,
        B_used=B_used,
        B_trace=se_trace,
    )


def print_ranking(result: BTResult, model_names: list[str]):
    order = np.argsort(-result.log_beta)
    print(f"\n{'Rang':<5} {'Modèle':<20} {'log beta':<8} {'IC 95 %':>20}  {'SE':<6}")
    print("─" * 65)
    rank = 1
    for idx in order:
        name = model_names[idx]
        score = result.log_beta[idx]
        lo = result.ci_low[idx]
        hi = result.ci_high[idx]
        se = result.se[idx]
        print(f"{rank:<5} {name:<20} {score:+.3f}   [{lo:+.3f}, {hi:+.3f}]  {se:.4f}")
        rank += 1
