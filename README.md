# Rangstruktur

Ein Mind-Map-Editor für Rangstrukturen (Organigramme): Positionen mit Titel + Name,
frei platzierbare Textfelder und dynamische Pfeile, die an Karten und Textfeldern
angebunden bleiben. Export als PNG-Bild oder JSON-Datei.

## Direkt im Browser nutzen

**➡ https://emilalexanderreimer-eng.github.io/rangstruktur/**

Keine Installation nötig — läuft komplett im Browser und speichert lokal.

## Als Windows-App

Unter [Releases](../../releases) gibt es `Rangstruktur.exe` — eine eigenständige
Windows-App ohne Abhängigkeiten (einfach herunterladen und starten; die
SmartScreen-Warnung beim ersten Start mit „Weitere Informationen → Trotzdem
ausführen" bestätigen).

Alternativ mit Python starten: `pip install pywebview`, dann `python app.py`.

## Bedienung

| Aktion | So geht's |
|---|---|
| Position auswählen | Klick |
| Titel/Name bearbeiten | Klick auf ausgewählte Karte (oder Doppelklick / F2) |
| Untergebenen anlegen | Tab oder „+ Untergeordnet" |
| Gleichrangigen anlegen | Enter oder „+ Gleichrangig" |
| Zweig löschen | Entf |
| Zweig umhängen | Karte auf neue Vorgesetzten-Karte ziehen |
| Textfeld | „+ Textfeld", ziehen zum Verschieben, Ecke unten rechts für Größe |
| Pfeil verbinden | „↗ Pfeil", dann von Karte/Textfeld zum Ziel ziehen |
| Rückgängig | Strg+Z |
| Ansicht | Fläche ziehen (verschieben), Scrollen (zoomen), „Einpassen" |
