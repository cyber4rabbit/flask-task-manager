import pytest
from app import create_app
from app.models import db, User, Task


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        test_user = User(username="testuser", email="test@example.com")
        db.session.add(test_user)
        db.session.commit()

        yield app.test_client()

        db.drop_all()

def test_create_task(client):
    """Testuje dodawanie nowego zadania (POST /tasks)"""
    response = client.post('/tasks', json={
        'title': 'Testowe zadanie',
        'user_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Testowe zadanie'
    assert data['is_completed'] == False


def test_get_all_tasks(client):
    """Testuje pobieranie listy zadań (GET /tasks)"""
    client.post('/tasks', json={'title': 'Task 1', 'user_id': 1})
    client.post('/tasks', json={'title': 'Task 2', 'user_id': 1})

    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2


def test_update_task(client):
    """Testuje aktualizację zadania (PUT /tasks/<id>)"""
    create_res = client.post('/tasks', json={'title': 'Do update', 'user_id': 1})
    task_id = create_res.get_json()['id']
    update_res = client.put(f'/tasks/{task_id}', json={'is_completed': True})
    assert update_res.status_code == 200
    data = update_res.get_json()
    assert data['is_completed'] == True
    assert data['title'] == 'Do update'


def test_delete_task(client):
    """Testuje usunięcie zadania (DELETE /tasks/<id>)"""
    create_res = client.post('/tasks', json={'title': 'Do delete', 'user_id': 1})
    task_id = create_res.get_json()['id']

    delete_res = client.delete(f'/tasks/{task_id}')
    assert delete_res.status_code == 204

    get_res = client.get(f'/tasks/{task_id}')
    assert get_res.status_code == 404