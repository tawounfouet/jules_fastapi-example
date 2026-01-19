from app.blog import services, schemas
from app.users import services as user_services
from app.users import schemas as user_schemas

def test_create_post(db):
    user_in = user_schemas.UserCreate(email="author@example.com", password="password")
    user = user_services.create_user(db, user_in)

    post_in = schemas.PostCreate(title="Test Post", content="Content")
    post = services.create_post(db, post_in, user.id)

    assert post.title == "Test Post"
    assert post.owner_id == user.id

def test_get_posts(db):
    user_in = user_schemas.UserCreate(email="author@example.com", password="password")
    user = user_services.create_user(db, user_in)

    services.create_post(db, schemas.PostCreate(title="Post 1", content="C1"), user.id)
    services.create_post(db, schemas.PostCreate(title="Post 2", content="C2"), user.id)

    posts = services.get_posts(db)
    assert len(posts) == 2
