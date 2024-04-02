""" DB connection """
import mysql.connector
import json

class TJOPDatabase:

    def connect(self, host='localhost', port='5000') -> None:
        if self.__db:
            return
        self.__db = mysql.connector.connect(
            host=host,
            port=port,
            database='joy_of_painting',
            user='jop_user',
            password='bobross'
        )

    def build_query_JSON_str(self, query: dict) -> str:
        """ Build part of query that select JSON values """
        json_str = ""
        if not (query.get('colors') or query.get('subject')):
            return ''
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
                    json_str += 'AND '
                else:
                    json_str += '( '
                json_str += (
                    "JSON_OVERLAPS(painting.subject, "
                    f"'{json.dumps(query['subject'])}') ) "
                )
        return json_str

    def build_query_date_str(self, query: dict) -> str:
        """ Build year and month part of query """
        return ''

    def build_query_str(self, query: dict) -> str:
        """ Build query from dict """
        query_str = (
            "SELECT episode.air_date, episode.episode, episode.season, "
            "painting.name, painting.colors, painting.subject "
            "FROM episode "
            "JOIN painting ON episode.painting_index = painting.index "
            "WHERE "
        )
        json_str = self.build_query_JSON_str(query)
        query_str += json_str
        # if json_str != '':
        #     query_str += 'AND '
        # date_str = self.build_query_date_str(query)
        # query_str += date_str

        # query_str += "( "

        # for col in query['colors']:
        #     query_str += (
        #         f"JSON_CONTAINS(painting.colors, )"
        #    )
        query_str += ';'
        return query_str
