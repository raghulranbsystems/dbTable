# # Run this app with `python app.py` and
# # visit http://127.0.0.1:8050/ in your web browser.

# from dash import Dash, html, dcc
# import plotly.express as px
# import pandas as pd

# app = Dash(__name__)

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.read_csv('dbTable.csv')

# fig = px.bar(df, x=df["payment_date"], y=df["amount"],
#              color="amount", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Demo project'),

#     html.Div(children='''
#         Data analysis for payment date and amount.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# fig = px.scatter(df, x=df["payment_date"], y=df["amount"],
#                  size=df["rental_id"], color=df["customer_id"], hover_name=df["staff_id"],
#                  log_x=True, size_max=60)

# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
