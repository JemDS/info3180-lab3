from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config['MAIL_SERVER']="smtp.mailtrap.io"
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="4e52affca2e588"
app.config['MAIL_PASSWORD']="9ad110b78cfda0"
app.config['SECRET_KEY']="dsj200695"

mail = Mail(app)
from app import views