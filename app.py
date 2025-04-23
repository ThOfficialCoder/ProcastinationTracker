from flask import Flask, render_template, redirect, url_for, request, flash
from wtforms import Form, BooleanField, StringField, validators
from models import User
from database import db_session, init_db

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/default")
def default():
    return render_template("layout.html")

class ProcastinationForm(Form):
    reason = StringField('Reason', validators=[validators.input_required()])
    source = StringField('Source', validators=[validators.input_required()])
    feeling = StringField('Feeling', validators=[validators.input_required()])

@app.route("/form", methods=['GET', 'POST'])
def form():
    form = ProcastinationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.reason.data, form.source.data,
                    form.feeling.data)
        db_session.add(user)
        db_session.commit()
        flash('Great. Would you like a 5 min focus session?')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)

@app.route("/view")
def view():
    users = db_session.query(User).all()
    return render_template('view.html', users=users)

if __name__ == "__main__":
    init_db()
    app.run(debug=False)