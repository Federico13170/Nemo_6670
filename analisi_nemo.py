import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math 
import pandas as pd
gu
# --- Parte 1: Derfinizione della classe 

class Star:
    def __init__(self, name, absolute_magnitude, distance):
        #"""Costruttore che carica i dati dal file specificato."""
        self.name = name
        self.absolute_magnitude = absolute_magnitude
        self.distance = distance

    @property
    def apparent_magnitude(self):
        """ Calcolo la magnitudine apparente"""
        if self.distance > 0:
            return self.absolute_magnitude + 5 * math.log10(self.distance / 10)
        else:
            raise ValueError(f"Errore: La distanza della stella '{self.name}' deve essere maggiore di zero.")
    @classmethod
    def from_dataframe(cls, df):
        """Crea istanze di star da un DataFrame"""
        stars = []
        for _, row in df.iterrows():
            try:
                star = cls(
                    name=f"Star_{int()}
    def show_info(self):
        """Mostra informazioni sul DataFrame."""
        print(self.data.info())

    def get_column(self, column_name):
        """Ritorna i dati di una colonna specifica."""
        if column_name in self.data.columns:
            return self.data[column_name]
        else:
            raise ValueError(f"Colonna '{column_name}' non trovata nel file.")

    def save_to_csv(self, output_path):
        """Salva il DataFrame in un file CSV."""
        self.data.to_csv(output_path, index=False)
        print(f"Dati salvati in {output_path}")
import pandas as pd

# --- PARTE 4: Creazione degli Intervalli di Età ---

# Definisci il numero di bins
Nbins = 30
cacca
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
