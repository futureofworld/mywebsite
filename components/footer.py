"""This File contain the Footer of the App"""
import dash_bootstrap_components as dbc
from dash import html


Footer = dbc.Nav([
    # Github Icon
    dbc.NavItem(
        dbc.NavLink(
            html.I(className='bi bi-github', style={'fontSize':'1.6rem'}),
            href='https://github.com/futureofworld/mywebsite'
        ), 
        id='github_icon',
    ),
    # On Hover show source code
    dbc.Tooltip("source code", target='github_icon', placement='left'),
    # LinkedIn Icon
    dbc.NavItem(
        dbc.NavLink(
            html.I(className='bi bi-linkedin', style={'fontSize':'1.6rem'}), 
            href='https://www.linkedin.com/in/rahul-dhavale-9181a1213/',
        ), 
        id='linkedin_icon',
    ),
    # On Hover show LinkedIn Profile
    dbc.Tooltip("LinkedIn Profile",target='linkedin_icon',placement='right')
], class_name='justify-content-center sticky-bottom bg-dark',)