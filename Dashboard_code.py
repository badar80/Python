import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Load data from CSV file
df = pd.read_csv(r'C:\Users\badar\Downloads\Top250.csv')  # Replace with your actual file name

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Restaurant Dashboard"),

    dcc.Dropdown(
        id='dropdown-column',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Sales'  # Default selected column
    ),

    dcc.Graph(id='bar-plot'),
])


# Define callback to update bar plot based on dropdown selection
@app.callback(
    Output('bar-plot', 'figure'),
    [Input('dropdown-column', 'value')]
)
def update_graph(selected_column):
    # Create a bar plot
    fig = {
        'data': [
            {'x': df['Restaurant'], 'y': df[selected_column], 'type': 'bar', 'name': selected_column},
        ],
        'layout': {
            'title': f'{selected_column} Bar Plot',
            'xaxis': {'title': 'Restaurant'},
            'yaxis': {'title': selected_column},
        }
    }
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)