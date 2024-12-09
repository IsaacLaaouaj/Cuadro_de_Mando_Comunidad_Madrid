
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

# Inicialización de la aplicación
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Mapa de Calor de Madrid"

# Simulación de datos para el ejemplo
np.random.seed(42)
data = {
    "lat": np.random.uniform(40.35, 40.50, 500),  # Coordenadas de Madrid
    "lon": np.random.uniform(-3.85, -3.60, 500),
    "intensidad": np.random.randint(1, 100, 500),  # Intensidad del mapa de calor
    "categoria": np.random.choice(["Tráfico", "Contaminación", "Zonas verdes"], 500)
}
df = pd.DataFrame(data)

# Layout de la aplicación
app.layout = dbc.Container([
    html.H1("Visualización de Mapa de Calor de Madrid", className="text-center my-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Selecciona la categoría:"),
            dcc.Dropdown(
                id="filtro-categoria",
                options=[
                    {"label": "Tráfico", "value": "Tráfico"},
                    {"label": "Contaminación", "value": "Contaminación"},
                    {"label": "Zonas verdes", "value": "Zonas verdes"},
                    {"label": "Todas", "value": "Todas"},
                ],
                value="Todas",
                clearable=False
            )
        ], width=4)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="mapa-calor", style={"height": "70vh"})
        ])
    ])
], fluid=True)

# Callback para actualizar el mapa de calor
@app.callback(
    Output("mapa-calor", "figure"),
    [Input("filtro-categoria", "value")]
)
def actualizar_mapa(categoria):
    if categoria == "Todas":
        df_filtrado = df
    else:
        df_filtrado = df[df["categoria"] == categoria]

    # Crear el mapa de calor
    fig = px.density_mapbox(
        df_filtrado,
        lat="lat",
        lon="lon",
        z="intensidad",
        radius=10,
        center={"lat": 40.4168, "lon": -3.7038},  # Centro en Madrid
        zoom=11,
        mapbox_style="carto-positron",
        title=f"Mapa de Calor - {categoria}"
    )

    return fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
