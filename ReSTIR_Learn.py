import numpy as np
import matplotlib.pyplot as plt


def gt_f(x):
    g1 = 10 * np.exp(-((x - 0.2) ** 2) / (2 * 0.05**2))
    g2 = 5 * np.exp(-((x - 0.8) ** 2) / (2 * 0.1**2))
    return g1 + g2


def mis_f(x):
    return x + 1


def ris_f(x):
    return x + 2


gt_x = np.linspace(0, 1, 1000)
gt_y = gt_f(gt_x)

mis_x = np.linspace(0, 1, 1000)
mis_y = mis_f(mis_x)

ris_x = np.linspace(0, 1, 1000)
ris_y = ris_f(ris_x)

fig, ax = plt.subplots(figsize=(8, 3.5))

ax.plot(gt_x, gt_y, color="orange", linewidth=2, label="GT")
ax.plot(mis_x, mis_y, color="red", linewidth=2, label="MIS")
ax.plot(ris_x, ris_y, color="blue", linewidth=2, label="RIS")

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.2, 11)
ax.legend(frameon=True, loc="upper right")
ax.grid(False)

plt.tight_layout()
plt.show()
