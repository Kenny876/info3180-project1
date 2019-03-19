from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = "app/static/uploads"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


app.config.from_object(__name__)
from app import views