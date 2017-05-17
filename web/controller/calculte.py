from flask import Blueprint

calculate_blueprint = Blueprint('calculate', __name__,url_prefix='/calculate')

index = Blueprint('index', __name__,url_prefix='/index')

@calculate_blueprint.route('/')
def home():
    return 'calculate'
    # return render_template('')


@index.route('/')
def home():
    return 'index'
    # return render_template('')