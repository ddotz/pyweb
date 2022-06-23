from flask import Blueprint,render_template, flash, request, redirect, url_for
from models.book import Author, Book
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from extensions import db

book = Blueprint('book',__name__,template_folder='../templates/book',static_folder='static/book')

class SearchForm(FlaskForm):
    author = StringField('作者',validators=(DataRequired(),))
    book = StringField('书名',validators=(DataRequired(),))
    submit = SubmitField('添加书籍')

@book.route('/',methods=['GET','POST'])
def index():
    searchForm = SearchForm()
    if searchForm.validate_on_submit():
        author_name = searchForm.author.data
        book_name = searchForm.book.data
        author_query = Author.query.filter(Author.name == author_name).first()
        #作者不存在，直接添加作者和书籍
        if not author_query:
            try:
                author = Author(name=author_name)
                #先添加作者，自动生成作者id
                db.session.add(author)
                db.session.commit()
                book = Book(name=book_name, author_id=author.id)
                db.session.add(book)
                db.session.commit()
                flash("作者和书籍添加成功")
            except Exception as e:
                print(e)
                flash('添加作者和书籍失败')
                db.session.rollbak()
        #作者存在，看对应书籍是否存在
        else:
            #对应书籍不存在，添加书籍
            if not Book.query.filter_by(name=book_name).first():
                try:
                    book = Book(name=book_name, author_id=author_query.id)
                    db.session.add(book)
                    db.session.commit()
                    flash("书籍添加成功")
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollbak()
            #对应书籍存在，提示‘书籍已存在’
            else:
                flash("书籍已存在")
    else:
        if request.method == "POST":
            flash("信息填写有误")
    authors = Author.query.all()
    return render_template("books.html", authors=authors, searchform=searchForm)

@book.route("/deletebook/<book_id>")
def deletebook(book_id):
    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            flash("书籍已删除")
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("删除书籍出错")
    else:
        flash("找不到对应书籍")
    return redirect(url_for("book.index"))

@book.route("/deletauthor/<author_id>")
def deleteauthor(author_id):
    author = Author.query.get(author_id)
    if author:
        try:
            Book.query.filter_by(author_id=author.id).delete()
            db.session.delete(author)
            db.session.commit()
            flash("作者及其书籍已删除")
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("删除作者及其书籍出错")
    else:
        flash("找不到对应作者")
    return redirect(url_for("book.index"))

