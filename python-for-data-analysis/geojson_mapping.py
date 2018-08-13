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
    BLUE = '#6699cc'
    th = []
    feature_list = []
    poly_list = []
    fig_base = plt.figure()
    th.append(requests.get(url_list['geojsonURL'][3]).text)
    gj = geojson.loads(th[ii])
    with open(fp) as f:
        gj = geojson.load(f)

    i = 0
    i_end = len(gj['features']) - 1
    for i in range(i_end):
        feature_list.append(gj['features'][i])
        poly_list.append(gj['features'][i]['geometry'])
           #Plotting
        ax_1 = fig_base.gca()
        ax_1.add_patch(PolygonPatch(poly_list[i], fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))

    ax_1.axis('scaled')
    plt.show()
    return(fig_base)
