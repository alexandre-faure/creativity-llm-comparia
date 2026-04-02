# Étude de Cas

_Réponses aux questions du sujet_

## Exercice 0: Justification théorique des métriques

### 1. Famille A — Métriques de nouveauté lexicale et sémantique

#### 1.1. Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?

Utilisation d'un vocabulaire varié (équivalent à la notion de nouveauté).

#### 1.2. Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.

On peut envisager produire des exemples de différentes natures:

- **Exemples de haute diversité lexicale**: Générer des réponses avec un vocabulaire riche et varié.
- **Exemples de faible diversité lexicale**: Générer des réponses avec un vocabulaire limité et répétitif.

Vérifier empiriquement que les métriques de nouveauté lexicale et sémantique attribuent des scores plus élevés aux exemples de haute diversité lexicale par rapport à ceux de faible diversité.

#### 1.3. Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).

- **Faux positifs**: Un modèle pourrait générer des réponses avec un vocabulaire varié en enchaînant des mots qui n'ont aucun sens ensemble, donnant ainsi une impression de créativité sans réelle cohérence.
- **Faux négatifs**: Cas de citations inventées avec des mots simples (e.g. "Je pense donc je suis")

### 2. Famille B — Métriques de cohérence et valeur

#### 2.1. Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?

Elle quanitifie la cohérence de la formulation et la valeur perçue de la réponse, ce qui correspond à la dimension de pertinence et d'utilité.

#### 2.2. Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.

Grâce aux données de Compar:IA-vote, on peut vérifier que les scores pour les métriques sont corrélés aux votes des utilisateurs (conv_useful_a / b).

#### 2.3. Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).

- **Faux positifs**: Un modèle pourrait générer une réponse très cohérente et bien formulée, mais qui ne serait pas du tout créative (e.g. "La Terre est ronde"). Tout ce qui relève des faits établis et connus pourrait être perçu comme cohérent et utile, mais pas créatif.
- **Faux négatifs**: Par exemple des textes de poésie dont la cohérence n'est pas toujours linéaire, mais qui sont perçus comme très créatifs par les utilisateurs.

### 3. Famille C — Métriques de surprise et d’originalité

#### 3.1. Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?

Les métriques représentent la capacité d'un modèle à générer des réponses inattendues notamment par l'enchaînement surprenant des mots.

#### 3.2. Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.

On peut constituer quelques exemples de réponses:

- **Exemples de haute surprise**: Rédiger des débunks de faits méconnus ou avec des twists inattendus, ou encore des associations de mots surprenantes (e.g. "Le chat a décidé de devenir astronaute").
- **Exemples de faible surprise**: Rédiger des réponses avec des associations de mots très prévisibles et courantes, notamment des faits ou des proverbes.

On peut aussi regarder si l'augmentation de la température d'un modèle génère des réponses plus surprenantes et si les métriques de surprise et d'originalité attribuent des scores plus élevés à ces réponses.

#### 3.3. Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).

- **Faux positifs**: des phrases peuvent être fausses malgré leur caractère surprenant (e.g. "Le soleil est une étoile froide").
- **Faux négatifs**: un raisonnement mathématique ne va pas être très surprenant en tant que succession de propositions logiques, mais peut être très créatif dans sa capacité à résoudre un problème complexe.

### 4. Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative\_\*).

Partant de la forme suivante pour le Creativity Index (CI):
$$CI = \alpha \cdot \text{Nouveauté} + \beta \cdot \text{Valeur} + \gamma \cdot \text{Surprise}$$
avec $\alpha + \beta + \gamma = 1$.

Il nous semble que la valeur est certe importante, mais pas autant que la nouveauté et la surprise, qui sont des dimensions plus fondamentales de la créativité. Nous proposons donc la pondération suivante:

- $\alpha = 0.4$ (Nouveauté)
- $\beta = 0.2$ (Valeur)
- $\gamma = 0.4$ (Surprise)
