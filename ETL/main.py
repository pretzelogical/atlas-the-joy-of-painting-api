#!/usr/bin/env python3
# import csv
import mysql.connector
from datetime import datetime


painting_map = {
    "index": int,
    "name": str,
    "img_src": str,
    "colors": list,
    "colors_hex": list,
    "subject": list
}
episode_map = {
    "id": int,
    "season": int,
    "episode": int,
    "air_date": datetime,
    "youtube_src": str,
    "painting_index": int
}


def convert_to_date(episode_date: str) -> datetime:
    date_map = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    # first parenthesis always contains date so get and split
    ep_dates_str = (
        episode_date.split('(')[1].split(')')[0].replace(',', '').split(' ')
    )
    print(ep_dates_str)
    month = date_map[ep_dates_str[0]]
    day = int(ep_dates_str[1])
    year = int(ep_dates_str[2])
    return datetime(year, month, day)


print(convert_to_date('"A Walk in the Woods" (January 11, 1983)'))

# db_conn = mysql.connector.connect(user='jop_etl_user', password='bobross',
#                                   host='localhost', port=3306,
#                                   db='joy_of_painting')
# cursor = db_conn.cursor()
# query = ("DESCRIBE painting")

# cursor.execute(query)
# print(cursor.fetchall())

# cursor.close()
# db_conn.close()
