# 1. Menedżer Zadań (Flask + SQLAlchemy + Marshmallow)

Flask-task-manager to aplikacja webowa zbudowana na frameworku Flask, służąca do zarządzania zadaniami i użytkownikami. 
Projekt implementuje pełny CRUD (Create, Read, Update, Delete) w dwóch warstwach: jako REST API (JSON) dla klientów zewnętrznych oraz jako Przyjazny Interfejs GUI dla użytkowników końcowych.
Jest to projekt demonstracyjny mający na celu zaprezentowanie architektury aplikacji Flask opartej na wzorcu Application Factory i Blueprintach, z wykorzystaniem SQLAlchemy jako ORM. 

Framework: Flask
Baza Danych SQLAlchemy
Serializacja: Marshmallow
Formularze: Flask-WTF
Struktura: Blueprints & Application Factory
Python 3.12

# 2. Konfiguracja Środowiska Wirtualnego (VENV)

Utwórz środowisko wirtualne:

python -m venv .venv

Aktywuj środowisko wirtualne:

Dla Windows (CMD/PowerShell):
.venv\Scripts\activate
Dla macOS/Linux:
source .venv/bin/activate

# 3. Instalacja Zależności

Zainstaluj wymagane pakiety Pythona:
pip install -r requirements.txt

# 4. Uruchomienie Aplikacji

Ustaw zmienną środowiskową i uruchom aplikację:

Ustawienie trybu deweloperskiego.

Dla Windows:

$env:FLASK_ENV="development"

Dla Linux/macOS:

export FLASK_ENV=development

Uruchomienie serwera:

Należy uruchomić run.py

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:5000/

Aplikacja jest zaprojektowana tak, aby nawigacja była intuicyjna:

Dashboard (Główna)URL: http://127.0.0.1:5000/ - Centralna strona startowa GUI, która umożliwia przejście do głównych sekcji.

SekcjaFunkcjaURLZadaniaLista 

(Read All)/gui/tasksZadaniaDodaj 

(Create)/gui/tasks/newUżytkownicyLista 

(Read All)/gui/usersUżytkownicyDodaj 

(Create)/gui/users/new3. REST API (JSON)

Endpointy dla klientów zewnętrznych do zarządzania danymi za pomocą JSON.

