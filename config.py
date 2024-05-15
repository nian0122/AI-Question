# ��������
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3048586944@qq.com"
MAIL_PASSWORD = "pyzxzuzvvuisddgj"
MAIL_DEFAULT_SENDER = "3048586944@qq.com"

## 

SECRET_KEY = "asdfasdfjasdfjasd;lf"

# ���ݿ��������Ϣ
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI