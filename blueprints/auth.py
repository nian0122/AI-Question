from flask import Blueprint,render_template,jsonify,request,redirect,url_for,session
from flask_mail import Message
from exts import mail,db
import string
import random
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__,url_prefix="/auth")

@bp.route("/login",methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                session["user_id"] = user.id
                return redirect("/")
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))
        
@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
        
# GET：从服务器上获取数据
# POST：将客户端的数据提交给服务器
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register_1.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证：flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    message = Message(subject="验证码",recipients=[email],body=f"您的验证码是:{captcha}")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code":200,"message":"","date":None})

@bp.route("/mail/text")
def mail_text():
    message = Message(subject="测试",recipients=["972139363@qq.com"],body="酸萝卜别吃")
    mail.send(message)
    return "测试成功"