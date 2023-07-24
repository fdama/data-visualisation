import plotly.graph_objects as go
from random_walk import RandomWalk

walk = RandomWalk()
walk.fill_walk()

fig = go.Figure(data=go.Scatter(x=walk.x_vals, y=walk.y_vals))
fig.show()
