# db.py module

import psycopg2 as psql

class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database="lesson_9",
            user="postgres",
            password="sam2303",
            host="localhost",
            port="5432"
        )
        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"
        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM users_2 WHERE user_id = {user_id}"
        check_user = await Database.connect(query, query_type="select")
        if len(check_user) == 1:
            print(">>>>>>>>>>>>>>>>>>>>", check_user)
            return True
        return False
