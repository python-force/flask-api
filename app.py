from flask import Flask, render_template

import config
import models
from resources.todos import todos_api
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

app = Flask(__name__)
app.secret_key = 'sd7sa76v8*&%7asf7656#dsjksadjwaalcma.caskascjhavs'
app.register_blueprint(todos_api)

limiter = Limiter(app, global_limits=[config.DEFAULT_RATE], key_func=get_ipaddr)
limiter.limit("40/day")(todos_api)
limiter.limit(config.DEFAULT_RATE, per_method=True, methods=['post', 'put', 'delete'])(todos_api)


@app.route('/')
def my_todos():
    return render_template('index.html')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
