import streamlit as st
import pandas as pd
import sys
import os

# Suchpfad für utils hinzufügen
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from scraping import scrape_bafa_modul3_pdf
from llm_assistant import bewerte_massnahme_beschreibung

st.set_page_config(page_title="Fördermittel-Agent", layout="centered")

# Förderprogrammdaten laden
@st.cache_data
def lade_daten():
    return pd.read_csv("data/foerderprogramme.csv")

df = lade_daten()

# App-Oberfläche
st.title("🔍 Fördermittel-Agent – EnMS NGD")
st.markdown("Finde passende Förderprogramme für geplante Energieeffizienzmaßnahmen.")

massnahme = st.selectbox(
    "Welche Maßnahme planen Sie?",
    sorted(df["Maßnahme"].unique().tolist())
)

zielgruppe = st.radio(
    "Gebäudetyp bzw. Zielgruppe:",
    df["Zielgruppe"].unique().tolist()
)

investition = st.number_input("Geschätzte Investitionshöhe (€)", min_value=1000, step=500)

if st.button("💡 Förderprogramme anzeigen"):
    # Matching-Funktion
    treffer = df[
        df["Maßnahme"].str.contains(massnahme, case=False) &
        df["Zielgruppe"].str.contains(zielgruppe, case=False)
    ].copy()

    if treffer.empty:
        st.warning("⚠️ Keine passenden Förderprogramme gefunden.")
    else:
        treffer["Geschätzte Förderung (€)"] = (treffer["Förderquote"] * investition).clip(
            upper=treffer["Max. Förderung (€)"]
        ).round(2)
        st.success(f"✅ {len(treffer)} passende Förderprogramme gefunden:")
        st.dataframe(treffer[[
            "Programmname", "Träger", "Maßnahme", "Förderquote",
            "Max. Förderung (€)", "Geschätzte Förderung (€)", "Link"
        ]])

# LLM-Analyse
st.markdown("## 🧠 Maßnahme-Erkennung per Freitext")
eingabe = st.text_area("Beschreiben Sie Ihre geplante Maßnahme oder Ihr Problem:")

if st.button("🔍 Analyse starten (LLM)"):
    if not eingabe.strip():
        st.warning("Bitte geben Sie eine Beschreibung ein.")
    else:
        with st.spinner("KI analysiert Ihre Eingabe…"):
            antwort = bewerte_massnahme_beschreibung(eingabe)
        st.markdown("### 📝 Ergebnis")
        st.markdown(antwort)

st.markdown("---")
st.caption("© Fördermittel-Agent – NGD Energiemanagement")
