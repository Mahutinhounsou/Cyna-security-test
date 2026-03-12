import streamlit as st
import pandas as pd

df = pd.read_csv("data/enriched/enriched_logs.csv")

df["is_malicious"] = df["is_malicious"].astype(bool)

st.title("Dashboard de surveillance sécurité")
st.write("Visualisation des logs enrichis avec la threat intelligence feed.")

st.metric("Nombre total de logs", len(df))
st.metric("Logs malveillants détectés", df["is_malicious"].sum())

st.subheader("Répartition malveillant / non malveillant")
st.bar_chart(df["is_malicious"].value_counts())

st.subheader("Top 10 des IP malveillantes détectées")
top_ips = df[df["is_malicious"]]["matched_ip"].value_counts().head(10)
st.bar_chart(top_ips)

st.subheader("Répartition des logs par type")
st.bar_chart(df["log_type"].value_counts())

st.subheader("Exemples de logs malveillants")
st.subheader("Filtrer les logs")

log_type_filter = st.selectbox(
    "Type de log",
    ["Tous", "ids", "access"]
)

if log_type_filter != "Tous":
    df_filtered = df[df["log_type"] == log_type_filter]
else:
    df_filtered = df
malicious_logs = df[df["is_malicious"] == True]
st.dataframe(df_filtered.head(20))