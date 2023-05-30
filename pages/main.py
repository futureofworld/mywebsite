from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/')

ml = dbc.Row([
    dbc.Col(),  # add machine learning image
    dbc.Col([
        html.H1("Machine Learning", className='dbc'),
        html.P("Machine learning is a branch of Computer Science which gives \
            computer the ability to learn without being explicitly programmed",
            className='dbc'),
    ])
])

dl = dbc.Row([
    dbc.Col([
        html.H1("Deep Learning", className='dbc'),
        html.P("Deep Learning", className='dbc')
    ]),
    dbc.Col()
])

rl = dbc.Row([
    dbc.Col(),  # add reinforcement learning image
    dbc.Col([
        html.H1("Reinforcement Learning", className='dbc'),
        html.P("Reinforcement Learning about",
            className='dbc'),
    ])
])

layout = dbc.Container([ml, dl, rl])