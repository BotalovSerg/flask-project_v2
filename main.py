from flask import Flask, render_template, request, url_for, redirect
from game_live import GameOfLife
from config import Config
from project.forms import MessageForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    new_live = GameOfLife()
    if new_live.counter > 0:
        new_live.form_new_generation()
    new_live.counter += 1
    return render_template('live.html', new_live=new_live)


@app.route('/message/', methods=['get', 'post'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print("\nData received. Now redirecting...")
        return redirect(url_for('message'))

    return render_template('message.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
