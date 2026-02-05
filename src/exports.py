import os
import csv
from datetime import datetime

from src.config import EXPORTS_FOLDER


def exporter_csv(client, shopping):
    os.makedirs(EXPORTS_FOLDER, exist_ok=True)

    dossier_client = os.path.join(EXPORTS_FOLDER, client)
    os.makedirs(dossier_client, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"{client}_{timestamp}.csv"
    chemin = os.path.join(dossier_client, nom_fichier)

    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["client", "date", "article"])
        for item in shopping:
            writer.writerow([client, timestamp, item])

    print(f"✅ Export CSV créé : {chemin}")
