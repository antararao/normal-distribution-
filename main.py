import pandas as pd 
import plotly.figure_factory as ff 

read = pd.read_csv("data.csv")
fig = ff.create_distplot([read["Avg Rating"].tolist()], ["Average Rating"])
fig.show()
