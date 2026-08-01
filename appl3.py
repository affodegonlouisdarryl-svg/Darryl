import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("les diagrammes de dispersion")
st.subheader("Auteur: M. AFFODEGON")
st.write("c'est un Diagramme de dispersion du poids en fonction du temps")
temps=[20, 25, 30, 35, 40]
poids=[60, 65, 70, 75, 80]

fig, ax = plt.subplots()
temps = st.write_input(label="Entrez une valeur pour le temps:", min_value=0, max_value=24, value=12) 
poids = st.write_input(label="Entrez une valeur pour le poids:", min_value=0, max_value=100, value=70)
ax.plot(temps, poids, marker='o', color="yellow", label=f'Temp: {temps}, Poids: {poids}')   
ax.set_xlabel('Temp (h)')
ax.set_ylabel('Poids (kg)')
ax.set_title('Temp en fonction du Poids')


st.pyplot(fig) 