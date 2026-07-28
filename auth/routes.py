from flask_bcrypt import Bcrypt

flask_bcrypt = Bcrypt()

print(flask_bcrypt.generate_password_hash('Admin123').decode('utf-8'))