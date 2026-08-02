import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Guide d'orientation au soutien des bacheliers")
st.subheader("Auteur: M. AFFODEGON Louis-Darryl")
st.write("Pour aider les bacheliers à bien s'orienter dans leur choix de  filière, ce guide d'orientation a été mis en place.De ce fait  elle  permettra de calculer la moyenne et de savoir si le bachelier cible est admis.Suite à une admission, Il vous donnera également des conseils sur les filières qui s'offrent à vous en fonction de votre série .")
Nom = st.text_input(label="Nom:")
plt.text(0.05, 0.95, f'Nom & Prénom: {Nom}', transform=plt.gca().transAxes, verticalalignment='top'  )
Prenoms = st.text_input(label=" Prénom:")
plt.text(0.05, 0.95, f'Nom & Prénom: {Prenoms}', transform=plt.gca().transAxes, verticalalignment='top'  )

z = st.pills("Sélectionnez votre série:",["D","C","B","A"], selection_mode="single")
plt.text(0.05, 0.85, f"Vous avez sélectionné la série: {z}", transform=plt.gca().transAxes, verticalalignment='top'     )

if z == "D":
    p = st.container(border=True)
    p.write("Mathématiques coeff (4)")
    p.write("PCT coeff (4)")
    p.write("Anglais coeff (2)")
    p.write("Français coeff (2)")
    p.write("Philosophie coeff (2)")
elif z == "C":
    p = st.container(border=True)
    p.write("Mathématiques coeff (6)")
    p.write("PCT coeff (5)")
    p.write("Anglais coeff (2)")
    p.write("Français coeff (2)")
    p.write("Philosophie coeff (2)")
elif z  == "B":
    p = st.container(border=True)
    p.write("Mathématiques coeff (2)")
    p.write("PCT coeff (1)")
    p.write("Anglais coeff (3)")
    p.write("Français coeff (4)")
    p.write("Philosophie coeff (4)")
elif z  == "A":
    p = st.container(border=True)
    p.write("Mathématiques coeff (2)")
    p.write("PCT coeff (1)")
    p.write("Anglais coeff (3)")
    p.write("Français coeff (4)")
    p.write("Philosophie coeff (3)") 
    
k = st.number_input(label="Votre note de PCT:", min_value=0.0, max_value=20.0, value=17.0, step=0.25)
s = st.number_input(label="Votre note d'Anglais:", min_value=0.0, max_value=20.0, value=12.0, step=0.25) 
o = st.number_input(label="Votre note de Français:", min_value=0.0, max_value=20.0, value=17.0, step=0.25)
i = st.number_input(label="Votre note de Maths:", min_value=0.0, max_value=20.0, value=12.0, step=0.25   ) 

if z == "D":
    moyenne = (k*4 + s*2 + o*2 + i*4) / (4+2+2+4) 

elif z == "C":
    moyenne = (k*5 + s*2 + o*2 + i*6) / (5+2+2+6)
    
elif z  == "B":  
    moyenne = (k*1 + s*3 + o*3 + i*2) / (1+3+3+2)
    
elif z  == "A":
    moyenne = (k*1 + s*3 + o*2 + i*2) / (1+3+2+2)
 
if st.button("Calculer la moyenne"):
 st.write(f"Votre moyenne est: {moyenne}")
 if moyenne >= 10:
     st.write("Félicitations! Vous etes admis.")
     st.write("Vous pouvez passer en classe supérieure.")
     st.write("Voici les choix de filières qui s'offrent à vous.")
     

 else:
     st.write("Désolé! Vous n'est pas admis.")
     st.write(" Du courage! Vous pouvez toujours vous améliorez.")
if moyenne >= 10:       
 if st.button("Voir les choix de filière"):
      
         st.write("Voici les choix de filière qui s'offrent à vous.")
 if z == "A":
             st.write("Droit")
             st.write("Lettres")
             st.write("Philosophies")
             st.write(" Economique et sociale")
             st.write(" Langes et histoire ")
 elif z == "D":
             st.write("Sciences de la vie et de la terre")
             st.write("Pharmacie")
             st.write("Sciences de l'environnement")
             st.write("Sciences de la santé")
             st.write("Agronomie")
             st.write("Biologie")
 elif z == "C":
             st.write("Sciences de l'ingénieur")
             st.write("Informatique")
             st.write("Mathématiques")
             st.write("Physique")
             st.write("Chimie")
 elif z == "B":
                    st.write("Commerce")
                    st.write("Droit")
                    st.write("Gestion")
                    st.write("Economie")
                    st.write("Comptabilité")
     
     