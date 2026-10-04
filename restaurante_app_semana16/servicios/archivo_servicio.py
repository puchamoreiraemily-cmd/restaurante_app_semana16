import json
import os


class ArchivoServicio:

    @staticmethod
    def leer(ruta):
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError):
            return []

    @staticmethod
    def guardar(ruta, datos):
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )