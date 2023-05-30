""" Main Page for machine learning.
Collection of all the algorithm and dashbord related to ml"""

from dash import html, register_page, callback, Input, Output, State
import dash_bootstrap_components as dbc
from components.sidebar import sidebar

register_page(__name__, path='/ml')

content = dbc.Container([
    html.H1("Hello Machine Learning", style={'paddingTop':'300px', 'paddingBottom': '300px'}),
    html.H2("Hello Deep Learning", style={'paddingTop':'300px', 'paddingBottom': '300px'})
])

layout = html.Div([sidebar(), content])