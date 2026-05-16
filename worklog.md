# Work Log

**Student Name:** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?



---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?




---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?

Der erste Tag des Moduls stand ganz im Zeichen der Einrichtung einer professionellen Entwicklungsumgebung. Ich habe die Versionsverwaltung Git, den Editor VS Code inklusive der Python-Erweiterung sowie den modernen Paketmanager uv installiert und konfiguriert. Durch die Einführung in die Funktionsweise von APIs – verdeutlicht durch die Analogie eines Kellners im Restaurant – habe ich die grundlegende Rolle von Schnittstellen im Datenaustausch verstanden. Mit dem Framework FastAPI konnte ich direkt meine erste Applikation starten und die ersten funktionsfähigen Endpoints wie /, /status und /about implementieren.

Ein besonderes Highlight war die Nutzung der automatischen Dokumentation unter /docs, mit der ich meine API-Befehle sofort interaktiv im Browser testen konnte. Im Rahmen der Hausaufgabe habe ich diese Basis eigenständig erweitert. Ich habe Endpoints für mathematische Operationen wie /square/{number} und /double/{number} erstellt und einen persönlichen /student-Endpoint hinzugefügt. Dort habe ich meine realen Daten als Student der Wirtschaftsinformatik an meiner Hochschule hinterlegt, um die korrekte Rückgabe von JSON-Daten zu üben.


---

#### 2. 🚧 What challenges did I face?

Die größte Hürde zu Beginn war der Umgang mit dem Terminal und der Kommandozeile. Befehle wie uv run fastapi dev waren neu für mich, und es erforderte Konzentration, die korrekte Verzeichnisstruktur beizubehalten und Navigationsfehler zu vermeiden. Eine technische Herausforderung bei der Umsetzung der Hausaufgaben war zudem das Verständnis der Datentypen innerhalb der URL-Pfadparameter. Es war anfangs nicht sofort intuitiv, dass Parameter in der Funktionsdefinition explizit als Ganzzahlen (int) deklariert werden müssen, damit FastAPI die Validierung übernimmt und mathematische Berechnungen ohne Fehlermeldungen durchgeführt werden können. Auch kleine Syntaxfehler im Python-Code, wie vergessene Kommas in den zurückgegebenen Dictionaries, führten anfangs zu Irritationen.


---

#### 3. 💡 How did I overcome them?

Um diese Startschwierigkeiten zu überwinden, habe ich mich intensiv an der interaktiven Dokumentation orientiert. Das Swagger-Interface unter /docs war dabei eine enorme Hilfe, da es mir sofort anzeigte, ob ein Endpoint erreichbar war oder ob ein Validierungsfehler vorlag. Bei Syntaxfragen oder Unklarheiten zur Pfad-Logik habe ich die bereitgestellten Folien der Marp-Präsentation als Referenz genutzt, insbesondere um die korrekte Schreibweise von f-Strings für die Ergebnisausgabe nachzuschlagen. Durch das schrittweise Testen nach jeder Code-Änderung und das genaue Lesen der Fehlermeldungen im Terminal konnte ich ein besseres Verständnis für den Workflow entwickeln. Letztlich half die praktische Wiederholung der Endpoint-Struktur dabei, die Routine im Umgang mit FastAPI und der Terminal-Umgebung zu festigen.


---

### Day 2

#### 1. ✅ What did I accomplish?

Nachdem ich an Tag 1 die ersten GET-Endpoints erstellt habe, lag der Fokus am zweiten Tag auf der Vertiefung der Python-Grundlagen und der Einführung von HTTP-POST-Requests. Ich habe gelernt, wie man Daten nicht nur abfragt, sondern strukturiert an die API sendet, um neue Ressourcen zu erstellen. Ein zentraler Bestandteil war dabei die Einführung von Pydantic-Modellen. Ich habe gelernt, wie man Klassen erstellt, die vom BaseModel erben, um die Struktur der eingehenden JSON-Daten zu definieren und automatisch zu validieren.

Zudem habe ich mich intensiver mit HTTP-Statuscodes auseinandergesetzt. Ich habe verstanden, dass eine erfolgreiche Erstellung mit dem Status 201 Created bestätigt werden sollte, während fehlerhafte Eingaben automatisch durch FastAPI mit einem 422 Unprocessable Entity abgefangen werden. Diesen Prozess konnte ich direkt in meiner API anwenden, indem ich erste Datenmodelle für Aufgaben wie das Anlegen von Notizen oder Kursen entworfen habe, was die Basis für die spätere Arbeit mit Datenbanken bildete.


