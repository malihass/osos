import pandas as pd
from prettyPlot.plotting import plt, pretty_labels
import matplotlib.dates as mdates
import numpy as np

#,clones,clones_unique,views,views_unique,issues_closed,issues_open,pulls_closed,pulls_open,forks,stargazers,subscribers,contributors,commits,total_commits,updated_on

begin_date = "2023-10-01"

repos_dat = {"BiRD": "../data/bioreactordesign.csv", "PelePhysics": "../data/pelephysics.csv", "PINNSTRIPES": "../data/pinnstripes.csv", "Sup3r": "../data/sup3r.csv"}


for repo in repos_dat:
    A=np.genfromtxt(repos_dat[repo], delimiter=",", usemask=True, dtype=str)
    Ai=np.genfromtxt(repos_dat[repo], delimiter=",", usemask=True)
    ind_date = 0
    date_beg_index = np.argwhere(A[:,ind_date] >= begin_date)[0][0]
    print(f"Repo {repo} since {A[date_beg_index,0]}")
    try:
        ind_clones_unique = np.argwhere(A.data[0,:] == "clones_unique")[0][0]
        clone_unique=Ai[date_beg_index:,ind_clones_unique]
        print(f"\tclones unique = {int(np.sum(clone_unique))}")
    except IndexError:
        pass
    try:
        ind_clones = np.argwhere(A.data[0,:] == "clones")[0][0]
        clone=Ai[date_beg_index:,ind_clones]
        print(f"\tclones = {int(np.sum(clone))}")
    except IndexError:
        pass
    try:
        ind_views = np.argwhere(A.data[0,:] == "views")[0][0]
        view=Ai[date_beg_index:,ind_views]
        print(f"\tviews = {int(np.sum(view))}")
    except IndexError:
        pass
    try:
        ind_views_unique = np.argwhere(A.data[0,:] == "views_unique")[0][0]
        view_unique=Ai[date_beg_index:,ind_views_unique]
        print(f"\tviews unique = {int(np.sum(view_unique))}")
    except IndexError:
        pass
    try:
        ind_pypi = np.argwhere(A.data[0,:] == "pypi_daily")[0][0]
        pypi=Ai[date_beg_index:,ind_pypi]
        print(f"\tpypi downloads = {int(np.sum(pypi))}")
    except IndexError:
        pass
