# dl03 / ex00 — Convolution simple

| Champ | Valeur |
| --- | --- |
| Livrable | `solution.py` ou fichiers explicitement indiqués |
| Tests | `test_solution.py` |
| Python | 3.11+ |
| Outils | NumPy ; PyTorch à partir de dl02 |

## Objectif
`conv2d_valid(image: np.ndarray, kernel: np.ndarray) -> np.ndarray`

Convolution 2D sans padding, stride 1; préciser convention corrélation.

## Exemple
Image 3×3, noyau 2×2 → sortie 2×2.

## Contraintes
- Respecter le contrat et documenter les formes des tenseurs.
- Vérifier dimensions et valeurs invalides ; lever `ValueError` quand applicable.
- Pas de mutation silencieuse des arguments.
- Fixer les seeds NumPy/PyTorch pour les expériences et documenter les écarts possibles selon plateforme.
- Éviter les appels de bibliothèque réalisant directement le mécanisme à implémenter, sauf demande explicite.
- Séparer train et validation et ne pas sélectionner un modèle sur le jeu de test.
- Préférer des expériences exécutables sur CPU, petits batchs et données réduites.

## À rendre
1. Code fonctionnel et lisible, sans solution préremplie.
2. Trois tests minimum : nominal, cas limite, erreur ou dimension invalide.
3. `NOTES.md` expliquant l'intuition mathématique, les formes et une observation mesurée.

## Bonus
Étudier l'effet d'un hyperparamètre, comparer une implémentation de référence, ou profiler la mémoire.

## Autoévaluation
- [ ] Je peux expliquer les étapes du calcul.
- [ ] Tests et résultats reproductibles.
- [ ] Je sais interpréter une limite du modèle.
