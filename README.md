# detection-anomalies-ecg

Projet de détection semi-supervisée d'anomalies cardiaques.

## Installation

Création d'un environnement virtuel pour isoler les dépendances de chaque projet et éviter les conflits de versions entre différents projets Python.

### 1. Créer l'environnement virtuel

```bash
python -m venv venv_ecg
```

### 2. Activer l'environnement virtuel

**Sur Windows :**
```bash
.\venv_ecg\Scripts\activate
```

**Sur Linux/macOS :**
```bash
source venv_ecg/bin/activate
```

### 3. Installer les paquets requis

```bash
pip install numpy scipy scikit-learn tensorflow matplotlib
```

## Dépendances

- `numpy` - Calculs numériques
- `scipy` - Traitement du signal
- `scikit-learn` - Prétraitement et métriques
- `tensorflow` - Deep learning
- `matplotlib` - Visualisation

