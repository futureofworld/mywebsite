""" Main Page for machine learning.
Collection of all the algorithm and dashbord related to ml"""

from dash import html, register_page
import dash_bootstrap_components as dbc
from components.sidebar import sidebar

register_page(__name__, path='/ml')

layout = html.Div(dbc.Row([sidebar, html.H1("ML Page")], style={'flex-wrap': 'inherit', 'margin': '0px'}))