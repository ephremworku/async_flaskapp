
# main.py
from initialize import create_app
from controllers.controllers import bp as bp
from asgiref.wsgi import WsgiToAsgi

app = create_app()
app.register_blueprint(bp)

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5000, debug=True)
