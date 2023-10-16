import requests as requests

from backend.repository.questions_repository import QuestionsRepository

questions_repository = QuestionsRepository()


def service_get_questions_by_num(num: int = 1) -> list:
    """ Получает кол-во questions по num  """
    url_question = lambda count: f"https://jservice.io/api/random?count={count}"
    questions = requests.get(url_question(count=num)).json()
    response = []

    for question in questions:
        res = questions_repository.db_add_questions(question)
        while res is None:
            question = requests.get(url_question(count=1)).json()[0]
            res = questions_repository.db_add_questions(question)
        response.append(res)
    return response
