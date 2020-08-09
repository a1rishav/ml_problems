import os
from app_props import AppProps


class MnistProps(AppProps):
    mnist_clustering_home = os.path.join(AppProps.app_home, "clustering", "mnist_clustering")
    data_dir = os.path.join(mnist_clustering_home, "data")
