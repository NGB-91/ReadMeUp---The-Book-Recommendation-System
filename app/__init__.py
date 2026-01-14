from flask import Flask

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )

    from app.main.routes import main
    app.register_blueprint(main)

    return app
