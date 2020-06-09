import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
from .assets import header, footer

from dash.dependencies import Input, Output
from data_analysis import *

TOPIC = "#BlackLivesMatter"
df = pd.read_csv('https://raw.githubusercontent.com/pleelapr/twitter-analysis-on-dash/master/data/cleaned_data.csv')


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(__name__, server=server,
                         url_base_pathname='/app/',
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Create Dash Layout
    dash_app.layout = html.Div(id='dash-container')
    dash_app.layout = html.Div(children=[
        header.navBar,
        header.get_header('Twitter Analysis on ' + TOPIC, len(df)),

        # === Tweet Graph and Table
        html.Div([
            html.Label('Rank Tweet By'),
            dcc.Dropdown(
                id='select-rank-tweet-by',
                options=[
                    {'label': 'Count of Tweets', 'value': 'text'},
                    {'label': 'Number of Retweet', 'value': 'retweet_count'}
                ],
                value='text'
            ),
            dcc.Graph(id='live-rank-tweet-graph'),
            html.Div(id="live-rank-tweet-table")
        ], style={'width': '48%', 'display': 'inline-block', 'padding':'20px'}),

        # === User Graph and Table
        html.Div([
            html.Label('Rank User By'),
            dcc.Dropdown(
                id='select-rank-user-by',
                options=[
                    {'label': 'Number of Tweets by User', 'value': 'user'},
                    {'label': 'Number of Followers', 'value': 'user_follower_count'},
                    {'label': 'Number of Favorite', 'value': 'user_favorite_count'},
                    {'label': 'Number of Retweet from the User', 'value': 'retweet_from_user'}
                ],
                value='user'
            ),
            dcc.Graph(id='live-rank-user-graph'),
            html.Div(id="live-rank-user-table")
        ], style={'width': '48%', 'display': 'inline-block', 'padding':'20px'}),

        footer.get_footer(),
    ])

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)


def init_callbacks(dash_app):
    # === Tweets Ranking Graph
    @dash_app.callback(
        Output('live-rank-tweet-graph', 'figure'),
        [Input('select-rank-tweet-by', 'value')]
    )
    def update_graph(select_rank_tweet_by):
        if select_rank_tweet_by == 'text':
            output = get_top_count_by(df, 'text')
        elif select_rank_tweet_by == 'retweet_count':
            output = get_rank_col_by_index_col(df, 'retweet_count', 'text', 10)
        return {
            'data': [
                {'x': output.iloc[:, 0], 'y': output.iloc[:, 1], 'type': 'bar', 'name': 'Count'}
            ],
            'layout': {
                'title': 'Tweet Ranking Table'
            }
        }

    # === Tweets Ranking Table
    @dash_app.callback(
        dash.dependencies.Output("live-rank-tweet-table", "children"),
        [dash.dependencies.Input("select-rank-tweet-by", "value")],
    )
    def update_output(select_rank_tweet_by):
        if select_rank_tweet_by == 'text':
            output = get_top_count_by(df, 'text')
        elif select_rank_tweet_by == 'retweet_count':
            output = get_rank_col_by_index_col(df, 'retweet_count', 'text', 10)
        return dbc.Table.from_dataframe(output, striped=True, bordered=True, hover=True)

    # === User Ranking Graph
    @dash_app.callback(
        Output('live-rank-user-graph', 'figure'),
        [Input('select-rank-user-by', 'value')]
    )
    def update_graph(select_rank_user_by):
        if select_rank_user_by == 'user':
            output = get_top_count_by(df, 'user')
        elif select_rank_user_by == 'retweet_from_user':
            output = get_top_count_by(df, 'retweet_from_user')
        elif select_rank_user_by == 'user_favorite_count':
            output = get_rank_col_by_index_col(df, 'user_favorite_count', 'user', 10)
        elif select_rank_user_by == 'user_follower_count':
            output = get_rank_col_by_index_col(df, 'user_follower_count', 'user', 10)
        return {
            'data': [
                {'x': output.iloc[:, 0], 'y': output.iloc[:, 1], 'type': 'bar', 'name': 'Count'}
            ],
            'layout': {
                'title': 'User Ranking Table'
            }
        }

    # === User Ranking Table
    @dash_app.callback(
        dash.dependencies.Output("live-rank-user-table", "children"),
        [dash.dependencies.Input("select-rank-user-by", "value")],
    )
    def update_output(select_rank_user_by):
        if select_rank_user_by == 'user':
            output = get_top_count_by(df, 'user')
        elif select_rank_user_by == 'retweet_from_user':
            output = get_top_count_by(df, 'retweet_from_user')
        elif select_rank_user_by == 'user_favorite_count':
            output = get_rank_col_by_index_col(df, 'user_favorite_count', 'user', 10)
        elif select_rank_user_by == 'user_follower_count':
            output = get_rank_col_by_index_col(df, 'user_follower_count', 'user', 10)
        return dbc.Table.from_dataframe(output, striped=True, bordered=True, hover=True)
