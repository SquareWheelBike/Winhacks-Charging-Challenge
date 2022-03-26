# import data for essex county, ontario into overpy

import overpy

api = overpy.Overpass()

# (south, west, north, east)
bbox=(41.9794,-83.1191,42.3454,-82.4943)

data = '../data/WindsorEssex OpenMap Data.xml'

data = api.parse_xml(data)