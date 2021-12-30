from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateTodoForm(FlaskForm):
    todo = TextAreaField(validators=[DataRequired(), Length(1,80)])
    date = DateField(validators=[DataRequired()])
    time = TimeField(validators=[DataRequired()])
    submit = SubmitField(label='Create')