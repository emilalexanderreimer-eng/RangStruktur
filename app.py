"""Rangstruktur – Desktop-App (pywebview / Edge WebView2).

Startet ein natives Fenster mit dem Mind-Map-Editor.
Daten liegen in %APPDATA%\\Rangstruktur\\daten.json.
"""
import base64
import json
import os
import sys

import webview

APP_DIR = os.path.join(os.environ.get("APPDATA", os.path.dirname(os.path.abspath(__file__))), "Rangstruktur")
DATA_FILE = os.path.join(APP_DIR, "daten.json")
# Als PyInstaller-Exe liegt die HTML im entpackten Temp-Verzeichnis (_MEIPASS)
_BASE = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
HTML_FILE = os.path.join(_BASE, "rangstruktur.html")

window = None


class Api:
    def save_data(self, text):
        os.makedirs(APP_DIR, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(text)
        return True

    def load_data(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except OSError:
            return None

    def export_json(self, text):
        path = window.create_file_dialog(
            webview.SAVE_DIALOG,
            save_filename="rangstruktur.json",
            file_types=("JSON Datei (*.json)",),
        )
        if not path:
            return False
        if isinstance(path, (list, tuple)):
            path = path[0]
        # Hübsch formatiert exportieren, damit die Datei auch von Hand lesbar ist
        try:
            text = json.dumps(json.loads(text), ensure_ascii=False, indent=2)
        except ValueError:
            pass
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True

    def export_png(self, data_url):
        path = window.create_file_dialog(
            webview.SAVE_DIALOG,
            save_filename="rangstruktur.png",
            file_types=("PNG Bild (*.png)",),
        )
        if not path:
            return False
        if isinstance(path, (list, tuple)):
            path = path[0]
        data = base64.b64decode(data_url.split(",", 1)[1])
        with open(path, "wb") as f:
            f.write(data)
        return True

    def import_json(self):
        paths = window.create_file_dialog(
            webview.OPEN_DIALOG,
            file_types=("JSON Datei (*.json)", "Alle Dateien (*.*)"),
        )
        if not paths:
            return None
        with open(paths[0], "r", encoding="utf-8") as f:
            return f.read()


if __name__ == "__main__":
    window = webview.create_window(
        "Rangstruktur",
        HTML_FILE,
        js_api=Api(),
        width=1200,
        height=800,
        min_size=(700, 450),
    )
    webview.start()
