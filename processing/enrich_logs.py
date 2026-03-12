import os
import csv

THREAT_FILE = "data/threat_feed/malicious_ips.csv"
IDS_FILE = "data/logs/ids.log"
ACCESS_FILE = "data/logs/access.log"
OUTPUT_FILE = "data/enriched/enriched_logs.csv"


def main():

    # charger les IP malveillantes
    malicious_ips = {}

    with open(THREAT_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            malicious_ips[row["ip"]] = row["reports"]

    # créer le dossier enriched si nécessaire
    os.makedirs("data/enriched", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="") as outfile:

        writer = csv.writer(outfile)

        # écrire les colonnes
        writer.writerow([
            "log_type",
            "timestamp",
            "source_ip",
            "destination_ip",
            "is_malicious",
            "matched_ip",
            "reports",
            "raw_log"
        ])

        # ----------------------
        # traitement des logs IDS
        # ----------------------

        with open(IDS_FILE, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(" - ")

                # vérifier que la ligne contient assez d'informations
                if len(parts) < 5:
                    continue

                timestamp = parts[0]
                connection = parts[4]

                if " --> " not in connection:
                    continue

                src_part, dest_part = connection.split(" --> ")

                src_ip = src_part.split(":")[0]
                dest_ip = dest_part.split(":")[0]

                matched_ip = ""

                if src_ip in malicious_ips:
                    matched_ip = src_ip
                elif dest_ip in malicious_ips:
                    matched_ip = dest_ip

                is_malicious = matched_ip != ""
                reports = malicious_ips[matched_ip] if is_malicious else ""

                writer.writerow([
                    "ids",
                    timestamp,
                    src_ip,
                    dest_ip,
                    is_malicious,
                    matched_ip,
                    reports,
                    line
                ])

        # ----------------------
        # traitement des logs ACCESS
        # ----------------------

        with open(ACCESS_FILE, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(" - ")

                if len(parts) < 3:
                    continue

                timestamp = parts[0].strip("[]")
                client_ip = parts[2]

                is_malicious = client_ip in malicious_ips
                matched_ip = client_ip if is_malicious else ""
                reports = malicious_ips[client_ip] if is_malicious else ""

                writer.writerow([
                    "access",
                    timestamp,
                    client_ip,
                    "",
                    is_malicious,
                    matched_ip,
                    reports,
                    line
                ])

    print("Logs enrichis avec succès.")
    print(f"Fichier créé : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()