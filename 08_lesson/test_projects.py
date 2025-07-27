import pytest
from api_client import YougileAPI
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("YOUGILE_BASE_URL")
token = os.getenv("YOUGILE_API_TOKEN")


@pytest.fixture(scope="module")
def api():
    return YougileAPI(base_url, token)


@pytest.fixture()
def created_project(api):
    response = api.create_project("Проекты для теста")
    assert response.status_code == 201
    return response.json()


def test_post_project_positive(api):
    response = api.create_project("Создать")
    print(response)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_post_project_negative_missing_title(api):
    response = api.create_project("")
    assert response.status_code in (400, 422)


def test_put_project_positive(api, created_project):
    project_id = created_project["id"]
    new_users = {"8a0b723e-0f0d-4348-b717-31bfec8380b2": "admin"}
    response = api.update_project(project_id, title="Обновленный проект",
                                  users=new_users)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_put_project_negative_invalid_id(api):
    project_id = 123
    new_users = {"8a0b723e-0f0d-4348-b717-31bfec8380b2": "admin"}
    response = api.update_project(project_id, title="Обновленный проект",
                                  users=new_users)
    assert response.status_code == 404


def test_get_project_positive(api, created_project):
    project_id = created_project["id"]
    response = api.get_project(project_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_get_project_negative_invalid_id(api):
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(invalid_id)
    assert response.status_code == 404
