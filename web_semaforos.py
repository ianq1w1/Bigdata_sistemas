import pandas as pd
import streamlit as st

df = pd.read_csv('semaforos.csv')

#df['status'] = "funcionando"
#df.to_csv('semaforos.csv', index=False)

bairros = list(df['bairro'].unique())
bairro = st.sidebar.selectbox("Escolha o bairro", ["Bairro"] + bairros)

filtered_df = df[df['bairro'] == bairro]
localizacoes1 = list(filtered_df['localizacao1'].unique())
localizacao1 = st.sidebar.selectbox("Escolha a localização 1", ["Localização 1"] + localizacoes1)

filtered_df = df[df['localizacao1'] == localizacao1]
localizacoes2 = list(filtered_df['localizacao2'].unique())
localizacao2 = st.sidebar.selectbox("Escolha a localização 2", ["Localização 2"] + localizacoes2)

if(localizacao1 != 'Localização 1'):
    #df = df[df['localizacao1'] == localizacao1]
    df_filtered = df[df['localizacao1'] == localizacao1].copy()
else:
    df_filtered = df.copy()

if(localizacao2 != 'Localização 2'):
    #df = df[df['localizacao2'] == localizacao2]
    df_filtered = df_filtered[df_filtered['localizacao2'] == localizacao2]

if(localizacao1 != 'Localização 1' and localizacao2 != 'Localização 2'):
    places = pd.DataFrame({
        "lat": df_filtered["latitude"].astype(float),
        "lon": df_filtered["longitude"].astype(float),
    })

    st.title("Semáforo entre " + localizacao1 + " e " + localizacao2)

    if (df_filtered["status"] == "funcionando").any():
        st.success("Nenhum problema reportado para este semáforo.")
        if st.button("Reportar problema", type="primary"):
            # Identificar o semáforo específico
            semaforo_index = df_filtered.index[(df_filtered['bairro'] == bairro) & (df_filtered['localizacao1'] == localizacao1) & (df_filtered['localizacao2'] == localizacao2)].tolist()

            if semaforo_index:
                # Atualizar o status do semáforo para "defeituoso" na cópia
                df_filtered.at[semaforo_index[0], 'status'] = "defeituoso"
                
                # Salvar a cópia do DataFrame de volta no arquivo CSV
                df.update(df_filtered)
                df.to_csv('semaforos.csv', index=False)
                st.rerun()
            
    elif(df_filtered["status"] == "defeituoso").any():
        st.error("Um problema foi reportado para este semáforo.")
    st.map(places)
else:
    st.warning("Selecione as localizações")