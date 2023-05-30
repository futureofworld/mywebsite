from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

from components.navbar import Navbar
from components.footer import Footer
# from main import main
from utils import CSS_URL

dbc_css = CSS_URL

app = Dash(
    external_stylesheets=[dbc.themes.DARKLY, dbc_css, dbc.icons.BOOTSTRAP],
    meta_tags=[{"name":"viewport", 
            "content": "width=device-width, intial-scale=1"}],
    use_pages=True,
)

app.layout = html.Div([Navbar, page_container, Footer])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port='8080', debug=True)