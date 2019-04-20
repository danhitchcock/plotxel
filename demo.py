from plotxel import Plotxel

x = Plotxel((800, 400))  # our main drawing canvas in x, y

# add some data as a series. The series name, the x data, and y data

series1 = [i for i in range(10)]
x.add_data('series1', series1, series1)

#x.add_data('series1', [0, 40, 80, 120, 160, 200], [0, 40, 80, 120, 160, 200])

# left plot -- its name, type, and data it's linked to
plot1 = x.add_drawable("plot1", "Scatter", "series1")
plot1.pos = [50, 50]

# right plot and its position. Same data as plot1
plot2 = x.add_drawable("plot2", "Scatter", "series1")
plot2.pos = [360, 50]  # since the default plot size is 300px, 360 will place 10 blank pixels between the graphs
plot2.setattrs(
    marker_shape='square',
    marker_fill_color=(255, 0, 0),
    title='Number of Geese on the Bike Path'
)

ax1 = x.add_drawable("ax1", 'YAxis', link_to="plot1")
ax1.axis_offset = 10

ax2 = x.add_drawable("ax2", 'YAxis', link_to="plot2")
ax2.side = 'right'
ax2.axis_offset = 10

ax3 = x.add_drawable("ax3", 'XAxis', link_to="plot2")
ax3.side = 'bottom'
ax3.axis_offset = 10
ax3.axis_label = "Number of f****** geese"
ax3.axis_label_offset = 30


x.show()

"""
# create a drawable object. Include its name, its type, and what data it is linked to
plot1 = x.add_drawable("plot1", "Scatter", "series1")  # assign during creation
plot1 = x.drawables['plot1']  # or retrieve it later!
plot1.pos = [50, 50]  # position from top corner. 0,0 is the top left pixel; this gives us [X, Y] blank pixels from y and x
plot1.dim = [200, 100]  # how big is the chart area?
plot1.xlim = [0, 200]  # scatter limits for x
plot1.ylim = [0, 200]  # scatter limits for y
plot1.inside_border_width = 1  # border goes on the *inside*.
plot1.outside_border_width = 5  # to be implemented soon! border on the outside
plot1.marker_border_width = 2  # outline of the svg circles
plot1.marker_size = 14  # size of the svg circles
plot1.marker_fill_color = [255, 0, 0]
plot1.marker_shape = 'circle'

plot2 = x.add_drawable("plot2", "Scatter", "series1")  # assign during creation
plot2 = x.drawables['plot2']  # or retrieve it later!
plot2.pos = [249, 50]  # position from top corner. 0,0 is the top left pixel; this gives us [X, Y] blank pixels from y and x
plot2.dim = [200, 100]  # how big is the chart area?
plot2.xlim = [0, 200]  # scatter limits for x
plot2.ylim = [0, 200]  # scatter limits for y
plot2.inside_border_width = 1  # border goes on the *inside*.
plot2.outside_border_width = 5  # to be implemented soon! border on the outside
plot2.marker_border_width = 2  # outline of the svg circles
plot2.marker_size = 14  # size of the svg circles
plot2.marker_fill_color = [0, 0, 255]
plot2.marker_shape = 'square'

plot3 = x.add_drawable("plot3", "Scatter", "series1")  # assign during creation
plot3 = x.drawables['plot3']  # or retrieve it later!
plot3.pos = [448, 50]  # position from top corner. 0,0 is the top left pixel; this gives us [X, Y] blank pixels from y and x
plot3.dim = [200, 100]  # how big is the chart area?
plot3.xlim = [0, 200]  # scatter limits for x
plot3.ylim = [0, 200]  # scatter limits for y
plot3.inside_border_width = 1  # border goes on the *inside*.
plot3.outside_border_width = 5  # to be implemented soon! border on the outside
plot3.marker_border_width = 2  # outline of the svg circles
plot3.marker_size = 14  # size of the svg circles
plot3.marker_fill_color = [0, 0, 255]
plot3.marker_shape = 'rect'


# linking to another plot pulls its scale, position, size, and data, unless they're explicitly set
x.add_drawable("yaxis2", "YAxis", link_to='plot1')
yaxis2 = x.drawables['yaxis2']
yaxis2.side = 'left'
yaxis2.font_size = 10
yaxis2.axis_offset = 5
yaxis2.axis_linewidth = 2
yaxis2.major_tick_linewidth = 1
yaxis2.major_tick_length = 5

x.add_drawable("yaxis1", "YAxis", link_to='plot3')
yaxis1 = x.drawables['yaxis1']
yaxis1.side = 'right'
yaxis1.font_size = 10
yaxis1.axis_offset = 5
yaxis1.axis_linewidth = 2
yaxis1.major_tick_linewidth = 1
yaxis1.major_tick_length = 5

x.add_drawable("xaxis1", "XAxis", link_to='plot1')
xaxis1 = x.drawables['xaxis1']
xaxis1.side='bottom'
xaxis1.font_size = 10
xaxis1.axis_offset = 5
xaxis1.axis_linewidth = 2
xaxis1.major_tick_length = 5
xaxis1.major_tick_linewidth = 1

x.add_drawable("xaxis2", "XAxis", link_to='plot1')
xaxis2 = x.drawables['xaxis2']
xaxis2.side='top'
xaxis2.font_size = 10
xaxis2.axis_offset = 5
xaxis2.axis_linewidth = 2
xaxis2.major_tick_length = 5
xaxis2.major_tick_linewidth = 1


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

"""
#x.add_drawable("sidehist1", "YHist", link_to='plot1')

#x.add_drawable("plot2", "Scatter", "series2")
#plot2 = x.drawables['plot2']

#x.drawables['plot2'].dim = [100, 100]
#x.drawables['plot2'].pos = [101, 1]

#plot1.size = 5
#plot1.fill_color = (200, 50, 50)




#print(x.draw())
#x.show()
#image = svg2png(bytestring=x.draw(), write_to='image.png')
#image = x.render()

#image = Image.open('image.png')
#image.show()


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



