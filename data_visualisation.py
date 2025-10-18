from scipy.io import loadmat
import matplotlib.pyplot as plt

# Charger le fichier
data = loadmat('ecg_dataset.mat')

# Explorer les clés contenues dans le fichier
print(data.keys())

# Recuperer X (les signaux ECG) et y (les classes : 0, 1 ou 2)
signaux = data['X']
classes = data['y']

# Afficher un échantillon des données (1er sigal ECG)
plt.plot(signaux[0])
plt.title(f"Classe : {classes[0]}")
plt.show()

# Afficher les classes disponibles
print("Classes disponibles 'y' :", set(classes.flatten()))