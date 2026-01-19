from users import services, schemas

def test_create_user(db):
    user_in = schemas.UserCreate(email="test@example.com", password="password")
    user = services.create_user(db, user_in)
    assert user.email == "test@example.com"
    assert hasattr(user, "hashed_password")

def test_get_user(db):
    user_in = schemas.UserCreate(email="test@example.com", password="password")
    user = services.create_user(db, user_in)
    fetched = services.get_user_by_email(db, "test@example.com")
    assert fetched.id == user.id
