from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import EmailField
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])

