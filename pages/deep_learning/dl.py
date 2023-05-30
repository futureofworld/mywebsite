""" Main Page for Deep learning.
Collection of all the algorithm and dashbord related to dl"""

from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/dl')

layout = dbc.Container(html.H1("DL Page"))