from dash import html
import dash_bootstrap_components as dbc

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
main = dbc.Container([ml, dl, rl])