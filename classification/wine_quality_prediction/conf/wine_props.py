import os
from app_props import AppProps


class WineProps(AppProps):
    wine_classification_home = os.path.join(AppProps.app_home, "classification", "wine_quality_prediction")
    data_dir = os.path.join(wine_classification_home, "data")
