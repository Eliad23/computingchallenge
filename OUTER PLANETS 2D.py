from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the figure and axis
fig, ax = plt.subplots()

# Set up the plot, with appropriate limits
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_aspect('equal', adjustable='box')

# Create scatter plots for Neptune, Jupiter, Uranus, and Saturn
neptune_scatter, = ax.plot([], [], 'b', label='Neptune', marker='o')
jupiter_scatter, = ax.plot([], [], 'r', label='Jupiter', marker='o')
uranus_scatter, = ax.plot([], [], 'g', label='Uranus', marker='o')
saturn_scatter, = ax.plot([], [], 'm', label='Saturn', marker='o')

# Create line plots to track the orbits
neptune_line, = ax.plot([], [], 'b', alpha=0.3)
jupiter_line, = ax.plot([], [], 'r', alpha=0.3)
uranus_line, = ax.plot([], [], 'g', alpha=0.3)
saturn_line, = ax.plot([], [], 'm', alpha=0.3)

# Create the yellow central dot
central_dot, = ax.plot([], [], 'yo', markersize=10)  # Use 'yo' for bright yellow

# Create the animation
num_frames = 10000  # Adjust this to control the number of frames (length of linspace)
interval = 50  # Milliseconds between frames

# Function to update the plot for each frame
def update(frame):

    theta = linspace(0, 360, num_frames)

    jupiterx = 5.20 * cos(theta) 
    jupitery = 5.20 * sin(theta)

    saturnx = 9.58 * cos(theta)
    saturny = 9.58 * sin(theta)

    neptunex = 30.25 * cos(theta)
    neptuney = 30.25 * sin(theta)

    uranusx = 19.29 * cos(theta)
    uranusy = 19.29 * sin(theta)
    
    neptune_scatter.set_data(neptunex[frame], neptuney[frame])
    jupiter_scatter.set_data(jupiterx[frame], jupitery[frame])
    uranus_scatter.set_data(uranusx[frame], uranusy[frame])
    saturn_scatter.set_data(saturnx[frame], saturny[frame])

    # Update the tracking lines
    neptune_line.set_data(neptunex[:frame+1], neptuney[:frame+1])
    jupiter_line.set_data(jupiterx[:frame+1], jupitery[:frame+1])
    uranus_line.set_data(uranusx[:frame+1], uranusy[:frame+1])
    saturn_line.set_data(saturnx[:frame+1], saturny[:frame+1])

    # Update the central yellow dot
    central_dot.set_data(0, 0)

    # Return a sequence of Artists for each scatter and line plot
    return (neptune_scatter, jupiter_scatter, uranus_scatter, saturn_scatter,
            neptune_line, jupiter_line, uranus_line, saturn_line, central_dot)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, repeat=False, blit=True)

# Set up the legend
ax.legend()

# Show the animation
plt.show()
