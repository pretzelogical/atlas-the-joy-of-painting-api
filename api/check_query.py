#!/usr/bin/env python3
""" Accepted values for queries """
import re
from datetime import datetime
from typing import Union


keys_accepted = ['match', 'month', 'color', 'subject']
match_accepted = ['all', 'some']
date_accepted = {"start": datetime(1983, 1, 1), "end": datetime(1994, 5, 31)}
colors_accepted = ['Black Gesso', 'Bright Red', 'Burnt Umber', 'Cadmium Yellow', 'Dark Sienna', 'Indian Red', 'Indian Yellow', 'Liquid Black', 'Liquid Clear', 'Midnight Black', 'Phthalo Blue', 'Phthalo Green', 'Prussian Blue', 'Sap Green', 'Titanium White', 'Van Dyke Brown', 'Yellow Ochre', 'Alizarin Crimson']  # noqa
subject_accepted = ['Apple Frame', 'Aurora Borealis', 'Barn', 'Beach', 'Boat', 'Bridge', 'Building', 'Bushes', 'Cabin', 'Cactus', 'Circle Frame', 'Cirrus', 'Cliff', 'Clouds', 'Conifer', 'Cumulus', 'Deciduous', 'Diane Andre', 'Dock', 'Double Oval Frame', 'Farm', 'Fence', 'Fire', 'Florida Frame', 'Flowers', 'Fog', 'Framed', 'Grass', 'Guest', 'Half Circle Frame', 'Half Oval Frame', 'Hills', 'Lake', 'Lakes', 'Lighthouse', 'Mill', 'Moon', 'Mountain', 'Mountains', 'Night', 'Ocean', 'Oval Frame', 'Palm Trees', 'Path', 'Person', 'Portrait', 'Rectangle 3d Frame', 'Rectangular Frame', 'River', 'Rocks', 'Seashell Frame', 'Snow', 'Snowy Mountain', 'Split Frame', 'Steve Ross', 'Structure', 'Sun', 'Tomb Frame', 'Tree', 'Trees', 'Triple Frame', 'Waterfall', 'Waves', 'Windmill', 'Window Frame', 'Winter', 'Wood Framed']  # noqa


def check_query(query) -> Union[None, str]:
    """ Check that query is valid and not malformed

    query can be empty object which fetches all episodes else
    require match and other keys

    if return is None then query is ok
    else return error text
    """
    if type(query) is not dict:
        return "Malformed JSON"
    if query == {}:
        return None
    query_filled = False
    for key, val in query.items():
        match key:
            case 'match':
                if val not in match_accepted:
                    return f"Invalid match value {val}"
            case 'month':
                validate_date = r"^\d{4}-\d{2}$"
                if not bool(re.match(validate_date, val)):
                    return f"Invalid date {val} format must be YYYY-MM"
                date_str_iso = f"{val}-01"
                from_iso = datetime.fromisoformat(date_str_iso)
                if not date_accepted['start'] <= from_iso <= date_accepted['end']:
                    return f"Date {val} out of range"
                query_filled = True
            case 'colors':
                if type(val) is not list:
                    return "Colors must be an array"
                for col in val:
                    if col not in colors_accepted:
                        return f"Invalid color {col} in {val}"
                query_filled = True
            case 'subject':
                if type(val) is not list:
                    return "Subject must be an array"
                for subj in val:
                    if subj not in subject_accepted:
                        return f"Invalid subject {subj} in {val}"
                query_filled = True
            case _:
                return f"Invalid key {key} in {list(query.keys())}"
    if not query_filled:
        return "Query requires keys month, colors and subject"
    return None
