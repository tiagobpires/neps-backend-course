from datetime import datetime

from factory import db
from sqlalchemy import select
from main import app
from models import User, Post, Role

with app.app_context():

    try:
        print("Limpando a base de dados...")

        # A ordem de exclusão é importante por causa das chaves estrangeiras (foreign keys)
        # 1. Excluir Posts (que dependem de User)
        db.session.query(Post).delete()
        print(" - Tabela 'Post' limpa.")

        # 2. Excluir Users (que dependem de Role)
        db.session.query(User).delete()
        print(" - Tabela 'User' limpa.")

        # 3. Excluir Roles
        db.session.query(Role).delete()
        print(" - Tabela 'Role' limpa.")

        db.session.commit()
        print("Base de dados limpa com sucesso!")
    except Exception as e:
        db.session.rollback()
        print(f"Ocorreu um erro ao limpar a base de dados: {e}")
