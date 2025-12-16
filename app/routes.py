
from flask import Blueprint, render_template, flash, redirect, url_for
from .models import db, Task, User
from .forms import TaskForm, UserForm

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    """Główna strona aplikacji i menu nawigacyjne (Dashboard)."""
    return render_template("dashboard.html")

@main.route("/api-docs")
def home():
    """Renderuje stronę z dokumentacją API (JSON)."""
    return render_template("index.html")

@main.route("/gui/tasks")
def task_list():
    """Wyświetla listę zadań w formie tabeli HTML."""
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

@main.route("/gui/tasks/new", methods=["GET", "POST"])
def task_create():
    """Wyświetla formularz dodawania zadania i obsługuje POST."""
    form = TaskForm()

    if form.validate_on_submit():
        if not User.query.get(form.user_id.data):
            flash('Użytkownik o podanym ID nie istnieje.', 'error')
            return render_template('task_form.html', title='Dodaj Zadanie', form=form)

        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            is_completed=form.is_completed.data,
            user_id=form.user_id.data
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Zadanie zostało pomyślnie dodane!', 'success')
        return redirect(url_for('main.task_list'))
    return render_template('task_form.html', title='Dodaj Zadanie', form=form)

@main.route("/gui/tasks/edit/<int:task_id>", methods=["GET", "POST"])
def task_edit(task_id):
    """Wyświetla formularz edycji zadania i obsługuje PUT (aktualizację)."""
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        if not User.query.get(form.user_id.data):
            flash('Użytkownik o podanym ID nie istnieje.', 'error')
            return render_template('task_form.html', title=f'Edytuj Zadanie {task.id}', form=form)

        form.populate_obj(task)
        db.session.commit()
        flash(f'Zadanie {task_id} zostało pomyślnie zaktualizowane!', 'success')
        return redirect(url_for('main.task_list'))

    return render_template('task_form.html', title=f'Edytuj Zadanie {task.id}', form=form)

@main.route("/gui/tasks/delete/<int:task_id>", methods=["POST"])
def task_delete_html(task_id):
    """Obsługuje usuwanie zadania przesłane z formularza (POST)."""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Zadanie {task_id} zostało pomyślnie usunięte!', 'success')
    return redirect(url_for('main.task_list'))


@main.route("/gui/users")
def user_list():
    """Wyświetla listę użytkowników w formie tabeli HTML."""
    users = User.query.all()
    return render_template('user_list.html', users=users)

@main.route("/add-user")
def add_user():
    """Tworzy testowego użytkownika, jeśli nie istnieje."""
    if not User.query.filter_by(username="admin").first():
        user = User(username="admin", email="admin@test.com")
        db.session.add(user)
        db.session.commit()
        return "Admin user created! ID: 1"
    return "Admin user already exists."


@main.route("/gui/users/new", methods=["GET", "POST"])
def user_create():
    """Wyświetla formularz dodawania użytkownika i obsługuje POST."""
    form = UserForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Użytkownik został pomyślnie dodany!', 'success')
        return redirect(url_for('main.user_list'))

    return render_template('user_form.html', title='Dodaj Użytkownika', form=form)

@main.route("/gui/users/edit/<int:user_id>", methods=["GET", "POST"])
def user_edit(user_id):
    """Wyświetla formularz edycji użytkownika i obsługuje PUT (aktualizację)."""
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash(f'Użytkownik {user_id} został pomyślnie zaktualizowany!', 'success')
        return redirect(url_for('main.user_list'))

    return render_template('user_form.html', title=f'Edytuj Użytkownika {user.id}', form=form)

@main.route("/gui/users/delete/<int:user_id>", methods=["POST"])
def user_delete_html(user_id):
    """Obsługuje usuwanie użytkownika. Uwaga: Może wymagać kaskadowego usuwania zadań w modelu Task!"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'Użytkownik {user_id} został pomyślnie usunięty!', 'success')
    return redirect(url_for('main.user_list'))