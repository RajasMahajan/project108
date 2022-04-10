import pandas as pd
import plotly.figure_factory as ff
import csv

dataone = pd.read_csv("data.csv")

fig = ff.create_distplot([dataone["Avg Rating"].tolist()],["avg rating"], show_hist = False)
fig.show()