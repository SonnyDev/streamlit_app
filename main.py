import pandas
import streamlit as st
import pandas as pd
import numpy as np

st.write("Formation LangChain")

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Salut")

df = pandas.read_csv("titanic.csv")

st.write(df)

age = st.slider("Sélectionner votre age", 0, 100, 25)
st.write("Vous avez", age, " ans")

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

couleur = st.selectbox('Quelle est ta couleur préferée ?', ['Bleu', 'Rouge', 'Vert'])

st.write("Ta couleur preferée est", couleur)


options = st.multiselect("Quelles sont tes coleurs préférées ?",
               ["Blue", "Jaune", "Rouge", "Vert"],
               ["Jaune", "Rouge"])


st.write("Vos couleurs sont", options)

st.write("Qu'aimeriez-vous commander ?")

banane = st.checkbox("Banane")
pomme = st.checkbox("Pomme")
poire = st.checkbox("Poire")

if banane:
    st.write("Voici vos bananes :banana")

if pomme:
    st.write("Voici vos pommes :apple")

if poire:
    st.write("Voici vos poires :smile")


