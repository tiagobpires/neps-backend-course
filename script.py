from datetime import datetime

from factory import db
from sqlalchemy import select
from main import app
from models import User, Post

with app.app_context():

    # Carrega usuário
    posts = db.session.scalars(
        select(Post).order_by(Post.created_at.desc()),
    ).all()

    posts_pagination = Post.query.paginate(1, 5)

    # Percorre postagens e imprime seus textos
    print(posts)
