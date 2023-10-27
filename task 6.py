import numpy as np
import matplotlib.pyplot as plt

# Orbital parameters for Earth
a_earth = 1.0  # Semi-major axis in AU
e_earth = 0.0167  # Eccentricity
T_earth = 1.0  # Orbital period in years

# Orbital parameters for Mars
a_mars = 1.52  # Semi-major axis in AU
e_mars = 0.0934  # Eccentricity
T_mars = 1.88  # Orbital period in years

# Number of orbits and time intervals
N = 10
Dt = N * max(T_earth, T_mars) / 1234

# Calculate mean motion for Earth and Mars
n_earth = 2 * np.pi / T_earth
n_mars = 2 * np.pi / T_mars

# Time values
num_points = 1000  # Number of points for calculation
time_years = np.linspace(0, N * max(T_earth, T_mars), num_points)

# Calculate positions for Earth and Mars over time
theta_earth = n_earth * time_years
theta_mars = n_mars * time_years

r_earth = a_earth * (1 - e_earth**2) / (1 + e_earth * np.cos(theta_earth))
r_mars = a_mars * (1 - e_mars**2) / (1 + e_mars * np.cos(theta_mars))

x_earth = r_earth * np.cos(theta_earth)
y_earth = r_earth * np.sin(theta_earth)

x_mars = r_mars * np.cos(theta_mars)
y_mars = r_mars * np.sin(theta_mars)

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x_earth, y_earth, label='Earth Orbit')
plt.plot(x_mars, y_mars, label='Mars Orbit')
plt.scatter([x_earth[0], x_earth[-1]], [y_earth[0], y_earth[-1]], color='blue', marker='o', label='Earth Start/End')
plt.scatter([x_mars[0], x_mars[-1]], [y_mars[0], y_mars[-1]], color='red', marker='o', label='Mars Start/End')

# Draw lines between Earth and Mars at specified time intervals
for t in np.arange(0, N * max(T_earth, T_mars), Dt):
    idx = np.argmin(np.abs(time_years - t))
    plt.plot([x_earth[idx], x_mars[idx]], [y_earth[idx], y_mars[idx]], 'k--', alpha=0.5)

plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Orbits of Earth and Mars with Connecting Lines')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
