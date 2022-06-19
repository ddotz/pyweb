from flask import Flask, render_template as rt, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/book'
db = SQLAlchemy(app)
app.secret_key = 'zhang'


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm = PasswordField('确认密码', validators=[DataRequired(), EqualTo("password", "密码不一致")])
    submit = SubmitField('提交')


class Role(db.Model):
    __tablename__ = 'demo'
    id = db.Column(db.Integer,primary_key=True)



class LoginForm_2(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm = PasswordField('确认密码', validators=[DataRequired(), EqualTo("username", "密码不一致")])
    submit = SubmitField('提交')

@app.route('/',methods=['GET','POST'])
def welcome():
    return "hello, flask"
@app.route('/zhang/<int:name>')
def with_param(**n):
    return "name = %s" % n.get('name')
@app.route('/index',methods=['GET','post'])
def index():
    # if request.method == 'POST':
    #     u = request.form.get('username')
    #     p = request.form.get('password')
    #     if not all([u,p]):
    #         flash('信息不完整')
    login_form = LoginForm()
    login_form_2 = LoginForm_2()
    if request.method == 'POST':
        if login_form_2.validate_on_submit():
            return "success"
        else:
            flash('信息有误')

    return rt('index.html',form=login_form)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == "POST":
        file = request.files.get('image')
        file.save(f"./image/{file.filename}")
    return rt("upload.html")

@app.route('/handlefile',methods=['GET','POST'])
def handle_file():
    data = request.files['image']
    print(data)
    return rt("upload.html")

if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    app.run(host='0.0.0.0',port=5000)