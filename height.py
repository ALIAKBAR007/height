import csv 
import plotly.figure_factory as pf
import pandas as pd

file = pd.read_csv("c108.csv")

hl=file["Height(Inches)"].to_list()
Wl=file["Weight(Pounds)"].to_list()

fig=pf.create_distplot([hl],["xyz"])
fig.show()