import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
L = 20  # Length of the x-axis
N = 100  # Number of discrete points
t_max = 10  # Increased duration for slower animation
fps = 30  # Frames per second
speed = 0.04  # Decreased speed of wave movement
wavelength = 1  # Further decreased wavelength
amplitude = 1  # Decreased amplitude
fade_in_frames = 30  # Number of frames for wave to appear gradually

# Space array
x = np.linspace(0, L, N)
y = np.zeros_like(x)  # All points initially at y = 0

# Initialize figure
fig, ax = plt.subplots(figsize=(18, 10))  # Adjust width and height as needed
ax.set_xlim(0, L)
ax.set_ylim(-5, 5)  # Set y-axis range
line, = ax.plot(x, y, '-o')  # Line connecting points

# Update function
def update(frame):
    if frame < fade_in_frames:
        alpha = frame / fade_in_frames  # Gradual appearance factor
    else:
        alpha = 1  # Fully visible wave
    
    # Superposition of two waves moving in opposite directions
    y[:] = alpha * amplitude * (
        np.exp(-((x - speed * frame) ** 2) / (2 * (wavelength/2) ** 2)) +
        np.exp(-((x + speed * frame - L) ** 2) / (2 * (wavelength/2) ** 2))
    )
    
    line.set_ydata(y)  # Update line
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, interval=1000/fps, blit=False)
plt.show()
