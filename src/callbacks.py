from dash import html
from dash.dependencies import Input, Output, State

from services.accuweather_api import get_weather_data
from visualizations.weather_graphs import generate_weather_graphs


def register_callbacks(app, api_key):
    @app.callback(
    Output("weather-graphs-container", "children"),
    [Input("submit-button", "n_clicks"),
     Input("parameter-dropdown","value"),
     Input("days-dropdown", "value")],
    [State("start-point", "value"), State("end-point", "value"), State("stops", "value")],
)
    def update_weather_graphs(n_clicks, parameter, days, start, end, stops):
        if not start or not end:
            return [html.Div("Введите все точки, чтобы показать прогноз", style={"color": "red"})]

        locations = [start, end]
        if stops:
            locations += [stop.strip() for stop in stops.split(",")]
        weather_data = get_weather_data(locations, api_key, days)
        graphs = generate_weather_graphs(weather_data, parameter)
        return graphs