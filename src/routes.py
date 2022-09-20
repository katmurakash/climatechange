from flask import render_template, Blueprint
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/news')
def about():
    return render_template('news.html')


@main.route("/aboutme")
def aboutme():
    return render_template('e.html')