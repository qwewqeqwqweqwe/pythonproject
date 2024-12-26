from dash import Dash

from src.layout import create_layout
from src.callbacks import register_callbacks

app = Dash(__name__)
api_key = 'uCoAhGjS5l3SRNeuA4ZkliXGCAaMolv8'
app.title = "Отслеживатель погодных условий"
app.layout = create_layout(app)
register_callbacks(app, api_key)


if __name__ == "__main__":
    app.run_server(debug=True)
