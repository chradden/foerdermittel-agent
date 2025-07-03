# 🔍 Fördermittel-Agent – EnMS NGD

Ein intelligenter Assistent zur Identifikation passender Förderprogramme für Energieeffizienzmaßnahmen in sozialen Einrichtungen.

## 📋 Übersicht

Der Fördermittel-Agent ist eine webbasierte Anwendung, die Nutzern dabei hilft, passende Förderprogramme für geplante Energieeffizienzmaßnahmen zu finden. Die Anwendung kombiniert eine strukturierte Datenbank mit KI-gestützter Analyse und bietet sowohl präzise Filteroptionen als auch Freitext-Analyse.

## ✨ Features

- **Strukturierte Förderprogramm-Suche**: Filterung nach Maßnahme, Zielgruppe und Investitionshöhe
- **KI-gestützte Maßnahme-Erkennung**: Automatische Identifikation von Maßnahmen aus Freitext-Beschreibungen
- **Förderungsberechnung**: Automatische Berechnung der geschätzten Förderung basierend auf Investitionshöhe
- **Umfassende Datenbank**: Integration verschiedener Förderprogramme (BAFA, KfW, Kommunalrichtlinie, etc.)
- **Benutzerfreundliche Oberfläche**: Intuitive Streamlit-basierte Webanwendung

## 🚀 Installation

### Voraussetzungen

- Python 3.8 oder höher
- OpenAI API-Key (für KI-Funktionen)

### Setup

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd foerdermittel-agent
   ```

2. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

3. **OpenAI API-Key konfigurieren**
   
   Erstellen Sie eine `.streamlit/secrets.toml` Datei:
   ```toml
   openai_api_key = "ihr-openai-api-key-hier"
   ```
   
   Alternativ können Sie die Umgebungsvariable setzen:
   ```bash
   export OPENAI_API_KEY="ihr-openai-api-key-hier"
   ```

4. **Anwendung starten**
   ```bash
   streamlit run main.py
   ```

## 📁 Projektstruktur

```
foerdermittel-agent/
├── main.py                 # Hauptanwendung (Streamlit App)
├── requirements.txt        # Python-Abhängigkeiten
├── data/
│   └── foerderprogramme.csv # Förderprogramm-Datenbank
├── utils/
│   ├── llm_assistant.py    # OpenAI Integration für KI-Analyse
│   └── scraping.py         # Web-Scraping Funktionen
└── README.md              # Diese Datei
```

## 🎯 Verwendung

### Strukturierte Suche

1. Wählen Sie die geplante Maßnahme aus der Dropdown-Liste
2. Wählen Sie den Gebäudetyp/Zielgruppe
3. Geben Sie die geschätzte Investitionshöhe ein
4. Klicken Sie auf "Förderprogramme anzeigen"

### KI-gestützte Analyse

1. Beschreiben Sie Ihre geplante Maßnahme im Freitext-Feld
2. Klicken Sie auf "Analyse starten (LLM)"
3. Die KI identifiziert automatisch:
   - Die erkannte Maßnahme
   - Passende Förderprogramme
   - Weitere Empfehlungen

## 📊 Förderprogramme

Die Anwendung unterstützt derzeit folgende Förderprogramme:

- **BAFA Modul 3**: Energiemanagement-Software
- **Kommunalrichtlinie**: LED-Umrüstung
- **KfW 278**: Zählernachrüstung
- **KfW 297/298**: Gebäudesanierung
- **BAFA Modul 1**: Querschnittstechnologien
- **Weitere**: co2online, BMWK Förderinfo, etc.

## 🔧 Technische Details

### Technologie-Stack

- **Frontend**: Streamlit
- **Datenverarbeitung**: Pandas
- **KI-Integration**: OpenAI GPT-4
- **Web-Scraping**: BeautifulSoup4, Requests

### API-Integration

Die Anwendung nutzt die OpenAI API für:
- Maßnahme-Erkennung aus Freitext
- Förderprogramm-Empfehlungen
- Strukturierte Antworten in Markdown-Format

## 🤝 Beitragen

1. Fork das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## 📝 Lizenz

Dieses Projekt ist für interne Zwecke der NGD Energiemanagement entwickelt.

## 👥 Autoren

- **NGD Energiemanagement** - *Entwicklung und Wartung*

## 🙏 Danksagungen

- OpenAI für die KI-Integration
- Streamlit für das Web-Framework
- BAFA, KfW und andere Fördergeber für die bereitgestellten Daten

---

**© Fördermittel-Agent – NGD Energiemanagement** 