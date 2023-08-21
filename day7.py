#treemap using python

import plotly.graph_objects as go


fig = go.Figure(go.Treemap(
    labels = ["Eve", "Cain", "Seth", "Enos"],
    parents = ["", "Eve", "Eve", "Seth"]))

fig.show()
    