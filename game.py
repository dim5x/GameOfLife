from flask import Flask, render_template, request

app = Flask(__name__)

from game_of_life import GameOfLife

g = GameOfLife


@app.route('/', methods=['post', 'get'])
def index():
    global g
    if request.method == 'POST':
        height = int(request.form.get('height'))
        width = int(request.form.get('width'))
        g = GameOfLife(width, height)
    else:
        g = GameOfLife(20, 20)
        g.count = 0
    return render_template('index.html')


@app.route('/live')
def live():
    g.form_new_generation()
    return render_template('live.html', g=g)


if __name__ == '__main__':
    app.run(debug=True)
