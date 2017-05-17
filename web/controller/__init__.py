from web import app
from web.controller.calculte import calculate_blueprint,index

app.register_blueprint(calculate_blueprint)
app.register_blueprint(index)