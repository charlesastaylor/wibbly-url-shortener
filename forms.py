from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class NewRuleForm(FlaskForm):
    key = StringField('key')
    url = StringField('url', validators=[DataRequired(), URL()])
    submit = SubmitField('Go!')