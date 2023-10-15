from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Quantity", validators=[DataRequired()])
    completed = SelectField("Diet", choices=[("Veg", "Veg"), ("Not Veg","Not Veg")], validators = [DataRequired()])
    submit = SubmitField("Add Todo")