from fractions import Fraction as fr

import matplotlib as mpl
import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("center")

# Eliminate upper and right axes
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.axis("equal")

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])


def get_x(degree):
    degree = np.deg2rad(degree)
    return np.cos(degree)


def get_y(degree):
    degree = np.deg2rad(degree)
    return np.sin(degree)


pist_xy = np.array([30, 45, 60, 90, 120, 150, 180, 270])

x = get_x(pist_xy)
y = get_y(pist_xy)

plt.scatter(x, y, marker="x")

for i in pist_xy:
    plt.annotate(
        text=f"{i}°",
        xy=(get_x(i), get_y(i)),
        xycoords="data",
        xytext=(+30, +5),
        textcoords="offset points",
        fontsize=12,
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )


plt.show()
