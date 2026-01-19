from app.comments import services, schemas
from app.blog import services as blog_services
from app.blog import schemas as blog_schemas
from app.users import services as user_services
from app.users import schemas as user_schemas

def test_create_comment(db):
    user_in = user_schemas.UserCreate(email="author@example.com", password="password")
    user = user_services.create_user(db, user_in)

    post_in = blog_schemas.PostCreate(title="Test Post", content="Content")
    post = blog_services.create_post(db, post_in, user.id)

    comment_in = schemas.CommentCreate(content="Nice post!", post_id=post.id)
    comment = services.create_comment(db, comment_in, user.id)

    assert comment.content == "Nice post!"
    assert comment.post_id == post.id
    assert comment.owner_id == user.id

def test_get_comments(db):
    user_in = user_schemas.UserCreate(email="author@example.com", password="password")
    user = user_services.create_user(db, user_in)

    post_in = blog_schemas.PostCreate(title="Test Post", content="Content")
    post = blog_services.create_post(db, post_in, user.id)

    services.create_comment(db, schemas.CommentCreate(content="C1", post_id=post.id), user.id)
    services.create_comment(db, schemas.CommentCreate(content="C2", post_id=post.id), user.id)

    comments = services.get_comments_by_post(db, post.id)
    assert len(comments) == 2
