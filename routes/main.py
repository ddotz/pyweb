from flask import Blueprint, render_template as rt, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from tools import img
# from flask_uploads import UploadSet, IMAGES
from extensions import db

main = Blueprint('main', __name__)
# photos = UploadSet('photos', IMAGES)

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm = PasswordField('确认密码', validators=[DataRequired(), EqualTo("password", "密码不一致")])
    submit = SubmitField('提交')


@main.route('/',methods=['GET','POST'])
def index():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            return "success"
        else:
            flash('信息有误')
    return rt('index.html', form=login_form)


@main.route('/zhang/<int:name>')
def with_param(**n):
    return "name = %s" % n.get('name')


@main.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == "POST":
        file = request.files.get('image')
        file.save("./image/back.jpg")
        img.compos('./image/back.jpg', './image/fore_1.jpg', './image/fore_2.jpg')
        return rt("image_res.html")
    return rt("upload.html")
    # if request.method == "POST":
    #     file = request.files.get('image')
    #     photos.save(file, 'test.jpg')
    #     file.save("../image/back.jpg")
    #     img.compos('../image/back.jpg', '../image/fore_1.jpg', '../image/fore_2.jpg')
    #     return rt("image_res.html")
    # return rt("upload.html")

