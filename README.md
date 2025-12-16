Menedżer Zadań (Flask + SQLAlchemy + Marshmallow)
flask-task-manager to nowoczesna aplikacja webowa zbudowana na frameworku Flask, służąca do zarządzania zadaniami i użytkownikami. Projekt implementuje pełny CRUD (Create, Read, Update, Delete) w dwóch warstwach: jako REST API (JSON) dla klientów zewnętrznych oraz jako Przyjazny Interfejs GUI (HTML) dla użytkowników końcowych.

Jest to projekt demonstracyjny mający na celu zaprezentowanie architektury aplikacji Flask opartej na wzorcu Application Factory i Blueprintach, z wykorzystaniem SQLAlchemy jako ORM.🛠️ TechnologieElementTechnologiaOpisFrameworkFlaskLekki framework webowy w Pythonie.Baza DanychSQLAlchemyPython SQL Toolkit i Object Relational Mapper (ORM).

Framework: Flask
Baza Danych SQLAlchemy
Serializacja: Marshmallow
Formularze: Flask-WTF
Struktura: Blueprints & Application Factory

2. Konfiguracja Środowiska Wirtualnego (VENV)Ważne: Zawsze używaj środowiska wirtualnego, aby izolować zależności projektu.

Bash# Utwórz środowisko wirtualne:
python -m venv .venv

Aktywuj środowisko wirtualne
# Dla Windows (CMD/PowerShell):
.venv\Scripts\activate
# Dla macOS/Linux:
source .venv/bin/activate

3. Instalacja Zależności

Zainstaluj wymagane pakiety Pythona:
pip install -r requirements.txt
(Jeśli plik requirements.txt nie istnieje, możesz go wygenerować ręcznie za pomocą pip freeze > requirements.txt po zainstalowaniu Flask, Flask-SQLAlchemy, Flask-Marshmallow, Flask-WTF i marshmallow-sqlalchemy).4. Uruchomienie AplikacjiUstaw zmienną środowiskową (dozwala na tryb deweloperski) i uruchom aplikację:Bash# Ustawienie trybu deweloperskiego.

# Dla Windows:
$env:FLASK_ENV="development"
# Dla Linux/macOS:
export FLASK_ENV=development

# Uruchomienie serwera
flask run
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:5000/🗺️ Struktura Aplikacji i Nawigacja

Aplikacja jest zaprojektowana tak, aby nawigacja była intuicyjna:1. 
Dashboard (Główna)URL: http://127.0.0.1:5000/ - Centralna strona startowa GUI, która umożliwia przejście do głównych sekcji: Zadania i Użytkownicy.

2. Interfejs GUI (HTML)Pełny CRUD dla zadań i użytkowników dostępny przez widoki renderowane w HTML.

SekcjaFunkcjaURLZadaniaLista 
(Read All)/gui/tasksZadaniaDodaj 
(Create)/gui/tasks/newUżytkownicyLista 
(Read All)/gui/usersUżytkownicyDodaj 
(Create)/gui/users/new3. REST API (JSON)
Endpointy dla klientów zewnętrznych do zarządzania danymi za pomocą JSON.

ZasóbMetodaURLZadaniaGET/api/tasksZadaniaPOST/api/tasksUżytkownicyGET/api/usersUżytkownicyGET/api/users/<id>DokumentacjaGET/api-docs🧑‍💻 AutorCyber4rabbitGitHub ProfileLink do Repozytorium⚖️ LicencjaTen projekt jest udostępniony na licencji MIT.
