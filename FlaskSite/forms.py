from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField , SubmitField , MultipleFileField , SelectField,HiddenField ,Form ,FormField,IntegerField,BooleanField ,PasswordField
from wtforms.validators import DataRequired , Length , URL, Optional,Email, EqualTo


class Text(Form):
    Head = StringField(   validators=[Length(max=200)])
    TextData = TextAreaField("Text")
    Comment = StringField("comment",validators=[Length(max=200)])

class Pics(Form):
    Head = StringField(validators=[Length(max=200)])
    Pic = MultipleFileField("Pics")
    Comment = StringField("comment",validators=[Length(max=200)])

class Links(Form):
    Head = StringField(validators=[Length(max=200)])
    Url = StringField("Link",validators=[ Optional(), URL()])
    Comment = StringField("comment",validators=[Length(max=200)])



class InfoF(FlaskForm): 
    Text = FormField(Text)
    Pic = FormField(Pics)
    Link = FormField(Links)
    Key = StringField("Key",validators=[Length(max=200),DataRequired()])
    Submit = SubmitField()

class NewTopic(FlaskForm):
    Name = StringField("TopicName",validators=[Length(max=40)])
    
    Submit = SubmitField()



class LoginForm(FlaskForm):
    UserName = StringField('Email',
                        validators=[DataRequired()])
    Pass = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    UserName = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    Password = PasswordField("Password", validators=[DataRequired()])
    RepeatPassword = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')
