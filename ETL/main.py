#!/usr/bin/env python3
import json
import csv
from datetime import datetime
from typing import List, Tuple
"""Extract transform and load tjop data

Assumptions made: data in all files is ordered from first episode to last
episode
"""


def convert_to_date(line: str) -> datetime:
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
        line.split('(')[1].split(')')[0].replace(',', '').split(' ')
    )
    month = date_map[ep_dates_str[0]]
    day = int(ep_dates_str[1])
    year = int(ep_dates_str[2])
    return datetime(year, month, day)


def titles_dates_extract() -> List[Tuple[str, datetime]]:
    """ Extract titles and dates """
    titles_dates = []
    with open('tjop_episode_dates.txt', encoding='utf-8') as f:
        for line in f:
            if not line:
                continue
            title = line.split('"')[1].replace('"', '')
            titles_dates.append((title, convert_to_date(line)))
    return titles_dates


def csv_extract() -> Tuple[List[dict], List[dict]]:
    """ Get the csv data from subject mattter and colors used """
    colors_used = []
    subject_matter = []
    with open('tjop_colors_used.csv', encoding='utf-8') as f:
        color_reader = csv.DictReader(f)
        colors_used = [c for c in color_reader]

    with open('tjop_subject_matter.csv', encoding='utf-8') as f:
        subject_reader = csv.DictReader(f)
        subject_matter = [s for s in subject_reader]

    return (colors_used, subject_matter)


def subject_to_json_list(colors_dict: dict) -> str:
    """ Converts subject booleans to list that matches formatting of other
    JSON lists in database
    """
    subjects = []
    exclude_keys = ['EPISODE', 'TITLE']
    for key, val in colors_dict.items():
        if key in exclude_keys:
            continue
        if val == '1':
            normal_key = (
                ' '.join(
                        map(
                            lambda k: k[0].upper() + k[1:],
                            key.lower().split('_')
                        ),
                )
            )
            subjects.append(normal_key)
    return json.dumps(subjects)


def records_transform(titles_dates,
                      subject_matter,
                      colors_used) -> Tuple[List[dict], List[dict]]:
    """ Takes gathered data and transforms it to be stored in the SQL database
    Type map for painting dict:
        {
            "index": int,
            "name": str,
            "img_src": str,
            "colors": list,
            "colors_hex": list,
            "subject": list
        }

    Type map for episode dict:
        {
            "season": int,
            "episode": int,
            "air_date": datetime,
            "youtube_src": str,
            "painting_index": int
        }
    """
    paintings_arr = []
    episodes_arr = []
    clean_json = (
        lambda s: s.replace("\\n", "").replace("\\r", "").replace("'", '"')
    )
    for i, colors in enumerate(colors_used):

        paintings_arr.append({
            "index": int(colors['painting_index']),
            "name": titles_dates[i][0],
            "img_src": colors['img_src'],
            "colors": clean_json(colors['colors']),
            "colors_hex": clean_json(colors['color_hex']),
            "subject": subject_to_json_list(subject_matter[i])
        })

        episodes_arr.append({
            "season": int(colors["season"]),
            "episode": int(colors["episode"]),
            "air_date": titles_dates[i][1],
            "youtube_src": colors["youtube_src"],
            "painting_index": int(colors["painting_index"])
        })

    return (episodes_arr, paintings_arr)


def write_sql_init(episodes, paintings):

    insert_paintings = (
        "INSERT INTO painting\n"
        '(`index`, `name`, `img_src`, `colors`, `colors_hex`, `subject`)\n'
        'VALUES\n'
    )
    for pnt in paintings:
        pnt_name = pnt['name'].replace("'", "''")
        insert_paintings += (
            f"({pnt['index']}, '{pnt_name}', '{pnt['img_src']}', "
            f"'{pnt['colors']}', '{pnt['colors_hex']}', '{pnt['subject']}'),\n"
        )
    insert_paintings = insert_paintings[:-2] + ";\n\n"

    insert_episodes = (
        "INSERT INTO episode\n"
        '(`season`, `episode`, `air_date`, `youtube_src`, `painting_index`)\n'
        'VALUES\n'
    )
    for epo in episodes:
        insert_episodes += (
            f"({epo['season']}, {epo['episode']}, "
            f"'{str(epo['air_date'])[:10]}', '{epo['youtube_src']}', "
            f"{epo['painting_index']}),\n"
        )
    insert_episodes = insert_episodes[:-2] + ";\n\n"

    pre_init = ""
    final_init = ""
    with open('pre.init.sql', mode='r', encoding='utf-8') as pre_f:
        pre_init = pre_f.read()

    with open('init.sql', mode='w', encoding='utf-8') as f:
        final_init = pre_init + insert_paintings + insert_episodes
        f.write(final_init)


def main():
    # extract
    titles_dates = titles_dates_extract()
    colors_used, subject_matter = csv_extract()
    # transform
    episodes, paintings = records_transform(
        titles_dates,
        subject_matter,
        colors_used
    )

    # load
    write_sql_init(episodes, paintings)

    print(len(episodes), len(paintings))


main()
