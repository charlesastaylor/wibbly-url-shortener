import random
import string

from flask import Flask, render_template, redirect, flash, url_for, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
from forms import NewRuleForm


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

def random_key(length=3):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewRuleForm()
    if form.validate_on_submit():
        key, url = form.key.data, form.url.data
        # Validate key
        if UrlRule.query.filter_by(key=key).first():
            flash(f'{request.host}/{key} already in use, please try again...')
            return redirect(url_for('index'))
        if ' ' in key:
            flash('No spaces in custom url! Try again...')
            return redirect(url_for('index'))
        # Create random key if one isnt supplied
        if not key:
            key = random_key()
            while UrlRule.query.filter_by(key=key).first():
                key = random_key()
        # Create new rule
        newrule = UrlRule(key=key, url=url)
        db.session.add(newrule)
        db.session.commit()
        flash(f'Success! {request.host}/{key} now redirects to {url[:37] + "..." if len(url) > 40 else url}')
    return render_template('index.html.j2', form=form)

@app.route('/<string:key>')
def redirecter(key):
    urlrule = UrlRule.query.filter_by(key=key).first()
    if not urlrule:
        flash(f'Unrecognized key: {key}')
        return redirect(url_for('index'))
    return redirect(urlrule.url)
    
from models import UrlRule
