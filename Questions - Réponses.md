# Remarques et pistes d'amélioration pour la plateforme `compar:ia`

## Améliorer l'expressivité du vote sur la créativité

- **Oui / Non trop restrictif** : le remplacer par une échelle de likert par exemple
- **Aucun moyen d'indiquer que l'utilisateur a bien voté pour la créativité** : laisser `NaN` par défaut et donner la possibilité d'exprimer qu'une réponse n'est pas créative.

## Améliorer la comparabilité des données

- **Foule annotant les conversations sans référence commune a priori** : ajouter une base de référence annotée par des "experts" sur plusieurs domaines
- **Foule n'annotant pas les mêmes conversations** : faire annoter des conversations "standards", annotées par les experts, par chaque utilisateur avant de le laisser générer sa propre conversation

Pour plus de détails, se référer à la proposition de protocole hybride experts/crowd esquissé dans le document sur le [paradoxe du juge](scripts/4_3_judge_paradox.ipynb), ou directement dans la présentation finale du projet (slides 31-32) : [compar:ia - présentation finale](Soutenance%20Étude%20de%20Cas%20-%20Groupe%205%20-%20Créativité%20des%20LLMs.pdf)
