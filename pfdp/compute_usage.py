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
    date_beg_index = np.argwhere(A[:,0] >= begin_date)[0][0]
    print(f"Repo {repo} since {A[date_beg_index,0]}")
    clone_unique=Ai[date_beg_index:,2]
    print(f"\tclones unique = {int(np.sum(clone_unique))}")
    clone=Ai[date_beg_index:,1]
    print(f"\tclones = {int(np.sum(clone))}")
    view=Ai[date_beg_index:,3]
    print(f"\tviews = {int(np.sum(view))}")
    view_unique=Ai[date_beg_index:,4]
    print(f"\tviews unique = {int(np.sum(view_unique))}")
    if Ai.shape[1]>=18:
        pypi=Ai[date_beg_index:,15]
        print(f"\tpypi downloads = {int(np.sum(pypi))}")
   
   
