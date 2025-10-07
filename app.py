import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Nome do ficheiro CSV onde os dados serão guardados
FICHEIRO_DADOS = "ocorrencias.csv"

st.set_page_config(page_title="Registo de Ocorrências", layout="centered")
st.title("📋 Registo de Ocorrências - Turno da Noite")

# Formulário de registo
with st.form("form_ocorrencia"):
    data = st.date_input("Data", value=datetime.today())
    tecnico = st.selectbox("Técnico", ["Bruno Guerreiro", "Ronaldo Tavares", "Pedro Puga", "José Reis"])
    localizacao = st.text_input("Localização")
    ocorrencia = st.text_area("Descrição da Ocorrência")
    acao = st.text_area("Ação Tomada")
    turno = st.selectbox("Turno", ["Noite", "Manhã", "Tarde"])
    submeter = st.form_submit_button("Submeter")

    if submeter:
        nova_ocorrencia = {
            "Data": data.strftime("%Y-%m-%d"),
            "Técnico": tecnico,
            "Localização": localizacao,
            "Ocorrência": ocorrencia,
            "Ação Tomada": acao,
            "Turno": turno
        }

        # Guardar no CSV
        if os.path.exists(FICHEIRO_DADOS):
            df = pd.read_csv(FICHEIRO_DADOS)
            df = pd.concat([df, pd.DataFrame([nova_ocorrencia])], ignore_index=True)
        else:
            df = pd.DataFrame([nova_ocorrencia])

        df.to_csv(FICHEIRO_DADOS, index=False)
        st.success("✅ Ocorrência registada com sucesso!")

# Mostrar relatório
st.subheader("📊 Relatório de Ocorrências")
if os.path.exists(FICHEIRO_DADOS):
    df = pd.read_csv(FICHEIRO_DADOS)
    st.dataframe(df)
else:
    st.info("Ainda não existem ocorrências registadas.")
