import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- PARTE 4: Creazione degli Intervalli di Età ---

# Definisci il numero di bins
Nbins = 30

# Crea i bins in base all'età
data['age_bin'] = pd.cut(data['age_parent'], bins=Nbins)
bins = pd.cut(data['age_parent'], bins=Nbins)

# Crea una colormap
cmap = plt.colormaps['viridis']
marker_size = 10

# Crea un color_map che usa l'indice del bin come chiave
color_map = {i: cmap(i / (Nbins - 1)) for i in range(Nbins)}

# --- PARTE 5: Diagramma di Dispersione ---

plt.figure(figsize=(10, 6))
for i, (bins_value, group) in enumerate(data.groupby(bins, observed=False)):
    color = color_map[i]
    plt.scatter(group['b_y'], group['M_ass'], 
                label=f'Bins: {bins_value.left:.2f} to {bins_value.right:.2f}', 
                color=color, alpha=0.8, s=marker_size)

plt.legend()
plt.title('Diagramma di Magnitudine Assoluta vs Età')
plt.xlabel('b_y')
plt.ylabel('Magnitudine Assoluta (M_sun)')
plt.gca().invert_yaxis()
plt.grid()
plt.show()

