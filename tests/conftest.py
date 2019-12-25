import pytest

from app import create_app, db
from app.models import User, Permission, Project


@pytest.fixture(scope='module')
def test_client() -> None:
    """ Define Test Variables and initialize app"""
    app = create_app(config_name="testing")
    testing_client = app.test_client()
    app_context = app.app_context()
    app_context.push()

    yield testing_client

    app_context.pop()


@pytest.fixture(scope='module')
def init_database() -> None:
    db.create_all()

    users = [
        User(username='test_user_1',
             email='test_user_1@test_user_email.com',
             job_title='test_job_title_1'),
        User(username='test_user_2',
             email='test_user_2@test_user_email.com',
             job_title='test_job_title_2'),
    ]

    for user in users:
        db.session.add(user)

    permissions = [
        Permission(permission_name='administrator',
                   created_by=users[0].id),
        Permission(permission_name='developer',
                   created_by=users[1].id),
    ]

    for permission in permissions:
        db.session.add(permission)

    projects = [
        Project(project_name='test_project_1',
                created_by=users[0].id),
        Project(project_name='test_project_2',
                created_by=users[1].id),
    ]

    for project in projects:
        db.session.add(project)

    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()
