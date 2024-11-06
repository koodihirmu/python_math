import matplotlib.pyplot as plt
import numpy as np

fig_scale = 2
fig = plt.figure(figsize=(fig_scale * 6.4, fig_scale * 4.8), dpi=72)
axs = plt.subplot()

ticks = [0.0]
names = ["0"]
for i in range(1, 4):
    ticks.append(-i * np.pi)
    ticks.append(i * np.pi)
    if i == 1:
        names.append(f"-π")
        names.append(f"π")
    else:
        names.append(f"-{i}π")
        names.append(f"{i}π")

axs.set_xlabel("radians")
axs.set_ylabel("ratio")

axs.set_xticks(
    ticks=ticks,
    labels=names,
)

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)


plt.show()
