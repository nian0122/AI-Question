from flask import Blueprint,render_template,jsonify,request,redirect,url_for,session
from flask_mail import Message
from exts import mail,db
import string
import random
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('pc',__name__,url_prefix='/')

