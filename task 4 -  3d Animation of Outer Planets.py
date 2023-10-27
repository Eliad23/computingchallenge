import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Orbital parameters (semi-major axis in AU and orbital period in Earth years)
planet_params = {
    'Jupiter': (5.2, 11.9),
    'Saturn': (9.6, 29.5),
    'Uranus': (19.2, 84.0),
    'Neptune': (30.1, 164.8),
    'Pluto': (39.5, 248.0)
}

# Generate time values
num_frames = 500
t = np.linspace(0, max([p[1] for p in planet_params.values()]), num_frames)

# Generate planet positions for each time step
planet_positions = {}
for planet, (a, T) in planet_params.items():
    x = a * np.cos(2 * np.pi * t / T)
    y = a * np.sin(2 * np.pi * t / T)
    z = np.zeros_like(t)
    planet_positions[planet] = np.array([x, y, z])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lines = {}
for planet in planet_positions:
    lines[planet], = ax.plot([], [], [], label=planet)

def update(frame):
    for planet, line in lines.items():
        line.set_data(planet_positions[planet][:2, frame])
        line.set_3d_properties(planet_positions[planet][2, frame])
    return list(lines.values())

anim = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_zlim(-10, 10)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.legend()

plt.show()
