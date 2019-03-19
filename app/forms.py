from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField,SelectField,IntegerField,FileField
from wtforms.validators import InputRequired


class SignUpForm(FlaskForm):
	fname = StringField("First Name", validators = [InputRequired()])
	lname= StringField("Last Name", validators = [InputRequired()])
	age = IntegerField(validators=[InputRequired()])
	biography = TextAreaField()
	sex =  SelectField("Sex", choices=[('Male',"male"),("Female","female")])