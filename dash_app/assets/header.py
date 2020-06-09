import dash_bootstrap_components as dbc
import dash_html_components as html

navBar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard 1", href="#")),
    ],
    brand="Twitter Analysis on Flask-Dash",
    brand_href="#",
    color="primary",
    dark=True, )


def get_header(title, data_size=0):
    if data_size > 0:
        return html.Div(children=[
            html.H1(children=title),
            html.H2(children="Total Number of Tweets : {}".format(data_size)),
        ], style={'padding': '20px'})
    else:
        return html.Div(children=[
            html.H1(children=title),
        ], style={'padding': '20px'})
