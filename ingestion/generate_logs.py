import os
import shutil

SOURCE_FOLDER = "../Security-Log-Generator/logs"
DEST_FOLDER = "data/logs"


def copy_logs():
    os.makedirs(DEST_FOLDER, exist_ok=True)

    shutil.copy(f"{SOURCE_FOLDER}/ids.log", f"{DEST_FOLDER}/ids.log") #génération de logs IDs
    shutil.copy(f"{SOURCE_FOLDER}/access.log", f"{DEST_FOLDER}/access.log") #génération de logs access

    print("ids.log copié dans data/logs")
    print("access.log copié dans data/logs")


if __name__ == "__main__":
    copy_logs()