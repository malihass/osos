import pandas as pd
from prettyPlot.plotting import plt, pretty_labels
import matplotlib.dates as mdates
import numpy as np

# ,clones,clones_unique,views,views_unique,issues_closed,issues_open,pulls_closed,pulls_open,forks,stargazers,subscribers,contributors,commits,total_commits,updated_on

A = np.genfromtxt("../data/pinnstripes.csv", delimiter=",", usemask=True, dtype=str)
Ai = np.genfromtxt("../data/pinnstripes.csv", delimiter=",", usemask=True)
date = pd.to_datetime(A[1:, 0])

date_github_index = np.argwhere(A[:, 0] == "2023-10-30")[0][0] - 1
date_arxiv_index = np.argwhere(A[:, 0] == "2023-12-28")[0][0] - 1

ind_clones_unique = np.argwhere(A.data[0,:] == "clones_unique")[0][0]
ind_clones = np.argwhere(A.data[0,:] == "clones")[0][0]
ind_views_unique = np.argwhere(A.data[0,:] == "views_unique")[0][0]
ind_views = np.argwhere(A.data[0,:] == "views")[0][0]
clone_unique=Ai[1:,ind_clones_unique]
clone=Ai[1:,ind_clones]
view=Ai[1:,ind_views]
view_unique=Ai[1:,ind_views_unique]

days = np.array(list(range(1, Ai[1:, :].shape[0] + 1)))

size = 16
# arrowprops = dict(arrowstyle='-|>')
arrowprops = None

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
y = np.cumsum(clone)
plt.plot(date, np.cumsum(clone))
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
# plt.annotate('Arxiv upload', (mdates.date2num(date[date_arxiv_index]), view[date_arxiv_index]), xytext=(0, view[date_arxiv_index]+), textcoords='offset points', arrowprops=arrowprops)
pretty_labels("", "clones", size, grid=False)
plt.tight_layout()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.plot(date, np.cumsum(view), linewidth=3, color="k")
y = np.cumsum(view)
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.plot(
    mdates.date2num(date[date_github_index]),
    y[date_github_index],
    "o",
    markersize=15,
    color="r",
)
plt.plot(
    mdates.date2num(date[date_arxiv_index]),
    y[date_arxiv_index],
    "o",
    markersize=15,
    color="r",
)
pretty_labels(
    "",
    "views",
    size,
    title=f"# views = {np.cumsum(view)[-1]}, # clones = {np.cumsum(clone)[-1]}",
    grid=False,
)
plt.tight_layout()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.plot(date, np.cumsum(clone_unique))
y = np.cumsum(clone_unique)
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
pretty_labels("", "clones unique", size, grid=False)
plt.tight_layout()


fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.plot(date, np.cumsum(view_unique), color="k", linewidth=3)
y = np.cumsum(view_unique)
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -10),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.plot(
    mdates.date2num(date[date_github_index]),
    y[date_github_index],
    "o",
    markersize=15,
    color="r",
)
plt.plot(
    mdates.date2num(date[date_arxiv_index]),
    y[date_arxiv_index],
    "o",
    markersize=15,
    color="r",
)
pretty_labels(
    "",
    "views unique",
    size,
    title=f"# views = {int(np.cumsum(view)[-1]):d}, # clones = {int(np.cumsum(clone)[-1]):d}",
    grid=False,
)
plt.tight_layout()


fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.plot(date, np.cumsum(view_unique) / days)
y = np.cumsum(view_unique) / days
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
pretty_labels("", "views unique per day", size, grid=False)
plt.tight_layout()


fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.plot(date, np.cumsum(clone_unique) / days)
y = np.cumsum(clone_unique) / days
plt.xticks(date, rotation=90)
old = None
for il, label in enumerate(ax.xaxis.get_ticklabels()):
    if old is None or not label.get_text() == old:
        label.set_visible(True)
        old = label.get_text()
    else:
        label.set_visible(False)
plt.annotate(
    "Github upload",
    (mdates.date2num(date[date_github_index]), y[date_github_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
plt.annotate(
    "arXiv upload",
    (mdates.date2num(date[date_arxiv_index]), y[date_arxiv_index]),
    xytext=(10, -15),
    textcoords="offset points",
    arrowprops=arrowprops,
    fontsize=size,
    font="serif",
    weight="bold",
)
pretty_labels("", "clones unique per day", size, grid=False)
plt.tight_layout()


plt.show()
