import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
df = pd.read_csv('integrated_output.csv')
print(df[:5])

app.layout = html.Div([
    html.H1("DCAsssist",style={'text-align':'center'}),
    html.Br(),
    dcc.Graph(id='graph'),
    html.Button('Change axis',id='btn',n_clicks=0)

])

@app.callback(
    Output("graph", "figure"),
    [Input("btn", "n_clicks")])

def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = 'Case_well_level', 'Di'
    else:
        x, y = 'Di', 'Case_well_level'

    fig = px.bar(df, x=x, y=y)
    
    
    fig.update_layout(barmode='relative',title_text='Case_well_level VS Di')

    return fig
if __name__=='__main__':
   app.run_server(debug=True)




