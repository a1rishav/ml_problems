import pandas as pd
import os

import matplotlib.pyplot as plt
from sklearn import model_selection
from classification.wine_quality_prediction.conf.wine_props import WineProps as props

data_path = os.path.join(props.data_dir, "winequality-red.csv")
df = pd.read_csv(data_path)

df.hist(['quality'])
# plt.show()

df['kfold'] = -1
df = df.sample(frac=1).reset_index(drop=True)
df = df[:100]
kf = model_selection.StratifiedKFold(n_splits=5)

y = df['quality'].values

for fold, (trn_, val_) in enumerate(kf.split(X=df, y=y)):
    df.loc[val_, 'kfold'] = fold
'''
we can see that the frequency distribution of target variable is same in all folds
'''
df[df['kfold'] == 0].hist('quality')
df[df['kfold'] == 1].hist('quality')
df[df['kfold'] == 4].hist('quality')
print()
