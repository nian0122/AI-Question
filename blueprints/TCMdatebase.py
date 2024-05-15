from flask import Blueprint,render_template,request,redirect,g,url_for,send_file
from models import TmcModel
from exts import db
from .forms import QuestionForm,AnswerForm
from sqlalchemy import func

bp = Blueprint('databases', __name__,url_prefix="/data")

@bp.route('/')
def index():
    Tmc = TmcModel.query.order_by(TmcModel.id).all()
    return render_template("databases.html",Tmcs=Tmc)

@bp.route("/detail/<da_id>")
def da_detail(da_id):
    Tmc =  TmcModel.query.get(da_id)
    target = TmcModel.query.get(da_id)
    names = [Text.name for Text in TmcModel.query.all()]
    return render_template("detail_da.html",Tmc=Tmc, target=target, names=names)


@bp.route("/serach")
def serch():
    d = request.args.get('q')
    Tmcs = TmcModel.query.filter(func.lower(TmcModel.name).ilike(f"%{d.lower()}%")).all()
    return render_template('databases.html',Tmcs=Tmcs)
