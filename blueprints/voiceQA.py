from flask import (request, 
                   render_template,
                   Blueprint)
from decorators import login_required
import os
import subprocess

from models import Ai_QuestionModel,Ai_AnswerModel
from exts import db

import VQA
import SparkApi
from to_word_helper import stt_api_get_result


bp = Blueprint('voiceQA', __name__,url_prefix="/record")

class SharedData:
    filename = None
    question = None


@bp.route('/')
def index():
    return render_template('index_1.html')


@bp.route('/save_recording', methods=['GET','POST'])
@login_required
def save_recording():
    if request.method == 'GET':
        return render_template("index_1.html")
    else:
        recording = request.data

        # 生成不重复的文件名
        i = 1
        while os.path.exists(f'recording/recording{i}.wav'):
            i += 1
        filename = f'recording/recording{i}.wav'

        # 保存录音文件
        with open(filename, 'wb') as f:
            f.write(recording)

        # 使用ffmpeg将录音文件转换为mp3格式
        subprocess.run(['E:\\ffmpeg\\bin\\ffmpeg', '-i', filename, '-ar', '16000', '-ac', '1', '-ab', '16k',
                        f'recording/recording{i}.mp3'])
        filename = './recording/' + f'recording{i}.mp3'
        SharedData.filename = filename
        # stt_api_get_result('5f39ccd8', 'f6d0d54675341a4dc0404aa640afc3e7', 'ZWUxMjhhM2VkNzk1MzI5N2FhYzliODZk', filename)
        # return redirect(url_for('test_input', filename=filename))
        return "success!"


@bp.route("/test_input")
def test_input():
    filename = SharedData.filename
    # filename = './recording/recording3.mp3'
    # filename = request.args.get('filename')
    # stt_api_get_result('5f39ccd8', 'f6d0d54675341a4dc0404aa640afc3e7', 'ZWUxMjhhM2VkNzk1MzI5N2FhYzliODZk', filename)
    stt_api_get_result('5f39ccd8', 'f6d0d54675341a4dc0404aa640afc3e7', 'ZWUxMjhhM2VkNzk1MzI5N2FhYzliODZk', filename)
    with open('./static/data.txt', 'r') as f:
        text = f.readlines()
    result = ''.join(text)
    question = Ai_QuestionModel(text = result)
    db.session.add(question)
    db.session.commit()
    SharedData.question = result  # 储存问题
    return render_template("home.html", result=result)


@bp.route("/test_input/test_output")
def process_data():
    data = SharedData.question
    question = VQA.checklen(VQA.getText("user", data))
    SparkApi.answer = ""
    SparkApi.main(VQA.appid, VQA.api_key, VQA.api_secret, VQA.Spark_url, VQA.domain, question)
    text = SparkApi.get_ans()
    question = Ai_AnswerModel(text = text)
    db.session.add(question)
    db.session.commit()
    return render_template("home.html", result=SparkApi.get_ans())
    # return SparkApi.get_ans()
