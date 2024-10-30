import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math 
import pandas as pd

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
    
    def show_head(self, n=5):
        """Mostra le prime n righe del file."""
        print(self.data.head(n))

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

