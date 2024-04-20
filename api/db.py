""" DB connection """
import mysql.connector
from build_query import build_get_query_str


class TJOPDatabase:

    def connect(self, host='localhost', port=5000) -> None:
        """ Connect to the database """
        if hasattr(self, '__db'):
            return
        self.__db = mysql.connector.connect(
            host=host,
            port=port,
            database='joy_of_painting',
            user='jop_user',
            password='bobross'
        )

    def get(self, query: dict):
        """ Get the query from the database """
        if not self.__db:
            return {}
        query_str = build_get_query_str(query)
        cursor = self.__db.cursor(dictionary=True)
        cursor.execute(query_str)
        res = cursor.fetchall()
        cursor.close()
        return res

    def close(self):
        """ Close the database """
        self.__db.close()
        del self.__db
