Applied Programming: StudyBuddy API & Frontend
Dieses Projekt wurde im Rahmen des Moduls Angewandte Programmierung (Wirtschaftsinformatik) an der Hochschule Coburg entwickelt. Es umfasst ein robustes FastAPI-Backend zur Verwaltung von Notizen und Kursen sowie ein interaktives Streamlit-Frontend.

🚀 Features
📝 Note Management API (v2.0)
Vollständiges CRUD: Erstellen, Lesen, Aktualisieren (PUT/PATCH) und Löschen von Notizen.

Erweiterte Filterung: Filtern nach Kategorien, Schlagworten (Tags), Volltextsuche und Erstellungsdatum (ISO-Format).

Statistiken: Endpunkt für globale Metriken wie Gesamtzahl der Notizen, Top-Tags und Verteilung pro Kategorie.

Datenbank: Migration von JSON-Dateien auf eine SQLite-Datenbank mittels SQLModel.

📚 Course Catalog
Verwaltung von Modulen inklusive Kurs-Code, ECTS, Semester und Dozenten.

Persistenz: Speicherung der Kursdaten in einer courses.json Datei.

Validierung: Duplikaterkennung für Kurs-Codes (409 Conflict).

🎨 Frontend
Streamlit Dashboard: Eine grafische Oberfläche zum Anzeigen aller Notizen und zum Erstellen neuer Einträge über ein Formular.

Session State: Konsistente Datenhaltung während der Benutzerinteraktion.

🛠 Tech Stack
Backend: FastAPI

Datenbank / ORM: SQLModel (Pydantic + SQLAlchemy)

Frontend: Streamlit

Testing: Pytest & Requests

Package Manager: uv

📦 Installation & Setup
Voraussetzungen: Stelle sicher, dass uv auf deinem System installiert ist.

Abhängigkeiten installieren:

PowerShell
uv sync
Backend starten:

PowerShell
uv run fastapi dev main.py
Die API-Dokumentation findest du anschließend unter http://127.0.0.1:8000/docs.

Frontend starten:

PowerShell
uv run streamlit run frontend.py
🧪 Testing
Das Projekt enthält eine umfassende Test-Suite in test_main.py, die sowohl funktionale CRUD-Tests als auch Performance-Benchmarks umfasst.

Alle Tests ausführen:

PowerShell
uv run pytest test_main.py -v
Nur Performance-Tests:

PowerShell
uv run pytest test_main.py -v -m performance
📂 Projektstruktur
main.py: Zentraler API-Code (Notizen & Kurse).

test_main.py: Umfassende Test-Suite und Performance-Checks.

frontend.py: Streamlit Applikation.

notes.db: SQLite Datenbank für persistente Notizen.

courses.json: JSON-Speicher für den Kurs-Katalog.