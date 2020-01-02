from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateTicketForm(FlaskForm):
    priority_choices = [(0, 'LOW'), (1, 'MEDIUM'), (2, 'HIGH'), (3, 'CRITICAL')]
    title = StringField('Title', validators=[DataRequired()])
    priority = SelectField(label='Priority', choices=priority_choices)
    project = SelectField(label='Project', choices=[])
    ticket_contents = TextAreaField(label='Ticket Contents', validators=[DataRequired()])
    assigned = SelectField(label='Assignee', choices=[])
    submit = SubmitField('Request Password Reset')
