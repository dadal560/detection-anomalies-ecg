# Détection d'Anomalies ECG (Auto-encodeur)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet utilise le Deep Learning pour identifier automatiquement les battements cardiaques anormaux à partir de signaux ECG. L'approche repose sur un **auto-encodeur** entraîné exclusivement sur des données normales.

---

## Présentation du Projet

L'objectif est de détecter des pathologies cardiaques en analysant la capacité d'un modèle à reconstruire un signal. 
- Si le modèle reconstruit bien le signal : le battement est considéré comme **Normal**.
- Si l'erreur de reconstruction est élevée : le battement est classé comme **Anomalie**.

### Dataset
Le projet utilise le dataset **ECG5000**, contenant 5 000 extraits d'électrocardiogrammes.
* **Classe 0 :** Battements normaux.
* **Classe 1 à 4 :** Différentes classes d'anomalies (Arythmies, etc.).

---

## Architecture du Modèle

Le modèle est un réseau de neurones de type **Auto-encodeur** composé de :
1.  **Encodeur :** Compresse le signal d'entrée (140 points) vers un espace latent réduit.
2.  **Décodeur :** Reconstruit le signal original à partir de cette représentation compressée.

---

## Installation et Utilisation

### Prérequis
Assurez-vous d'avoir Python installé ainsi que les bibliothèques suivantes :
```bash
pip install pandas numpy matplotlib tensorflow scikit-learn
