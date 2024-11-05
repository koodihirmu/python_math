import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(3 * 6.4, 3 * 4.8), dpi=72)
axs = plt.subplot()

axs.set_xticks(
    ticks=np.arange(-3 * np.pi, 3 * np.pi + np.pi / 4, np.pi / 4),
    labels=[
        f"{int(t/np.pi) if t % np.pi == 0 else int(t/(np.pi/4))/4}π" if t != 0 else "0"
        for t in np.arange(-3 * np.pi, 3 * np.pi + np.pi / 4, np.pi / 4)
    ],
)

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)


plt.show()
