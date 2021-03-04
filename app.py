import os
from flask import Flask
from flask_restful import Api

from resources.special_sum import SpecialSum

# Flask setup
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Flask Restful
api = Api(app)

api.add_resource(SpecialSum, '/sum')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
