""" DB connection """
import mysql.connector
import json


class TJOPDatabase:

    def connect(self, host='localhost', port=5000) -> None:
        if hasattr(self, '__db'):
            return
        self.__db = mysql.connector.connect(
            host=host,
            port=port,
            database='joy_of_painting',
            user='jop_user',
            password='bobross'
        )

    def build_get_query_JSON_str(self, query: dict) -> str:
        """ Build part of query that select JSON values """
        json_str = ""
        if not (query.get('colors') or query.get('subject')):
            return json_str
        if query["match"] == "all":
            # If strict match then use JSON_CONTAINS and AND conditionals
            json_str += '( '

            for col in query.get('colors', []):
                json_str += (
                    f"JSON_CONTAINS(painting.colors, '\"{col}\"', '$') AND "
                )

            for sub in query.get('subject', []):
                json_str += (
                    f"JSON_CONTAINS(painting.subject, '\"{sub}\"', '$') AND "
                )
            json_str = json_str[:-4]
            json_str += ') '
        else:
            # If loosely match then use JSON_OVERLAPS
            if query.get('colors'):
                json_str += (
                    "( JSON_OVERLAPS(painting.colors, "
                    f"'{json.dumps(query['colors'])}') "
                )

            if not query.get('subject'):
                json_str += ') '
            else:
                if query.get('colors'):
                    json_str += 'OR '
                else:
                    json_str += '( '
                json_str += (
                    "JSON_OVERLAPS(painting.subject, "
                    f"'{json.dumps(query['subject'])}') ) "
                )
        return json_str

    def build_get_query_date_str(self, query: dict) -> str:
        """ Build year and month part of query """
        date_str = ""
        if not query.get('month'):
            return date_str

        date_str += '( '
        for date in query['month']:
            date_str += (
                f"( EXTRACT(YEAR FROM episode.air_date) = {date[:4]} "
                f"AND EXTRACT(MONTH FROM episode.air_date) = {date[-2:]} ) OR "  # noqa
            )

        date_str = date_str[:-3]
        date_str += ') '
        return date_str

    def build_get_query_str(self, query: dict) -> str:
        """ Build query from dict """
        # TODO: Add path for empty {} that fetches all
        # TODO: Add option for user defined query
        query_str = (
            "SELECT episode.air_date, episode.episode, episode.season, "
            "episode.youtube_src, "
            "painting.name, painting.img_src "
            "FROM episode "
            "JOIN painting ON episode.painting_index = painting.index "
            "WHERE "
        )
        json_str = self.build_get_query_JSON_str(query)
        query_str += json_str
        if json_str != '' and query.get('month'):
            query_str += 'AND '
        date_str = self.build_get_query_date_str(query)
        query_str += date_str

        query_str += ';'
        return query_str

    def get(self, query: dict):
        if not self.__db:
            return {}
        query_str = self.build_get_query_str(query)
        cursor = self.__db.cursor(dictionary=True)
        print(query_str)
        cursor.execute(query_str)
        res = cursor.fetchall()
        cursor.close()
        return res

    def close(self):
        self.__db.close()
        del self.__db
