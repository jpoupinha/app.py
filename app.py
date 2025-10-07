import streamlit as st
import pandas as pd
from datetime import datetime
import os

FICHEIRO_DADOS = "ocorrencias.csv"

st.title("📋 Registo de Ocorrências - Turno da Noite")

with st.form("form_ocorrencia"):
    data = st.date_input("Data", value=datetime.today())
    tecnico = st.text_input("Técnico")
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

        if os.path.exists(FICHEIRO_DADOS):
            df = pd.read_csv(FICHEIRO_DADOS)
            df = pd.concat([df, pd.DataFrame([nova_ocorrencia])], ignore_index=True)
        else:
            df = pd.DataFrame([nova_ocorrencia])

        df.to_csv(FICHEIRO_DADOS, index=False)
        st.success("✅ Ocorrência registada com sucesso!")

st.subheader("📊 Relatório de Ocorrências")
if os.path.exists(FICHEIRO_DADOS):
    df = pd.read_csv(FICHEIRO_DADOS)
    st.dataframe(df)
else:
    st.info("Ainda não existem ocorrências registadas.")