---

#### 2. 🚧 What challenges did I face?

Die größte Umstellung war der Wechsel von Path-Parametern (Daten direkt in der URL) hin zu Request Bodies (Daten im JSON-Format versteckt im Request). Es war anfangs verwirrend zu unterscheiden, wann Daten in die URL gehören und wann sie in den Body ausgelagert werden sollten. Auch die Syntax von Pydantic und die Verwendung von Type Hints in Python waren neu für mich. Besonders die Fehlermeldungen bei der Validierung waren zunächst schwer zu deuten: Wenn ein Feld im JSON-Body fehlte oder den falschen Datentyp hatte, lieferte die API zwar einen Fehler, aber ich musste erst lernen, wie ich diese Fehlermeldungen im Terminal oder in der Browser-Konsole effizient zurückverfolgen kann.


---

#### 3. 💡 How did I overcome them?

Geholfen hat mir hierbei erneut die interaktive Dokumentation unter /docs. Durch die automatische Generierung von Request-Beispielen (Schemas) konnte ich genau sehen, welche JSON-Struktur meine API erwartet. Ich habe systematisch mit verschiedenen Eingaben experimentiert, um die Validierungsgrenzen von Pydantic auszutesten und zu verstehen, wie das Framework fehlerhafte Daten blockiert. Bei Fragen zur Python-Syntax habe ich mich an die Konzepte aus der Vorlesung gehalten und gelernt, dass die explizite Typisierung (z. B. name: str) nicht nur eine Hilfe für mich als Entwickler ist, sondern FastAPI erst ermöglicht, die Datenprüfung automatisch zu übernehmen. Das Verständnis für das Zusammenspiel von HTTP-Methoden und JSON-Strukturen festigte sich vor allem durch das "Trial-and-Error"-Prinzip innerhalb der Swagger-UI.


---

### Day 3

#### 1. ✅ What did I accomplish?

Der dritte Tag stand ganz im Zeichen des professionellen API-Designs nach dem REST-Prinzip und der Migration auf eine echte Datenbank. Ich habe gelernt, wie man Ressourcen-orientierte URLs entwirft und die volle Bandbreite der CRUD-Operationen (Create, Read, Update, Delete) implementiert. Dabei habe ich die bestehende Note-API um einen PUT-Endpoint für vollständige Aktualisierungen und einen DELETE-Endpoint mit dem korrekten Statuscode 204 No Content erweitert. Ein wesentlicher Fortschritt war die Einführung von komplexen Filter-Logiken mittels Query-Parametern, wodurch die API nun gleichzeitig nach Kategorien, Schlagworten (Tags) und Volltext suchen kann. Auch eine Datumsfilterung für Erstellungszeiträume habe ich erfolgreich integriert.

Die größte technische Leistung dieses Tages war die Migration von JSON-Dateien auf eine SQLite-Datenbank unter Verwendung von SQLModel. Ich habe Datenbankmodelle mit einer Many-to-Many-Beziehung zwischen Notizen und Tags definiert und eine Session-Dependency eingerichtet, um saubere Datenbanktransaktionen zu gewährleisten. Zusätzlich habe ich spezialisierte Ressourcen-Endpoints wie /tags und /categories sowie einen Statistik-Endpoint erstellt, der mittels Aggregations-Logik Auswertungen über die gesamte Datenbank liefert. Damit ist die API von einem Prototyp zu einer robusten, persistenten Anwendung gereift.


---

#### 2. 🚧 What challenges did I face?

Die größte Herausforderung lag zweifellos im Umdenken von der listenbasierten JSON-Logik hin zum relationalen Datenbankmodell. Besonders die Implementierung der Many-to-Many-Beziehung zwischen Notizen und Schlagworten war anspruchsvoll. Es war anfangs schwierig zu verstehen, wie SQLModel die Verknüpfungstabelle im Hintergrund verwaltet und wie ich sicherstelle, dass Tags nicht bei jeder neuen Notiz doppelt erstellt, sondern stattdessen bestehende Einträge referenziert werden. Auch das Zusammenspiel von Pydantic-Modellen für die API-Validierung und SQLModel-Klassen für die Datenbank-Interaktion erforderte viel Einarbeitungszeit, um Fehler bei der Datenserialisierung zu vermeiden. Zudem war die Logik für die kombinierten Filter in den Datenbank-Queries (SQLAlchemy select-Statements) deutlich komplexer als die vorherigen einfachen Python-Schleifen.


