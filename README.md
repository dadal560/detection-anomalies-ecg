# Détection d'Anomalies ECG par Auto-encodeur Convolutionnel (AE-CNN)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org)
[![Licence](https://img.shields.io/badge/Licence-La_Rochelle_Université-green.svg)](https://www.univ-larochelle.fr/)

Ce projet implémente un algorithme de Deep Learning semi-supervisé pour la détection d'anomalies cardiaques à partir de signaux ECG, conçu pour être déployé sur des systèmes embarqués type Raspberry Pi.

---

## Présentation du Projet
L'objectif est de détecter des pathologies (Classes R et V) au sein d'un jeu de données massivement déséquilibré (97.8% de signaux normaux). 

### Stratégie Semi-Supervisée
Plutôt qu'une classification classique, nous utilisons un **Auto-encodeur (AE)** entraîné exclusivement sur les signaux normaux (Classe N). L'hypothèse est simple : le modèle apprend à reconstruire parfaitement la "normalité", mais échouera face à une anomalie, générant ainsi une erreur de reconstruction (MSE) élevée.

## Architecture du Modèle (AE-CNN)
Pour respecter une contrainte d'inférence stricte de **500ms**, nous avons conçu une architecture légère :
* **Type :** Auto-encodeur Convolutionnel 1D.
* **Conv1D :** Idéal pour identifier les motifs locaux invariants (complexes P-QRS-T).
* **Bottleneck :** Un goulot d'étranglement de seulement **8 filtres** pour forcer la compression.
* **Légèreté :** Seulement **34 641 paramètres**.

## Prétraitement des Données
Pour garantir l'intégrité de l'approche et éviter toute fuite de données (*data leakage*) :
1.  Utilisation d'un **StandardScaler** (Z-score).
2.  Calibration (*fit*) uniquement sur les 5288 signaux de Classe N.
3.  Transformation de l'ensemble du dataset via ce scaler calibré sur la "normalité".

## Performances et Résultats
Le modèle a été entraîné jusqu'à l'époque 34 (EarlyStopping). Deux stratégies de seuillage ont été évaluées :

| Stratégie | Seuil (MSE) | Détection Classe V | Détection Classe R | Faux Positifs (N) |
| :--- | :--- | :--- | :--- | :--- |
| **F1-Optimal** | 0.1385 | 100% | 91.9% | 1.9% |
| **Sécurité Médicale** | 0.0987 | 100% | 100% | 3.2% |

### Points Clés :
* **Vitesse d'inférence :** 97.33 ms (très en dessous de la limite des 500ms).
* **Robustesse :** L'erreur moyenne des anomalies reste 8.5 fois supérieure à celle des normaux même en présence de bruit.

## Installation et Utilisation
1.  **Installation des dépendances :**
    ```bash
    pip install tensorflow pandas numpy scikit-learn matplotlib
    ```
2.  **Lancement de l'analyse :**
    Exécutez le script principal pour charger le modèle et calculer les erreurs de reconstruction sur les classes de test.

## Auteurs
* **Gwendal Henry**
* **Charles Gery**
* *La Rochelle Université* (Novembre 2025)

---
*Ce projet s'inspire de la recherche sur les Adversarial Autoencoders (AAE) pour la validation des stratégies de reconstruction sur signaux physiologiques.*
