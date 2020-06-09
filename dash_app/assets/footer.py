import dash_bootstrap_components as dbc
import dash_html_components as html

def get_footer():
    return html.Div(children=[
        html.Footer(children="@ 2020 Patraporn Leelaprachakul"),
    ], style={'padding': '20px'})