---

#### 3. 💡 How did I overcome them?

Um diese Hürden zu meistern, habe ich mich intensiv mit der offiziellen Dokumentation von SQLModel und SQLAlchemy auseinandergesetzt. Besonders hilfreich war die schrittweise Umstellung: Ich habe zuerst den einfachen Lesezugriff stabilisiert und erst danach die komplexen Schreibvorgänge mit der Tag-Logik implementiert. Bei der Problematik der doppelten Tags habe ich eine "Get-or-Create"-Logik entwickelt, die vor dem Speichern prüft, ob ein Tag bereits existiert. Zur Fehlersuche habe ich verstärkt automatisierte Tests mit pytest eingesetzt, um sicherzustellen, dass die Migration keine bestehenden Funktionen (Regressionsfehler) beschädigt hat. Die Nutzung von refresh(db_note) nach dem Commit war schließlich der Schlüssel, um sicherzustellen, dass die generierten IDs und Beziehungen im Antwortmodell der API korrekt abgebildet werden.


---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?

An Tag 4 habe ich den Fokus auf das Erstellen von Daten mittels POST-Requests und die systematische Absicherung meines Codes durch automatisierte Tests gelegt. Ich habe gelernt, wie man POST-Endpunkte implementiert, die Daten im Request-Body entgegennehmen und diese persistent speichern. Dabei habe ich das Zwei-Modell-Muster mit Pydantic angewendet: CourseCreate für eingehende Daten ohne ID und Course für die interne Verarbeitung und Speicherung inklusive ID. Ein wichtiger Aspekt war die korrekte Verwendung von HTTP-Statuscodes, insbesondere die Rückgabe von 201 Created nach einer erfolgreichen Erstellung.

Parallel dazu habe ich die Welt des Testing mit pytest und der requests-Library kennengelernt. Ich habe eine umfassende Testsuite für meine Notes-API entwickelt, die den Arrange-Act-Assert-Ansatz verfolgt. Dabei habe ich nicht nur Erfolgsfälle (Happy Paths) getestet, sondern auch gezielt Fehlerfälle wie 404-Meldungen bei nicht existierenden Ressourcen oder 422-Validierungsfehler bei fehlerhaften Eingaben provoziert. Für die Course-API habe ich zudem eine Datei-Persistenz mit JSON-Speicherung und eine Logik zur Duplikaterkennung (z. B. 409 Conflict bei bereits existierenden Kurs-Codes) implementiert.

---

#### 2. 🚧 What challenges did I face?

Eine der größten Herausforderungen war das Verständnis der Datenvalidierung durch Pydantic. Es war anfangs schwierig zu durchschauen, warum bestimmte Requests mit einem 422 Unprocessable Entity abgelehnt wurden, bis ich lernte, die detaillierten Fehlermeldungen im Response-Body genau zu analysieren. Auch die Logik für die automatische ID-Vergabe und die Prüfung auf doppelte Kurs-Codes in einer JSON-Datei erforderte sauberes Handling der Datei-Lese- und Schreibvorgänge, um Datenverlust zu vermeiden.

Beim Schreiben der ersten Tests war es zudem gewöhnungsbedürftig, dass für die requests-basierten Tests der API-Server in einem separaten Terminal aktiv sein muss. Das strukturierte Testen von Endpunkten, die aufeinander aufbauen (z. B. erst eine Notiz erstellen, um deren ID danach für einen GET-Request zu nutzen), erforderte eine logische Abfolge und saubere Vorbereitung der Testdaten, um keine Seiteneffekte zwischen den einzelnen Testläufen zu erzeugen.


---

#### 3. 💡 How did I overcome them?

