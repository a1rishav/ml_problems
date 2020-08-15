import matplotlib.pyplot as plt #plotting
import numpy as np
import pandas as pd
import seaborn as sns #plotting
import pickle
from sklearn import datasets
from sklearn import manifold
from clustering.mnist_clustering.conf.mnist_props import MnistProps as props
import os

from file_utils import FileUtils

'''
1. download mnist data set using datasets.openml --> mnist_784
2. we save the dataset object to save network download everytime
3. The data set has pixel_values, target
    - pixel_values --> (70000,784) --> (70000, 28 * 28)   
    - target --> 700000 labels saying which number 28 * 28 image represents 
4. See a single image --> save it as sample_image.jpg
'''

data_set_path =  os.path.join(props.data_dir, "mnist_dataset.pkl")
if not FileUtils.does_file_exists(data_set_path):
    data = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
    FileUtils.save_to_file(data, data_set_path)
else:
    data = FileUtils.load_from_file(data_set_path)
# pickle.dumps()

pixel_values, target = data
'''
    - mnist dataset contains handwritten images of numbers
    - pixel_values contains pixel values of image
    - pixel_values.shape = (70000,784) --> 70000 images of handwritten numbers 28*28 
        - target contains the number represented by image
        - len(target) --> 70000
    - tsne --> dimensionality reduction to reduce the 784 columns to 2, helps in plotting
    - 
'''

target = target.astype(int)
single_image = pixel_values[1, :].reshape(28, 28)
plt.savefig(os.path.join(props.data_dir, 'single_image.png'), format='png')
# plt.imshow(single_image, cmap='gray')
# plt.show()

# using tsne
tsne = manifold.TSNE(n_components=2, random_state=42)
transformed_data = tsne.fit_transform(pixel_values[:3000, :])
# pixel_values[:3000, :].shape --> (3000, 784)
tsne_df = pd.DataFrame(np.column_stack((transformed_data, target[:3000])), columns =["x", "y", "targets"])
# tsne_df shape (3000, 3)
# x, y, target
tsne_df.loc[:, "targets"] = tsne_df.targets.astype(int)
grid = sns.FacetGrid(tsne_df, hue="targets", size = 8)
grid.map(plt.scatter, "x", "y").add_legend()
plt.savefig(os.path.join(props.data_dir, 'mnist_clsuters.png'), format='png')
