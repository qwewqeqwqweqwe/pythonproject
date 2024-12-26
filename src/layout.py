from dash import dcc, html

def create_layout(app):
    return html.Div([
        html.H1(
            "Планировщик путешествия с погодой",
            style={"textAlign": "center", "color": "#E30613", "marginBottom": "20px"}
        ),

        html.Div([
            html.Label("Введите город старта", style={"fontWeight": "bold"}),
            dcc.Input(
                id="start-point",
                type="text",
                placeholder="Введите город старта",
                style={"width": "100%", "marginBottom": "10px"}
            ),

            html.Label("Введите город достижения", style={"fontWeight": "bold"}),
            dcc.Input(
                id="end-point",
                type="text",
                placeholder="Введите город достижения",
                style={"width": "100%", "marginBottom": "10px"}
            ),

            html.Label("Введите промежуточные города (через запятую)", style={"fontWeight": "bold"}),
            dcc.Input(
                id="stops",
                type="text",
                placeholder="Введите через запятые",
                style={"width": "100%", "marginBottom": "10px"}
            ),

            html.Button(
                "Показать погоду",
                id="submit-button",
                n_clicks=0,
                style={
                    "backgroundColor": "#E30613",
                    "color": "white",
                    "border": "none",
                    "padding": "10px 20px",
                    "cursor": "pointer",
                    "marginTop": "10px"
                }
            )
        ], style={"marginBottom": "20px"}),

        html.Div([
            html.Label("Выберете метрику:", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="parameter-dropdown",
                options=[
                    {"label": "Температура", "value": "temperature"},
                    {"label": "Скорость ветра", "value": "wind_speed"}
                ],
                value="temperature",
                clearable=False,
                style={"width": "50%", "marginBottom": "20px"}
            ),
        ]),
            html.Div([
            html.Label("Выберете промежуток:", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="days-dropdown",
                options=[
                    {"label": "5 дней", "value": 5},
                ],
                value=5,
                clearable=False,
                style={"width": "50%", "marginBottom": "20px"}
            ),
        ]),
        html.Div(id="message-container", style={"color": "red", "marginBottom": "20px"}),
        html.Div(
            id="weather-graphs-container",
            style={"marginTop": "20px"}
        )
    ])