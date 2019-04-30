# Plotxel

*Control your plots down to the pixel!*  
Ever have trouble moving a chart to the right? Moving your axis up? Getting rid of ticks? Then try out Plotxel!

It's wordy, slow, and unnecessary 99% of the time. But that 1%, you'll be glad you have Plotxel.

## Installation

    pip3 install plotxel
    
## Example

    from plotxel import Plotxel
    
    x = Plotxel((800, 400))  # our main drawing canvas in x, y
    
    # add some data as a series. The series name, the x data, and y data
    series1 = [i for i in range(10)]
    x.add_data('series1', series1, series1)
   
    # left plot -- its name, type, and data it's linked to
    plot1 = x.add_drawable("plot1", "Scatter", "series1")
    plot1.pos = [50, 50]
    
    # right plot and its position. Same data as plot1
    plot2 = x.add_drawable("plot2", "Scatter", "series1")
    # set a bunch of attributes at once! 
    # since the default plot size is 300px, 360 will place 10 blank pixels between the graphs
    plot2.setattrs(
        pos=[360, 50],
        marker_shape='square',
        marker_fill_color=(255, 0, 0),
        title='Number of Geese on the Bike Path'
    )
    
    # add some axes, and link them to our plots. It will copy the size, position, scale, and limits.
    ax1 = x.add_drawable("ax1", 'YAxis', link_to="plot1")
    ax1.axis_offset = 10
    
    ax2 = x.add_drawable("ax2", 'YAxis', link_to="plot2")
    ax2.side = 'right'
    ax2.axis_offset = 10
    
    ax3 = x.add_drawable("ax3", 'XAxis', link_to="plot2")
    ax3.setattrs(
        side = 'bottom',
        axis_offset = 10,
        axis_label = "Number of freaking geese",
        axis_label_offset = 30
    )
    
    
    x.show()
    
    # or for SVG
    # svg_html = x.draw()
    
    # or for image in BytesIO / save to filename
    # x.render(filename=None)
    

![Example1 Image](https://github.com/danhitchcock/plotxel/wiki/example1.png)
    
This program is being developed based on my own needs, and unfortunately I don't do a lot of plotting today, therefore I don't need a lot of features.

In any case, I'll be prioritizing features, up next is bar charts and histograms! 