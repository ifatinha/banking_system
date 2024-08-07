import os
from pathlib import Path
from datetime import datetime
import inspect

file_path = Path(__file__).resolve().parents[1] / "logs" / "log.txt"


def log_operations(type_operation):

    def log_decorator(operation):
        def wrapper(*args, **kwargs):

            status = operation(*args, **kwargs)

            try:
                signature = inspect.signature(operation)
                log_txt = (
                    datetime.now().strftime("%d/%m/%Y %H:%M")
                    + " - "
                    + operation.__name__
                    + " - "
                    + str(signature)
                    + " - "
                    + str(status)
                    + "\n"
                )

                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(log_txt)
                else:
                    with open(file_path, "a", newline="") as file:
                        file.write(log_txt)

            except IOError as err:
                print(f"Erro ao criar o arquivo. {err}")

        return wrapper

    return log_decorator
