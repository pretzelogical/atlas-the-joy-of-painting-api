""" DB connection """
import mysql.connector
import json

class TJOPDatabase:

    def connect(self, host='localhost', port='5000') -> None:
        self.__db = mysql.connector.connect(
            host=host,
            port=port,
            database='joy_of_painting',
            user='jop_user',
            password='bobross'
        )


    def build_query(self, query: dict) -> str:
        query_str = (
            "SELECT episode.air_date, episode.episode, episode.season, "
            "painting.name, painting.colors, painting.subject "
            "FROM episode "
            "JOIN painting ON episode.painting_index = painting.index "
            "WHERE "
        )
        condition = ""
        if query["match"] == "all":
            condition = 'AND'
        else:
            condition = 'OR'
            # If loosely match then use JSON_OVERLAPS
            if query.get('colors'):
                query_str += (
                    "( JSON_OVERLAPS(painting.colors, "
                    f"'{json.dumps(query['colors'])}') "
                )

            if not query.get('subject'):
                query_str += ') '
            else:
                if query.get('colors'):
                    query_str += 'AND '
                else:
                    query_str += '( '
                query_str += (
                    "JSON_OVERLAPS(painting.subject, "
                    f"'{json.dumps(query['subject'])}') ) "
                )


        # query_str += "( "

        # for col in query['colors']:
        #     query_str += (
        #         f"JSON_CONTAINS(painting.colors, )"
        #    )
        query_str += ';'
        return query_str
