import pandas as pd
import geoplotlib
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
import json


def get_color(county):
    key = county['NAME']
    county_df = (df[df['county'] == key]) # .iloc[0]['clusters']
    # val = county_df.iloc[0]['nitr'] / county_df.iloc[0]['nitr1'] if county_df.iloc[0]['nitr1'] != 0 else 0
    # print(cmap.to_color(val, 17, 'lin'))
    val = county_df.iloc[0]['clusters_all']
    return cmap.to_color(val, 10, 'lin')


df = pd.read_csv('clusters_new_all.csv')

cmap = ColorMap('prism', alpha=255, levels=10)
geoplotlib.geojson('cali.json', fill=True, color=get_color, f_tooltip=lambda county: county['NAME'])
geoplotlib.geojson('cali.json', fill=False, color=[0, 0, 0, 64])
# geoplotlib.set_bbox(BoundingBox(32.5295236, 42.009499, -124.482003, -114.1307816))
geoplotlib.show()
