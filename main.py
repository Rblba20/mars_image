from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/_')
def _():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_ = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                  "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promotion_)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    '<img img_width = 20 src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">' 
                    <h5>Вот она какая, красная планета.</h5>
                    </body> </html> '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
