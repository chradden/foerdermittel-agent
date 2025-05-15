import openai
import streamlit as st

# OpenAI API-Key aus secrets oder Umgebung lesen
api_key = st.secrets.get("openai_api_key", None)
if not api_key:
    import os
    api_key = os.getenv("OPENAI_API_KEY", "sk-...")

client = openai.OpenAI(api_key=api_key)

def bewerte_massnahme_beschreibung(text):
    system_prompt = """Du bist ein Experte für Energiemanagement in sozialen Einrichtungen.
Wenn dir ein Nutzer eine freie Beschreibung gibt, identifizierst du daraus:
1. die mutmaßliche Maßnahme (z. B. LED-Umrüstung, Dämmung, Hydraulischer Abgleich)
2. passende Förderprogramme in Deutschland (z. B. KfW 297, BAFA Modul 3, Kommunalrichtlinie)
3. optional weitere Vorschläge für Maßnahmen

Antworte strukturiert in Markdown mit drei Abschnitten:
- 'Erkannte Maßnahme'
- 'Förderprogramme'
- 'Weitere Empfehlungen'
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
