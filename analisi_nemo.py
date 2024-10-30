import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math 
import pandas as pd
#g
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
                    name=f"Star_{int(row['ID_parent'])}",
                    absolute_magnitude=row['m_app'],
                    distance=row['dist']
                )
                stars.append(star)
            except ValueError as e:
                print(f"Errore per la stella con ID {row['ID_parent']}: {e}")
        return stars
    # --- PARTE 2: Caricamento dei Dati ---

# Carica i dati
data = pd.read_csv('Nemo_6670.txt', sep=r'\s+', comment='#', header=None)

# Imposta i nomi delle colonne
data.columns = ['MsuH', 'm_ini', 'logL', 'logTe', 'M_ass', 'b_ass', 'y_ass', 'm_app', 'b_y', 'dist', 'abs_dist', 'ID_parent', 'age_parent']

# Debugging: Stampa la forma e i nomi delle colonne
print("Forma del DataFrame:", data.shape)
print("Nomi delle colonne:", data.columns.tolist())
print("Prime righe del DataFrame:")
print(data.head())

# Controllo dei valori NaN
print("Valori NaN nelle colonne:")
print(data.isna().sum())

# Converti le colonne in tipi numerici
numeric_columns = ['MsuH', 'm_ini', 'logL', 'logTe', 'M_ass', 'b_ass', 'y_ass', 'm_app', 'b_y', 'dist', 'abs_dist', 'ID_parent', 'age_parent']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Rimuovi le righe con NaN in M_ass o age_parent
data = data.dropna(subset=['M_ass', 'age_parent'])

# Rimuovi le righe con valori non validi in 'dist'
data = data[data['dist'] > 0]

# --- PARTE 3: Creazione degli Oggetti Star dal DataFrame ---

stars = Star.from_dataframe(data)

# Debug: Controllo se il numero di stelle corrisponde al numero di dati nel file
print(f"Numero totale di stelle nel file: {len(data)}")
print(f"Numero totale di stelle processate: {len(stars)}")

# Mostra le magnitudini apparenti calcolate per le prime 5 stelle
for star in stars[:5]:  
    try:
        print(f"{star.name} apparent magnitude: {star.apparent_magnitude:.2f}")
    except ValueError as e:
        print(e)

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
