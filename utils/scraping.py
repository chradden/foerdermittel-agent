import pandas as pd

def scrape_bafa_modul3_pdf():
    url = "https://www.bafa.de/SharedDocs/Downloads/DE/Energie/ee_wirtschaft_modul3_mer.pdf"

    # Rückgabe nur als Linktabelle
    data = {
        "Programmname": ["BAFA Modul 3"],
        "Träger": ["BAFA"],
        "Zielgruppe": ["Eigentum"],
        "Maßnahme": ["Energiemanagement-Software"],
        "Förderquote": [0.3],
        "Max. Förderung (€)": [10000],
        "Link": [url],
        "Kurzinfo": ["Das offizielle BAFA-Merkblatt Modul 3 steht unter dem folgenden Link als PDF zur Verfügung."]
    }

    return pd.DataFrame(data), url
