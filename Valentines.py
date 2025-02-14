import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Correct function with symmetry across the y-axis
def f(x, a):
    return (np.abs(x) ** (2/3)) + 0.9 * np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)

# Setup the figure
fig, ax = plt.subplots()

# Set a more vibrant pink background
fig.patch.set_facecolor('#FFB6C1')  # Deeper pink figure background
ax.set_facecolor('#FFB6C1')  # Deeper pink axes background

x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 400)  # Restrict domain to avoid sqrt errors
line, = ax.plot([], [], 'r-', lw=2)

# Set plot limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)  # Remove border

# Add "Happy Valentine's Day" message at the top
ax.text(0, 2.7, "Happy Valentine's Day!", fontsize=18, color='red', ha='center', fontweight='bold')

# Add the equation at the bottom
ax.text(0, -2.8, r"$y = |x|^{\frac{2}{3}} + 0.9\sqrt{3.3 - x^2} \sin(a\pi x)$", 
        fontsize=14, color='red', ha='center', fontstyle='italic')

# Update function for animation
def update(frame):
    a = -2.5 + frame * 0.05  # Smooth transition
    y = f(x, a)
    line.set_data(x, y)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=450, interval=20, blit=True)

plt.show()
