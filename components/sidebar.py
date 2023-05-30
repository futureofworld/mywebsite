"""
This app creates an animated sidebar using the dbc.Nav component and some local
CSS. Each menu item has an icon, when the sidebar is collapsed the labels
disappear and only the icons remain. Visit www.fontawesome.com to find
alternative icons to suit your needs!

dcc.Location is used to track the current location, a callback uses the current
location to render the appropriate page content. The active prop of each
NavLink is set automatically according to the current pathname. To use this
feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, State

def sidebar(button_id="open-offcanvas", canvas_id="offcanvas"):
    drawer = html.Div(
        [
            html.Div(
                dbc.Button(
                    "", id=button_id, n_clicks=0, 
                    className='bi bi-three-dots-vertical position-fixed mt-1'
                ), 
                style={'paddingLeft': '4px'}
            ),
            dbc.Offcanvas(
                html.P(
                    "This is the content of the Offcanvas. "
                    "Close it by clicking on the close button, or "
                    "the backdrop."
                ),
                id=canvas_id,
                title="Title",
                is_open=False,
            ),
        ]
    )

    @callback(
        Output(canvas_id, "is_open"),
        Input(button_id, "n_clicks"),
        [State(canvas_id, "is_open")],
    )
    def toggle_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open

    return drawer
