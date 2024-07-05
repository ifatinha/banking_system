import os
from pathlib import Path
from datetime import datetime

file_path = Path(__file__).parent / "logs" / "log.txt"


try:

    log_txt = datetime.now().strftime("%d/%m/%Y %H:%M") + " - " + + "\n"

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(log_txt)
    else:
        with open(file_path, "a", newline="") as file:
            file.write(log_txt)

except IOError as err:
    print("Erro ao criar o arquivo. {err}")

