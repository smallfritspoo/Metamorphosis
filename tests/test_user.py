from app.models import User


def test_users_created(test_client, init_database):
    users = User.query.all()

    for index, value in enumerate(users, start=1):
        assert value.id == index
        assert value.username == f"test_user_{index}"
        assert value.email == f"test_user_{index}@test_user_email.com"
        assert value.job_title == f"test_job_title_{index}"
