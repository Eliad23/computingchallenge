from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots()

# Set up the plot, with appropriate limits
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', adjustable='box')

# Create scatter plots for Earth, Mercury, Mars, and Venus
earth_scatter, = ax.plot([], [], 'b', label='Earth', marker='o')
mercury_scatter, = ax.plot([], [], 'r', label='Mercury', marker='o')
mars_scatter, = ax.plot([], [], 'g', label='Mars', marker='o')
venus_scatter, = ax.plot([], [], 'm', label='Venus', marker='o')

# Create line plots to track the orbits
earth_line, = ax.plot([], [], 'b', alpha=0.3)
mercury_line, = ax.plot([], [], 'r', alpha=0.3)
mars_line, = ax.plot([], [], 'g', alpha=0.3)
venus_line, = ax.plot([], [], 'm', alpha=0.3)

# Create the animation
num_frames = 10000  # Adjust this to control the number of frames (length of linspace)
interval = 50  # Milliseconds between frames

# Function to update the plot for each frame
def update(frame):

    theta = linspace(0,360, num_frames)

    mercuryx = 0.387*cos(theta) +0.1 
    mercuryy = 0.387*sin(theta)

    venusx = 0.723*cos(theta)
    venusy = 0.723*sin(theta)

    earthx = cos(theta)
    earthy = sin(theta)

    marsx= 1.523*cos(theta) +0.15
    marsy = 1.523*sin(theta)
    earth_scatter.set_data(earthx[frame], earthy[frame])
    mercury_scatter.set_data(mercuryx[frame], mercuryy[frame])
    mars_scatter.set_data(marsx[frame], marsy[frame])
    venus_scatter.set_data(venusx[frame], venusy[frame])

    # Update the tracking lines
    earth_line.set_data(earthx[:frame+1], earthy[:frame+1])
    mercury_line.set_data(mercuryx[:frame+1], mercuryy[:frame+1])
    mars_line.set_data(marsx[:frame+1], marsy[:frame+1])
    venus_line.set_data(venusx[:frame+1], venusy[:frame+1])

    # Return a sequence of Artists for each scatter and line plot
    return (earth_scatter, mercury_scatter, mars_scatter, venus_scatter,
            earth_line, mercury_line, mars_line, venus_line)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, repeat=True, blit=True)

# Set up the legend
ax.legend()

# Show the animation
plt.show()
