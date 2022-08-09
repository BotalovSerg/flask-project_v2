from flask import Flask, render_template
from game_live import GameOfLife

app = Flask(__name__)


@app.route('/')
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


if __name__ == '__main__':
    app.run(debug=True)