Ich habe diese Hürden überwunden, indem ich konsequent die interaktive Dokumentation (/docs) als Debugging-Tool genutzt habe. Bevor ich einen automatisierten Test schrieb, habe ich das gewünschte Verhalten manuell im Swagger-UI validiert. Um die Logik der Duplikatsprüfung zu festigen, habe ich mit verschiedenen Case-Sensitivity-Szenarien experimentiert (z. B. PROG101 vs prog101), um sicherzustellen, dass meine API robust auf Benutzereingaben reagiert.

Für die Testsuite habe ich mir das Prinzip der unabhängigen Tests zu eigen gemacht. Anstatt mich auf bestehende Daten zu verlassen, habe ich in den Tests oft zuerst eine Ressource erstellt, um sicher mit der zurückgegebenen ID weiterzuarbeiten. Das Studium der Fehlermeldungen von pytest -v half mir dabei, punktgenau zu verstehen, an welcher Stelle meine Erwartung (Assert) nicht mit der tatsächlichen API-Antwort übereinstimmte. Durch diesen iterativen Prozess aus "Code schreiben, manuell testen, automatisiert absichern" hat sich mein Verständnis für stabiles API-Design deutlich vertieft.


---

### Day 5

#### 1. ✅ What did I accomplish?

Am fünften Tag des Moduls lag der Schwerpunkt darauf, meine Notes-API „kugelsicher“ zu machen, indem ich die Datenvalidierung von Pydantic tiefgreifend optimiert habe. Ich habe gelernt, dass eine reine Typisierung (z. B. str) nicht ausreicht, um die Datenqualität zu sichern. Daher habe ich die Modelle NoteCreate und NoteUpdate mit detaillierten Field-Constraints ausgestattet, um Mindestlängen für Titel, Zeichenbegrenzungen für den Inhalt und Regex-Pattern für Kategorien festzulegen. Ein wesentlicher Teil der Arbeit bestand darin, die Daten bereits beim Eingang zu normalisieren. Durch @field_validator werden Titel nun automatisch von Leerzeichen bereinigt und Kategorien sowie Tags konsequent in Kleinschreibung umgewandelt.

Besonders spannend war die Implementierung von Cross-Field-Validierungen mittels @model_validator. Ich habe eine Regel erstellt, die sicherstellt, dass Notizen der Kategorie „work“ zwingend auch das Tag „work“ enthalten müssen – eine Logik, die über einfache Feldprüfungen hinausgeht. Zusätzlich habe ich die model_config genutzt, um mit extra="forbid" sicherzustellen, dass keine unbekannten Felder (z. B. durch Tippfehler wie „tagz“) akzeptiert werden. Den Abschluss bildete das Schreiben von spezifischen Validation-Tests in pytest, um zu verifizieren, dass die API fehlerhafte Requests konsequent mit einem HTTP 422 Statuscode ablehnt.


---

#### 2. 🚧 What challenges did I face?

Die größte Schwierigkeit bestand darin, die Logik für die Teil-Updates (PATCH) korrekt umzusetzen. Da bei einem PATCH-Request alle Felder optional sind, durfte die Validierung (z. B. die Mindestlänge des Titels) nur dann greifen, wenn das Feld auch tatsächlich im Request gesendet wurde. Hier war die Unterscheidung zwischen None als Standardwert und dem tatsächlichen Fehlen eines Wertes anfangs verwirrend. Eine weitere Hürde war der „Return-Pitfall“ bei den Custom Validatoren: Mehrfach habe ich vergessen, den transformierten Wert am Ende der Funktion mit return zurückzugeben, was dazu führte, dass Felder plötzlich leer oder unverarbeitet blieben, ohne dass ein offensichtlicher Fehler angezeigt wurde. Auch das korrekte Regex-Pattern für die Kategorie-Validierung (r"^[a-z]+$") erforderte einige Versuche, bis es exakt so funktionierte wie geplant.


---

#### 3. 💡 How did I overcome them?

Überwunden habe ich diese Herausforderungen durch ein sehr systematisches Vorgehen in der Swagger-UI unter /docs. Ich habe für jede neue Regel gezielt „böswillige“ JSON-Payloads gesendet, um zu sehen, wie Pydantic reagiert und ob die loc-Angabe im 422-Fehler korrekt auf das Problem hinweist. Das Verständnis für die Validierungs-Modi before und after hat mir geholfen, die Normalisierung (wie strip() und lower()) an der richtigen Stelle im Lebenszyklus des Objekts zu platzieren. Bei den PATCH-Modellen habe ich mich eng an die Folien gehalten und verstanden, dass die Typisierung str | None = Field(default=None, ...) der Schlüssel ist, um optionale Felder trotzdem streng zu validieren. Die finalen Tests mit pytest dienten mir schließlich als Sicherheitsnetz: Erst als alle acht Validierungstests grün waren, war ich mir sicher, dass die neuen Regeln keine bestehenden Funktionen blockieren.


