from initialize import create_app
from controllers.controllers import bp as bp

app = create_app()
app.register_blueprint(bp)