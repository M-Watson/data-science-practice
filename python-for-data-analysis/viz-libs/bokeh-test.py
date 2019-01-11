import numpy as np

from bokeh.plotting import figure, show, output_file

from bokeh.resources import CDN
from bokeh.embed import file_html


N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(x_range=(0, 10), y_range=(0, 10),
           tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])

# must give a vector of image data for image parameter
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11")
p.toolbar.logo = None

output_file("image.html", title="image.py example")

show(p)  # open a browser

html = file_html(p, CDN, "my plot")
