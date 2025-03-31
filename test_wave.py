import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
L = 20  # Length of the x-axis
N = 150  # Number of discrete points
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

def my_new_wave(mywavelength, mydirection, mypropagation, mybirthdelay, myinitialposition, myspeed, index, myframe):
    director = 0
    motion = 0
    if mybirthdelay > myframe:
        return 0
    elif myframe - mybirthdelay < fade_in_frames:
        appearance_factor = (myframe - mybirthdelay)/ fade_in_frames  # Gradual appearance factor
    else:
        appearance_factor = 1  # Fully visible wave

    spawn = (myframe - mybirthdelay)
    if mydirection == "up":
        director = 1
    elif mydirection == "down":
        director = -1
    if mypropagation == "forward":
        motion = 1
    elif mypropagation == "backward":
        motion = -1
    return appearance_factor * director * np.exp(-(((index - myinitialposition) - (motion * myspeed) * spawn) ** 2) / (2 * (mywavelength/2) ** 2))

# Update function
def update(frame):
    # Superposition of two waves moving in opposite directions
    y[:] = amplitude * (
        my_new_wave(wavelength, "up", "forward", 0, 0, speed, x, frame) +
        my_new_wave(wavelength*2, "down","backward", 100, L, 3*speed/2, x, frame) +
        my_new_wave(wavelength, "up", "forward", 100, L/2, 5*speed/2, x, frame)
    )
    
    line.set_ydata(y)  # Update line
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, interval=1000/fps, blit=False)
plt.show()
