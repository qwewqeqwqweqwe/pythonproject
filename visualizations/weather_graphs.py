import plotly.graph_objs as go
from dash import dcc
import plotly.graph_objs as go


def generate_weather_graphs(weather_data, parameter):
    graphs = []
    parameter_mapping = {
        "temperature": "Температура",
        "wind_speed": "Скорость ветра"
    }

    for location, data in weather_data.items():
        days = [day['Date'] for day in data['DailyForecasts']]
        
        if parameter == "temperature":
            values = [day['Temperature']['Maximum']['Value'] for day in data['DailyForecasts']]
            y_label = "Температура (°C)"
        elif parameter == "wind_speed":
            values = [day['Day']['Wind']['Speed']['Value'] for day in data['DailyForecasts']]
            y_label = "Скорость ветра (км/ч)"

        fig = go.Figure(data=[
            go.Scatter(x=days, y=values, mode='lines+markers', name=f'{location}')
        ])
        fig.update_layout(
            title=f"{parameter_mapping[parameter]} Прогноз для {location}",
            xaxis_title="Дни",
            yaxis_title=y_label
        )

        graph_component = dcc.Graph(
            figure=fig,
            id=f"weather-graph-{location.replace(' ', '_')}"
        )
        graphs.append(graph_component)
    return graphs