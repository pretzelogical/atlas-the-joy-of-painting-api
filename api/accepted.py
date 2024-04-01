#!/usr/bin/env python3
""" Accepted values for queries """
from datetime import datetime


keys_accepted = ['match', 'month', 'color', 'subject']
match_accepted = ['all', 'some']
month_accepted = {"start": datetime(1983, 1, 11), "end": datetime(1994, 5, 17)}
colors_accepted = ['Black Gesso', 'Bright Red', 'Burnt Umber', 'Cadmium Yellow', 'Dark Sienna', 'Indian Red', 'Indian Yellow', 'Liquid Black', 'Liquid Clear', 'Midnight Black', 'Phthalo Blue', 'Phthalo Green', 'Prussian Blue', 'Sap Green', 'Titanium White', 'Van Dyke Brown', 'Yellow Ochre', 'Alizarin Crimson']  # noqa
subject_accepted = ['Apple Frame', 'Aurora Borealis', 'Barn', 'Beach', 'Boat', 'Bridge', 'Building', 'Bushes', 'Cabin', 'Cactus', 'Circle Frame', 'Cirrus', 'Cliff', 'Clouds', 'Conifer', 'Cumulus', 'Deciduous', 'Diane Andre', 'Dock', 'Double Oval Frame', 'Farm', 'Fence', 'Fire', 'Florida Frame', 'Flowers', 'Fog', 'Framed', 'Grass', 'Guest', 'Half Circle Frame', 'Half Oval Frame', 'Hills', 'Lake', 'Lakes', 'Lighthouse', 'Mill', 'Moon', 'Mountain', 'Mountains', 'Night', 'Ocean', 'Oval Frame', 'Palm Trees', 'Path', 'Person', 'Portrait', 'Rectangle 3d Frame', 'Rectangular Frame', 'River', 'Rocks', 'Seashell Frame', 'Snow', 'Snowy Mountain', 'Split Frame', 'Steve Ross', 'Structure', 'Sun', 'Tomb Frame', 'Tree', 'Trees', 'Triple Frame', 'Waterfall', 'Waves', 'Windmill', 'Window Frame', 'Winter', 'Wood Framed']  # noqa
