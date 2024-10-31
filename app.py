from flask import Flask
from database import db
from models.user import User
from routes.user import user_routes
from routes.meals import meal_routes
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.register_blueprint(user_routes)
app.register_blueprint(meal_routes)

uri = os.getenv('DB_URL')
secret_key = os.getenv('SECRET_KEY')

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = uri

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


# View de autenticação/login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
