import geojson
from descartes import PolygonPatch
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
from shapely.geometry import Polygon
import math
import numpy as np
import requests
import pandas as pd


def base_map(fp):
    #fp = "..\\..\\..\\Geographies\GeoJson\\Census_Tracts_in_2010.geojson"
    with open(fp) as f:
        gj = geojson.load(f)
    BLUE = '#6699cc'

    fig = plt.figure(num=None, figsize=(20, 16), dpi=80, facecolor='w', edgecolor='k')
    fig.show()
    return(fig)


fp = "nola-neighborhood.geojson"

a= base_map(fp)
a.show()
input('wait')
