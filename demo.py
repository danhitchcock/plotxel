from plotxel import Plotxel, Axis

x = Plotxel((800, 500))  # our main drawing canvas in x, y

# add some data as a series. The series name, the x data, and y data
series1 = [i for i in range(10)]
x.add_data('series1', series1, series1)
x.add_data('series2', [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

# left plot -- its name, type, and data it's linked to
plot1 = x.add_drawable("plot1", "Scatter", "series1")
plot1.title = 'Analysis of Goose Encounters'
plot1.pos = [60, 50]

# right plot and its position. Same data as plot1
plot2 = x.add_drawable("plot2", "Scatter", "series1")
# set a bunch of attributes at once!
# since the default plot size is 300px, 360 will place 10 blank pixels between the graphs
plot2.setattrs(
    pos=[450, 50],
    marker_shape='square',
    marker_fill_color=(255, 0, 0),
    title='Analysis of Goose Encounters (red)'
)

# add some axes, and link them to our plots. It will copy the size, position, scale, and limits of whichever plot it is linked to
ax1 = x.add_drawable("ax1", 'YAxis', link_to="plot1")
ax1.axis_offset = 10
ax1.title = "Near Death Experiences With Geese"

# all other axes, let's put them flush with the graph by changing the default
# defaults are copied at the time the object is initialized, so this won't affect ax1
Axis.defaults['axis_offset'] = -1
ax1b = x.add_drawable('ax1b', 'XAxis', link_to='plot1')

ax1r = x.add_drawable('ax1r', 'YAxis', link_to='plot1')
ax1r.side = 'right'
ax1r.title = 'Ax1 Right Title'

ax2 = x.add_drawable("ax2", 'YAxis', link_to="plot2")
ax2.side = 'right'
ax2.axis_offset = 10

ax3 = x.add_drawable("ax3", 'XAxis', link_to="plot2")
ax3.setattrs(
    side='bottom',
    axis_offset=10,
    title="Number of freaking geese",
)


# I think I would prefer axes to be blue!
Axis.defaults['color'] = (0, 0, 255)


plot3_attrs = {
    'pos': (60, 300),
    'ylim': [0, 10],
    'title': 'Near Death Experiences With Geese'
}
plot3 = x.add_drawable('bar1', 'Bar', 'series2')

plot3.setattrs(**plot3_attrs)

ax4 = x.add_drawable('ax4', 'YAxis', link_to="bar1")
ax4.setattrs(
    axis_offset=-1,
    title='Near Death Experiences With Geese'
)


# x.show()

# or for SVG
# svg_html = x.draw()

# or for image  in BytesIO / save to filename
x.render(filename='example1.png')

#x.anti_aliasing=False
# quick test! another test
#x.show()


