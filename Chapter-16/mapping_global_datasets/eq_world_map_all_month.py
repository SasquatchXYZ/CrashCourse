import os
from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/all_month.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    if mag is None:
        mag = 0.0
    if mag < 0:
        mag = 0.0
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=mags,
                     title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
# fig.show()
file_name = "global_earthquakes.html"
if os.path.exists(file_name):
    os.remove(file_name)
fig.write_html(file_name, auto_open=True)
