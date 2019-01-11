import json # reading geojson files
import matplotlib.pyplot as plt # plotting data
from shapely.geometry import asShape # manipulating geometry
from descartes import PolygonPatch # integrating geom object to matplot
import random

#------------------------- LOAD THE DATA -----------------------------
data = json.load(open("nola-neighborhood.geojson")) # from data folder.

# initiate the plot axes
fig = plt.figure(figsize=(20, 15)) # create a figure to contain the plot elements
ax = fig.gca(xlabel="Longitude", ylabel="Latitude")
color_r = 0.1843
color_g = 0.3098
color_b = 0.3098
# loop through the features plotting polygon centroid
for feat in data["features"]:

    color_r = random.uniform(0, 1)
    color_g = random.uniform(0, 1)
    color_b = random.uniform(0, 1)
    # convert the geometry to shapely
    geom = asShape(feat["geometry"])
    # obtain the coordinates of the feature's centroid
    x, y = geom.centroid.x, geom.centroid.y
    # plot the centroids
    ax.plot(x, y, 'None')
    # label the features at the centroid location
    #ax.text(x, y, feat['properties']['gnocdc_lab'], fontsize=4, bbox = dict(fc='w',alpha=0.3))
    # plot the polygon features: type help(PolygonPatch) for more args
    ax.add_patch(PolygonPatch(feat["geometry"], fc=(color_r,color_g,color_b), ec='blue',
                alpha=0.5, lw=0.5, ls='--', zorder=2))

ax.clear # clear the axes memory

plt.show()
