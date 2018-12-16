from plotxel import Plotxel
from svgwrite import rgb
from cairosvg import svg2png
from PIL import Image
import random

x = Plotxel((500, 200))

# add some data as a series
x.add_data('series1', [0, 40, 80, 120, 160, 200], [0, 40, 80, 120, 160, 200])
x.add_data('series2', [0, 40, 80, 220, 120, 250], [0, 40, 80, 120, 160, 200])

# create a drawable object. Include its name, its type, and what data it is linked to

plot1 = x.add_drawable("plot1", "Scatter", "series1")
plot1 = x.drawables['plot1']
plot1.dim = [100, 100]
plot1.pos = [0, 0]
plot1.xlim = [0, 300]
plot1.ylim = [0, 200]
plot1.inside_border_width = 1

plot2 = x.add_drawable("plot2", "Scatter", "series2")
plot2 = x.drawables['plot2']
plot2.dim = [100, 100]
plot2.pos = [100, 0]
plot2.xlim = [0, 300]
plot2.ylim = [0, 200]
plot2.inside_border_width = 1
plot2.line = False

plot3 = x.add_drawable("plot3", "Scatter", "series2")
plot3 = x.drawables['plot3']
plot3.dim = [100, 100]
plot3.pos = [200, 0]
plot3.xlim = [0, 300]
plot3.ylim = [0, 200]
plot3.inside_border_width = 1
plot3.line = False


x.add_drawable("yaxis1", "YAxis", link_to='plot1')
yaxis1 = x.drawables['yaxis1']
yaxis1.side = 'left'
#yaxis1.pos = [50, 50]
yaxis1.font_size = 10
yaxis1.axis_offset = 5

x.add_drawable("yaxis2", "YAxis", link_to='plot3')
yaxis2 = x.drawables['yaxis2']
yaxis2.side = 'right'
#yaxis1.pos = [50, 50]
yaxis2.font_size = 10
yaxis2.axis_offset = 5


x.add_drawable("xaxis1", "XAxis", link_to='plot1')
xaxis1 = x.drawables['xaxis1']
yaxis1.font_size = 10
xaxis1.axis_offset = 5


#x.add_drawable("sidehist1", "YHist", link_to='plot1')

#x.add_drawable("plot2", "Scatter", "series2")
#plot2 = x.drawables['plot2']

#x.drawables['plot2'].dim = [100, 100]
#x.drawables['plot2'].pos = [101, 1]

#plot1.size = 5
#plot1.fill_color = (200, 50, 50)


print(x.draw())
image = svg2png(bytestring=x.draw(), write_to='image.png')

image = Image.open('image.png')
image.show()


#x.drawables['yaxis1'].pos = [45, 50]
#x.drawables['yaxis1'].dim = 100
#x.drawables['yaxis1'].lim = [0, 200]

"""
# create another drawable object. Include its name, its type, and what data it is linked to

x.add_data('series2', [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
x.add_drawable("plot2", "Scatter", "series2")
x.drawables['plot2'].dim = [100, 100]
x.drawables['plot2'].pos = [10, 10]
x.drawables['plot2'].xlim = [0, 100]
x.drawables['plot2'].ylim = [0, 100]
x.drawables['plot2'].size = 5
x.drawables['plot2'].rgb = rgb(50, 200, 50)
"""



