import psycopg2
import psycopg2.extras
import psycopg2.pool

from backend.db_postgres.pg_connection import postgreSQL_pool
from backend.meta_classes import SingletonMultithreadBaseClass


class QuestionsRepository(metaclass=SingletonMultithreadBaseClass):
    def db_get_question_by_questionId(self, question_id):
        query = """SELECT * FROM questions_info WHERE question_id = %s;"""

        connect = postgreSQL_pool.getconn()
        with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(query, (question_id, ))
            res = curs.fetchone()
            if res is not None:
                res = dict(res)
        connect.commit()
        postgreSQL_pool.putconn(connect)

        return res

    def db_get_all_questions(self) -> list | None:
        query = """SELECT * FROM questions_info;"""

        connect = postgreSQL_pool.getconn()
        with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(query)
            res = curs.fetchall()
            if res is not None:
                res = [dict(el) for el in res]
        connect.commit()
        postgreSQL_pool.putconn(connect)

        return res

    def db_add_questions(self, questions_info):
        question = self.db_get_question_by_questionId(questions_info.get("id"))
        if question is not None:
            return None

        query = """INSERT INTO questions_info 
        (question_id, question_text, question_answer, question_created_at, create_date, update_date)
        VALUES (%s, %s, %s, %s, now(), now()) RETURNING *;"""

        connect = postgreSQL_pool.getconn()
        with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(query, (
                questions_info.get("id"),
                questions_info.get("question"),
                questions_info.get("answer"),
                questions_info.get("created_at"),
            ))
            res = curs.fetchone()
            if res is not None:
                res = dict(res)
        connect.commit()
        postgreSQL_pool.putconn(connect)

        return res
