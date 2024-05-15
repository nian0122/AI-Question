from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)


class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="questions")


class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # ���
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # ��ϵ
    question = db.relationship(QuestionModel, backref=db.backref("answers", order_by=create_time.desc()))
    author = db.relationship(UserModel, backref="answers")
    
class PictureModel(db.Model):
    __tablename__ = "picture"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name =  db.Column(db.String(100), nullable=False)
    data = db.Column(db.VARCHAR(100),nullable=False)

class TmcModel(db.Model):
    __tablename__ = 'tmc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    othername = db.Column(db.Text, nullable=False)
    englishname = db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    produce = db.Column(db.Text, nullable=False)
    shap = db.Column(db.Text, nullable=False)
    stc = db.Column(db.Text, nullable=False)
    effect = db.Column(db.Text, nullable=False)
    application = db.Column(db.Text, nullable=False)
    study = db.Column(db.Text, nullable=False)
    composition = db.Column(db.Text, nullable=False)
    taboo = db.Column(db.Text, nullable=False)
    formula = db.Column(db.Text, nullable=False)
    
    picture_id = db.Column(db.Integer, db.ForeignKey("picture.id"))
    picture = db.relationship(PictureModel, backref="Tmcs")

class EeeModel(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    picture = db.Column(db.String(200))
    
    
class Ai_QuestionModel(db.Model):
    __tablename__ = "ai_question"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    text = db.Column(db.Text , nullable = False)
    
class Ai_AnswerModel(db.Model):
    __tablename__ = "ai_answer"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    text = db.Column(db.Text , nullable = False)
    
    
