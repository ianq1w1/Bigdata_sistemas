import pandas as pd
import streamlit as st

df = pd.read_csv('semaforos.csv')

localizacoes1 = list(df['localizacao1'].unique())
localizacoes2 = list(df['localizacao2'].unique())

localizacao1 = st.sidebar.selectbox("Escolha a localização 1", localizacoes1)
localizacao2 = st.sidebar.selectbox("Escolha a localização 2", localizacoes2)

if(localizacao1 != 'Localização 1'):
    df = df[df['localizacao1'] == localizacao1]

if(localizacao2 != 'Localização 2'):
    df = df[df['localizacao2'] == localizacao2]

places = pd.DataFrame({
    "lat": df["latitude"].astype(float),
    "lon": df["longitude"].astype(float),
})

if(st.sidebar.checkbox("Mostrar tabela de dados")):
    st.write(df)

st.map(places)