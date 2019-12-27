from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.models import User


class CreateTicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    priority =