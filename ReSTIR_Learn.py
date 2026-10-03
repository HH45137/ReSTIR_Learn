import matplotlib.pyplot as plt
import numpy as np

GT_STEP = 512
APR_STEP = 64

rng = np.random.default_rng(seed=1919)


def gt_f(x):
    g1 = 0.8 * np.exp(-((x - 0.2) ** 2) / (2 * 0.05**2))
    g2 = 0.6 * np.exp(-((x - 0.8) ** 2) / (2 * 0.1**2))
    return 0.01 + g1 + g2


def uf_f(x):
    return rng.uniform(high=1, low=0, size=np.asarray(x).shape)


def mis_f(x):
    return rng.uniform(high=1, low=0, size=np.asarray(x).shape)


def ris_f(x):
    return rng.uniform(high=1, low=0, size=np.asarray(x).shape)


def prepare_bar_data(edges, gt_x):
    apr_x = (edges[:-1] + edges[1:]) / 2
    uf_y_raw = uf_f(gt_x)

    uf_y_bar = np.array(
        [
            np.mean(uf_y_raw[(gt_x >= edges[i]) & (gt_x < edges[i + 1])])
            for i in range(len(edges) - 1)
        ]
    )

    return apr_x, [
        (uf_y_bar, "red", "Uniform"),
        (mis_f(apr_x), "green", "MIS"),
        (ris_f(apr_x), "blue", "RIS"),
    ]


def plot_combined_comparisons(gt_x, gt_y, apr_x, bar_configs, bar_width):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)

    for ax, (y_bar, color, label) in zip(axes, bar_configs):
        ax.plot(gt_x, gt_y, color="orange", linewidth=2, label="GT")

        ax.bar(
            apr_x,
            y_bar,
            width=bar_width,
            align="center",
            color=color,
            alpha=0.6,
            edgecolor="none",
            label=label,
        )

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.2)
        ax.legend(loc="upper right")
        ax.grid(False)

    plt.tight_layout()
    plt.show()


def main():
    gt_x = np.linspace(0, 1, GT_STEP)
    gt_y = gt_f(gt_x)

    apr_edges = np.linspace(0, 1, APR_STEP + 1)
    bar_width = 1.0 / APR_STEP

    apr_x, bar_configs = prepare_bar_data(apr_edges, gt_x)
    plot_combined_comparisons(gt_x, gt_y, apr_x, bar_configs, bar_width)


if __name__ == "__main__":
    main()
