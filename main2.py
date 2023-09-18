from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from functions import *
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


#* Data
df_main = load_csv()
df_main = clean_columns(df_main)
df_dates, country_list = df_dates(df_main)
df_info = country_info(df_main)


app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

#app.litle = "World Population Dashboard"

app.layout = dbc.Container([

    dbc.Row([
        html.H1("World Population"),
        html.Hr()
    ]),
    dbc.Row([
        dash_table.DataTable(data=df_main.to_dict('records'), page_size=10, style_table={'overflowX': 'auto'}),
        dbc.Alert("This is a division called 'Alert' which can be modified with differents colors", color="info")
    ]),
    dbc.Row([
        html.Hr(),
        html.H3("Population over time by Country"),
        dcc.Dropdown(country_list, 'Afghanistan',id='dropdown_selection'),
        dcc.Graph(id='graph-content-wp')
    ]),
    dbc.Row([
        html.Hr(),
        html.H3("Population by Continent"),
        dbc.Col([
            dcc.Graph(id='graph-pie')]),
        dbc.Col([
            dcc.Graph(id='graph-pie2')])
    ]),
    dbc.Row([
        html.Hr(),
        html.H3("Information by Continent"),
        html.H3(""),
        dcc.RadioItems(options=['Area[km2]', 'Density[Km2]', 'World_Population_Percentage'], value='Density[Km2]', id='controls_item',
        labelStyle= {"margin":"2rem"}, style = {'display': 'flex'}),
    ]),
    dbc.Row([
        html.H3(""),
        dcc.Graph(id='graph-content-pbc')
    ]),
    dbc.Row([
        html.Hr(),
        html.H3("Treemap Density[Km2]"),
        dcc.Graph(id='graph-content-tree')
    ]),
]
    ,fluid=True
)

@callback(
    Output('graph-content-wp', 'figure'),
    Output('graph-pie','figure'),
    Output('graph-pie2','figure'),
    Output('graph-content-pbc', 'figure'),
    Output('graph-content-tree', 'figure'),
    Input('dropdown_selection', 'value'),
    Input('controls_item','value')
)

def update_graph(dropdown_selection, controls_item):
    fig_line = px.line(df_dates, x=df_dates['Year'], y=dropdown_selection)
    fig_pie = px.pie(df_main, values='Population_2022', names='Continent', hole=0.3, title='Population on 2022')
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie_2 = px.pie(df_main, values='Area[km2]', names='Continent', hole=0.3, title='Area[Km²]')
    fig_pie_2.update_traces(textposition='inside', textinfo='percent+label')
    fig_bar = px.bar(df_main, x='Continent', y=controls_item, color='Continent')
    fig_tree = px.treemap(df_main, path=[px.Constant('world'), 'Continent', 'Country'], values='Density[Km2]')
    fig_tree.update_traces(root_color='lightgrey')
    return fig_line, fig_pie, fig_pie_2, fig_bar, fig_tree

if __name__ == "__main__":
    app.run_server(debug=True)

