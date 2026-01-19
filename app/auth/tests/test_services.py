from app.auth import services
from app.users import services as user_services
from app.users import schemas as user_schemas

def test_authenticate_user(db):
    user_in = user_schemas.UserCreate(email="test@example.com", password="password")
    user_services.create_user(db, user_in)

    auth_user = services.authenticate_user(db, "test@example.com", "password")
    assert auth_user
    assert auth_user.email == "test@example.com"

    assert not services.authenticate_user(db, "test@example.com", "wrong")
    assert not services.authenticate_user(db, "wrong@example.com", "password")
