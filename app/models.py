import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db, login
from typing import Optional
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from flask_ckeditor import CKEditor
from datetime import datetime, timezone

class User(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    username: so.Mapped[str] = so.mapped_column(sa.String(64), 
                                                index=True,
                                                unique=True,
                                                )
    
    email: so.Mapped[str] = so.mapped_column(sa.String(120), 
                                             index=True, 
                                             unique=True,
                                             )
    
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, passw):
        self.password_hash = generate_password_hash(passw)
    
    def check_password(self, passw):
        return check_password_hash(self.password_hash, passw)
    
class Category(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(64))

    # cat_id = so.Mapped[int] = so.mapped_column(sa.ForeignKey(Category.id), index=True)
    # cat_desc = so.Mapped[Category] = so.relationship(back_populates='description')

    def __repr__(self):
        return '<Category {}>'.format(self.name)
    

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(64))
    body: so.Mapped[str] = so.mapped_column(sa.String(200))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    # categories: so.WriteOnlyMapped['Category'] = so.relationship(back_populates='description')

    def __repr__(self):
        return '<Post {}>'.format(self.name)
    

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
