import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



temps=[20, 25, 30, 35, 40]
poids=[60, 65, 70, 75, 80]
fig, ax = plt.subplots()
ax.plot(temps, poids, marker='o', color="yellow")
ax.set_xlabel('Temp (h)')
ax.set_ylabel('Poids (kg)')
ax.set_title('Temp en fonction du Poids')
x = np.linspace(20, 40, 100)
y = 2 + 9.5 * x
ax.plot(x, y, color='red',ls='--', label='y = 2 + 9.5 * x')
ax.grid()
st.pyplot(fig) 

a = [1,2,3,4,5]
np.random.seed(0)
b = np.random.rand(5)   
st.write("a:", a)
st.write("b:", b)   

w = np.array([[0.2, 0.5, 0.3], [0.1, 0.4, 0.6]])
w
w.shape
print(w.shape)
print(w[0, 1])  # Accéder à l'élément de la première ligne et de la deuxième colonne
print(w[1, :])  # Accéder à tous les éléments de la deuxième ligne
print(w[:, 2])  # Accéder à tous les éléments de la troisième colonne
print(w[0])     # Accéder à tous les éléments de la première ligne
print(w[1])     # Accéder à tous les éléments de la deuxième ligne
z = print(w)

st.write("w:", w)
st.write("w shape:", w.shape)
st.write("w[0, 1]:", w[0, 1])
st.write("w[1, :]:", w[1, :])
st.write("w[:, 2]:", w[:, 2])
st.write("w[0]:", w[0])
st.write("w:" , w)


temps=[20, 25, 30, 35, 40]
poids=[60, 65, 70, 75, 80]
fig, ax = plt.subplots()
ax.bar(temps, poids, color="blue")
ax.set_xlabel('Temp (h)')
ax.set_ylabel('Poids (kg)')
ax.set_title('Temp en fonction du Poids')


ax.bar(x, y, color='red')
ax.grid()
st.pyplot(fig) 