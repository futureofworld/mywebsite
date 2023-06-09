""""This file contains Navigation Bar of the App"""

import dash_bootstrap_components as dbc


Navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Machine Learning", href="/ml")),
        dbc.NavItem(dbc.NavLink("Deep Learning", href="/dl")),
        dbc.NavItem(dbc.NavLink("Reinforcement Learning", href="/rl")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More Pages", header=True),
                dbc.DropdownMenuItem("NLP", href="#"),
                dbc.DropdownMenuItem("Time Series Forecasting", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="RahulDhavale",
    brand_href="/",
    color="primary",
    dark=True,
    sticky='top',
)