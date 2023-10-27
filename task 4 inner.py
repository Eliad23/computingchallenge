import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

num_frames = 5000  # Increase the number of frames for smoother animation

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set up the data for the planets
theta = np.linspace(0, 360, 5000)

jx = 5.20 * np.cos(theta)
jy = 5.20 * np.sin(theta)
jupiterx = jx * np.cos(1.31)
jupitery = jy
jupiterz = jx * np.sin(1.31)

sx = 9.58 * np.cos(theta)
sy = 9.58 * np.sin(theta)
saturnx = sx * np.cos(2.49)
saturny = sy
saturnz = sx * np.sin(2.49)

nx = 30.25 * np.cos(theta)
ny = 30.25 * np.sin(theta)
neptunex = nx * np.cos(1.77)
neptuney = ny
neptunez = nx * np.sin(1.77)

ux = 19.29 * np.cos(theta)
uy = 19.29 * np.sin(theta)
uranusx = ux * np.cos(0.77)
uranusy = uy
uranusz = ux * np.sin(0.77)

px = 39.509 * np.cos(theta)
py = 39.509 * np.sin(theta)
plutox = px * np.cos(17.5)
plutoy = py
plutoz = px * np.sin(17.5)

# Plot the orbits
jupiter_orbit, = ax.plot(jupiterx, jupitery, jupiterz, label='Jupiter')
saturn_orbit, = ax.plot(saturnx, saturny, saturnz, label='Saturn')
neptune_orbit, = ax.plot(neptunex, neptuney, neptunez, label='Neptune')
uranus_orbit, = ax.plot(uranusx, uranusy, uranusz, label='Uranus')
pluto_orbit, = ax.plot(plutox, plutoy, plutoz, label='Pluto')

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Orbits of Planets')
ax.legend()

# Function to update the plot during animation
def update(frame):
    jupiter_idx = int(len(jupiterx) * (frame / num_frames))
    saturn_idx = int(len(saturnx) * (frame / num_frames))
    neptune_idx = int(len(neptunex) * (frame / num_frames))
    uranus_idx = int(len(uranusx) * (frame / num_frames))
    pluto_idx = int(len(plutox) * (frame / num_frames))
    
    jupiter_orbit.set_data(jupiterx[:jupiter_idx], jupitery[:jupiter_idx])
    jupiter_orbit.set_3d_properties(jupiterz[:jupiter_idx])
    
    saturn_orbit.set_data(saturnx[:saturn_idx], saturny[:saturn_idx])
    saturn_orbit.set_3d_properties(saturnz[:saturn_idx])
    
    neptune_orbit.set_data(neptunex[:neptune_idx], neptuney[:neptune_idx])
    neptune_orbit.set_3d_properties(neptunez[:neptune_idx])
    
    uranus_orbit.set_data(uranusx[:uranus_idx], uranusy[:uranus_idx])
    uranus_orbit.set_3d_properties(uranusz[:uranus_idx])
    
    pluto_orbit.set_data(plutox[:pluto_idx], plutoy[:pluto_idx])
    pluto_orbit.set_3d_properties(plutoz[:pluto_idx])

# Create the animation with a slower interval
interval = 90  # Increase this value for a slower animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=False)  # Set blit to False for smoother rendering

# Display the animation
plt.show()
