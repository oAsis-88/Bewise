from flask import jsonify, request
from flask_restx import Resource

from backend.service.questions_service import service_get_questions_by_num


class ControllerQuestions(Resource):

    def post(self):
        form = request.json  # {"questions_num": integer}
        num = form.get("questions_num")

        if not isinstance(num, int):
            return jsonify({'status': 'error', 'description': f"Вы передали {num}, а должны были число"})

        response = service_get_questions_by_num(int(num))
        return jsonify(response)
