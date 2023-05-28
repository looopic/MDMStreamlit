import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
@st.cache_data
def dataimport():
    data = pd.read_csv("bulidata.csv")
    data["GOALS_TOTAL"] = data["GOALS_HOME"] + data["GOALS_AWAY"]
    return data

# Streamlit-Anwendung
st.set_page_config(page_title="Fussball Daten")
st.title("Datenset-Visualisierung")
st.write("Das ist eine Visualisierung des \"Football | Bundesliga Seasons 2005/06 - 2022/23\" Datensets von Kaggle (https://www.kaggle.com/datasets/oles04/bundesliga-seasons)")

data = dataimport()

# Filtern der Daten basierend auf den Eingabefeldern
min_value = st.slider("Min. Goals", float(data["GOALS_TOTAL"].min()), float(data["GOALS_TOTAL"].max()), 0.0)
max_value = st.slider("Max. Goals", float(data["GOALS_TOTAL"].min()), float(data["GOALS_TOTAL"].max()), 20.0)
filtered_data = data[(data["GOALS_TOTAL"] >= min_value) & (data["GOALS_TOTAL"] <= max_value)]

# Grafik erstellen
plt.figure(figsize=(10, 6))
plt.hist(filtered_data["GOALS_TOTAL"], bins=20)
plt.xlabel("Totale Anzahl Tore")
plt.ylabel("Anzahl")
plt.title("Histogramm der Tore")
st.pyplot(plt)

# Tabelle mit den gefilterten Daten anzeigen
st.subheader("Gefilterte Daten")
st.write(filtered_data)
