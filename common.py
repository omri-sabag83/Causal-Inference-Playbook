"""Shared loaders, chart settings and table printing for every module.

load_lalonde()  NSW treated units plus a comparison group ("experimental", "psid" or "cps"), Modules 1-6
show()          print a table with text columns left-aligned, numbers right-aligned
draw_dag()      draw a causal diagram (boxes and arrows) on a matplotlib axis, Module 2 onwards
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"

# Chart palette: reference categorical slots (same as the earlier playbooks).
BLUE, ORANGE, AQUA, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#888888"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.25, "figure.dpi": 110})

# Every chart image gets a thin black frame (shared with the other repos: chart_style.py).
import chart_style  # noqa: E402,F401

# The randomized NSW estimate on the Dehejia-Wahba sample: treated minus control mean 1978 earnings.
BENCHMARK_ATT = 1794.3


def _need(name: str) -> Path:
    path = RAW / name
    if not path.exists():
        raise FileNotFoundError(f"{path} missing: run `python data/get_data.py` first.")
    return path


def load_lalonde(controls: str = "psid") -> pd.DataFrame:
    """NSW treated units (185) plus one comparison group.

    controls="experimental": the randomized NSW controls (260), the benchmark
    controls="psid" or "cps": a non-experimental survey sample, the observational setting
    """
    nsw = pd.read_stata(_need("nsw_dw.dta"))
    if controls == "experimental":
        df = nsw.copy()
    else:
        ctrl = pd.read_stata(_need(f"{controls}_controls.dta"))
        df = pd.concat([nsw[nsw.treat == 1], ctrl], ignore_index=True)
    df["treat"] = df["treat"].astype(int)
    return df.drop(columns="data_id")


def show(df: pd.DataFrame, index: bool = False) -> None:
    """Print a table with text columns left-aligned and numeric columns right-aligned."""
    import re
    if index:
        df = df.reset_index()
    numeric = re.compile(r"^[-+−]?[\d,]*\.?\d+%?$")
    cols = [str(c) for c in df.columns]
    cells = [[str(v) for v in df[c]] for c in df.columns]
    blank = {"n/a", "no data", "—", ""}
    is_text = [not all(numeric.match(v) or v in blank for v in col) or all(v in blank for v in col) for col in cells]
    widths = [max([len(h)] + [len(v) for v in col]) for h, col in zip(cols, cells)]
    pad = lambda s, w, left: s.ljust(w) if left else s.rjust(w)
    print("  ".join(pad(h, w, t) for h, w, t in zip(cols, widths, is_text)).rstrip())
    for r in range(len(df)):
        print("  ".join(pad(col[r], w, t) for col, w, t in zip(cells, widths, is_text)).rstrip())


def draw_dag(ax, nodes: dict, edges: list, title: str = "", dashed: tuple = (), colors: dict | None = None) -> None:
    """Draw a causal diagram: nodes = {name: (x, y)}, edges = [(from, to), ...].

    dashed: names of unmeasured nodes (dashed box). colors: {name: box colour}.
    """
    from matplotlib.patches import FancyArrowPatch
    colors = colors or {}
    boxes = {}
    for name, (x, y) in nodes.items():
        boxes[name] = ax.text(x, y, name, ha="center", va="center", fontsize=9, zorder=3,
                              bbox=dict(boxstyle="round,pad=0.4", fc=colors.get(name, "white"), ec="black",
                                        lw=1, ls="--" if name in dashed else "-"))
    for a, b in edges:
        # Clip each arrow to the two boxes' edges, so arrowheads are never hidden behind a box.
        ax.add_patch(FancyArrowPatch(nodes[a], nodes[b], arrowstyle="-|>", mutation_scale=14, lw=1.2,
                                     color="black", patchA=boxes[a].get_bbox_patch(), patchB=boxes[b].get_bbox_patch(),
                                     shrinkA=2, shrinkB=2, zorder=4, ls="--" if a in dashed or b in dashed else "-"))
    xs, ys = zip(*nodes.values())
    ax.set_xlim(min(xs) - 0.8, max(xs) + 0.8)
    ax.set_ylim(min(ys) - 0.6, max(ys) + 0.6)
    ax.set_title(title, fontsize=10)
    ax.axis("off")
