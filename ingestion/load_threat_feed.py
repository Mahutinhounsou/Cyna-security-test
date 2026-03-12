import os
import csv

INPUT_FILE = "../ipsum/ipsum.txt"
OUTPUT_FILE = "data/threat_feed/malicious_ips.csv"


def load_threat_feed():

    malicious_ips = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            # ignorer commentaires et lignes vides
            if line.startswith("#") or line.strip() == "":
                continue

            parts = line.split()

            ip = parts[0]
            reports = parts[1]

            malicious_ips.append([ip, reports])

    # créer dossier si besoin
    os.makedirs("../data/threat_feed", exist_ok=True)

    # écrire le csv
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ip", "reports"])

        for row in malicious_ips:
            writer.writerow(row)

    print("Threat feed chargé.")
    print(f"{len(malicious_ips)} IP enregistrées.")


if __name__ == "__main__":
    load_threat_feed()