from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from authlib.integrations.flask_client import OAuth

bcrypt = Bcrypt()
mail = Mail()
jwt = JWTManager()
oauth = OAuth()


