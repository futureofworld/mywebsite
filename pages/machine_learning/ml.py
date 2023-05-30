""" Main Page for machine learning.
Collection of all the algorithm and dashbord related to ml"""

from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/ml')

layout = dbc.Container(html.H1("ML Page"))