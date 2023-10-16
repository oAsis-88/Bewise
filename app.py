import os

from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api

from backend.controller.questions_controller import ControllerQuestions

dotenv_path = os.path.join(os.path.abspath(os.curdir), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

api.add_resource(ControllerQuestions, f"/questions", methods=['POST'], endpoint='questions')

if __name__ == '__main__':
    try:
        app.run(debug=True, host=os.getenv("UI_HOST"), port=os.getenv("UI_PORT"), use_reloader=False)
    except (KeyboardInterrupt, SystemExit):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! App stopped !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
