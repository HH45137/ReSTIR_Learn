import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)


def radiance_f(x):
    g1 = 10 * np.exp(-((x - 0.2) ** 2) / (2 * 0.05**2))
    g2 = 5 * np.exp(-((x - 0.8) ** 2) / (2 * 0.1**2))
    return g1 + g2


y = radiance_f(x)

fig, ax = plt.subplots(figsize=(8, 3.5))

ax.plot(x, y, color="orange", linewidth=2, label="Radiance f(x)")

ax.fill_between(x, y, color="orange", alpha=0.3)

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.2, 11)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend(frameon=True, loc="upper right")
ax.grid(False)

plt.tight_layout()
plt.show()
