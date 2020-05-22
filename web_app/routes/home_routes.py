from flask import Blueprint , render_template

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    return render_template('predict_form.html')


@home_routes.route('/about')  
def about():
    return 'I am batman'