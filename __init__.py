# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# from app import models, routes

# def seed_data():
#     from app import seeds 
#     seeds.seed_data()

# if __name__ == '__main__':
#     seed_data() 
#     app.run(port=5555)
