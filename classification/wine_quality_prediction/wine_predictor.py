import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

from classification.wine_quality_prediction.conf.wine_props import WineProps as props
from ml_utils import MlUtils

data_path = os.path.join(props.data_dir, "winequality-red.csv")
df = pd.read_csv(data_path)

# EDA
'''
Features : fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,
           free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol
Target : quality
'''
# get unique sorted values of target
uniqe_targets = df['quality'].unique().tolist().sort()

# historgram of wine qualities
# df.hist('quality')
# plt.show()

# see the affect of columns

MlUtils.corrplot(df)
print()