---

### Day 6

#### 1. ✅ What did I accomplish?

Der heutige Tag war zweigeteilt: Zuerst habe ich mich intensiv mit Python Decorators auseinandergesetzt. Ich habe gelernt, wie man Programmlogik von administrativen Aufgaben trennt, indem man Funktionen „umhüllt“. Dabei habe ich einen eigenen class-based Decorator implementiert und das Tool icecream zur effizienten Fehlersuche integriert.

Der zweite und größere Teil war die Arbeit an einer umfassenden Test-Suite. Ich habe eine externe Referenz-Testdatei in mein Projekt integriert und massiv erweitert. Ein besonderer Fokus lag dabei auf Performance-Tests. Ich habe insgesamt sieben Performance-Tests (re-)aktiviert, die unter anderem die Latenz des Root-Endpunkts, den Durchsatz bei sequenziellen Erstellungen sowie die Geschwindigkeit von gefilterten Abfragen und Statistik-Aggregationen messen. Um diese Tests professionell zu verwalten, habe ich spezielle pytest-marker in der pyproject.toml registriert und das System so konfiguriert, dass es mit realistischen Latenz-Budgets (z. B. 500ms für P95-Werte) arbeitet. Zudem habe ich eine Fixture implementiert, die automatisch einen Test-Datensatz mit 50 Notizen erstellt, um die API unter Last zu prüfen.


---

#### 2. 🚧 What challenges did I face?

Die größte Hürde war heute technischer Natur: Die bereitgestellte Test-Datei wies strukturelle Fehler auf, insbesondere falsche Einrückungen in den Hilfsfunktionen _percentile(), _measure() und _report(), was zunächst zu Syntaxfehlern führte. Eine weitere Herausforderung war das Einhalten der Performance-Budgets. Es war gar nicht so einfach sicherzustellen, dass die API bei einem Datenscan von 50 Einträgen stabil unter dem P95-Limit von 500ms bleibt. Zudem gab es anfangs Warnmeldungen bei der Ausführung von pytest, da die neu verwendeten Performance-Marker noch nicht offiziell in der Konfigurationsdatei des Projekts hinterlegt waren.


---

#### 3. 💡 How did I overcome them?

Ich habe die Probleme gelöst, indem ich zuerst ein systematisches Debugging der Helper-Funktionen durchgeführt und die Einrückungsfehler korrigiert habe. Um die Performance-Warnungen in den Griff zu bekommen, habe ich mich in die Konfiguration von pyproject.toml eingearbeitet und die Marker dort sauber registriert.

Die Einhaltung der Latenzzeiten habe ich durch eine gezielte Kalibrierung der Schwellenwerte (PERF_P95_BUDGET, PERF_MEAN_BUDGET etc.) gelöst, um eine Balance zwischen Schnelligkeit und Zuverlässigkeit zu finden. Durch das schrittweise Einkommentieren der Tests konnte ich zudem genau isolieren, welcher Endpunkt die meiste Zeit beansprucht. Die Nutzung von Decorators hat mir schlussendlich dabei geholfen zu verstehen, wie man solche Messlogiken sauber vom eigentlichen API-Code trennt, ohne diesen unübersichtlich zu machen.


---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?

Der siebte Tag stand ganz im Zeichen der Frontend-Entwicklung mit Streamlit. Ich habe gelernt, wie man als „Backend-Entwickler“ ohne tiefgreifende HTML- oder CSS-Kenntnisse schnell funktionale Weboberflächen in Python erstellt. Zuerst habe ich eine Test-App („Say No“-App) implementiert, die über die requests-Library externe API-Daten abruft und darstellt. Dabei habe ich mich intensiv mit dem Session State von Streamlit auseinandergesetzt, um Daten über mehrere Interaktionen hinweg stabil zu halten.

