from extensions import db


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(11))
    books = db.relationship('Book',backref='author')
    def __repr__(self):
        return "<Author id:%s name:%s>" % (self.id, self.name)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))
    def __repr__(self):
        return "<Book id:%s name:%s author_id:%s>" % (self.id, self.name, self.author_id)