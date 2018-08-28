
#
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf import FlaskForm


# Login Form
class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired,Length(max=10)])
    password = PasswordField('Password', validators=[DataRequired,Length(max=10)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


# Register Form
class RegisterForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired, Length(max=10)])
    password = PasswordField('Password', validators=[DataRequired, Length(max=10)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired, EqualTo('password')])
    submit = SubmitField('Sign up')