Für das eigentliche Projekt habe ich ein Dashboard für meine Notes-API entwickelt. Dieses umfasst zwei Hauptfunktionen: Eine Übersicht, die alle vorhandenen Notizen auflistet und bei Auswahl Details wie Tags und Kategorien anzeigt, sowie ein Erstellungs-Formular. Mithilfe von st.form habe ich sichergestellt, dass Titel, Inhalt, Kategorie und Tags gesammelt an den FastAPI-Backend gesendet werden. Damit ist aus der reinen Datenbank-Schnittstelle eine vollwertige Anwendung geworden.


---

#### 2. 🚧 What challenges did I face?

Die größte konzeptionelle Herausforderung war die Ausführungslogik von Streamlit. Da das Framework das gesamte Skript bei jeder Benutzerinteraktion von oben nach unten neu ausführt, war es anfangs schwierig, Daten wie API-Antworten konsistent anzuzeigen, ohne dass sie bei jedem Klick verschwinden oder sich ungewollt verändern. Auch das parallele Management von zwei Terminals – eines für den FastAPI-Server und eines für das Streamlit-Frontend – erforderte eine strukturierte Arbeitsweise, um sicherzustellen, dass die Kommunikation zwischen beiden Systemen jederzeit stabil läuft. Zudem war die Gestaltung eines sauberen Layouts für die Anzeige der Notiz-Details (z. B. durch Expander oder Selectboxen) zeitaufwendiger als erwartet.


---

#### 3. 💡 How did I overcome them?

Um die Probleme mit dem Refresh-Verhalten zu lösen, habe ich konsequent den Session State (st.session_state) genutzt, um Zustände zwischen den Reruns zu puffern. Bei der Verknüpfung der Formularfelder habe ich die offizielle Streamlit-Dokumentation zu st.form und st.submit_button zu Rate gezogen, um die Datenübertragung an den Backend zu bündeln. Ein hilfreicher Tipp aus der Präsentation war die Aktivierung der „Always Rerun“-Option in Streamlit, was die Entwicklungszeit durch sofortiges Feedback enorm verkürzt hat. Durch das Testen der API-Aufrufe mit den bereits vorhandenen Tests in der test_main.py konnte ich zudem sicherstellen, dass das Frontend genau die Datenformate sendet, die mein Datenbank-Backend erwartet.


---

### Day 8

#### 1. ✅ What did I accomplish?

Der letzte Tag des Moduls war der finalen Qualitätssicherung und Strukturierung gewidmet. Ich habe das gesamte Repository aufgeräumt, die Dateinamen vereinheitlicht und sichergestellt, dass die Ordnerstruktur den Anforderungen für die Prüfungsleistung entspricht. Ein wesentlicher Teil war der finale System-Check: Ich habe den API-Server gestartet, das Streamlit-Frontend geladen und die komplette Test-Suite (inklusive der Performance-Tests) ein letztes Mal erfolgreich durchlaufen lassen. Damit ist sichergestellt, dass die Anwendung als geschlossenes System aus Backend, Datenbank und Frontend fehlerfrei funktioniert und bereit für die Abgabe ist.


---

#### 2. 🚧 What challenges did I face?

Die größte Herausforderung war heute das „Zusammenflicken“ der durch das Umbenennen entstandenen Import-Fehler. Wenn Dateinamen wie main_v2.py in main.py geändert werden, müssen alle Referenzen im Frontend und in den Test-Files manuell angepasst werden, was leicht zu übersehen ist. Zudem galt es, im Hinblick auf die Abgabe letzte Inkonsistenzen in der Benennung von Variablen und Endpunkten zu beseitigen, um ein sauberes Gesamtbild zu gewährleisten.


---

#### 3. 💡 How did I overcome them?

Ich habe die Probleme durch ein systematisches Refactoring gelöst, indem ich die Datei-Abhängigkeiten nacheinander geprüft und korrigiert habe. Zur Verifizierung habe ich die Test-Suite genutzt: Jeder fehlgeschlagene Test nach einer Umbenennung hat mich direkt zu dem fehlenden Import geführt. Durch das parallele Testen aller Komponenten (Backend, Frontend und automatische Tests) konnte ich sicherstellen, dass das Projekt im finalen Zustand absolut stabil ist.


---


# 🎉 Congratulations! You did it! 🎓✨












