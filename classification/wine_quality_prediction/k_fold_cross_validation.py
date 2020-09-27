import pandas as pd
import os
from sklearn import model_selection

from classification.wine_quality_prediction.conf.wine_props import WineProps as props

data_path = os.path.join(props.data_dir, "winequality-red.csv")
df = pd.read_csv(data_path)

short_df = df[:100]
short_df['kfold'] = -1

short_df = short_df.sample(frac=1).reset_index(drop=True)
kf = model_selection.KFold(n_splits=5)

'''
loop will run for n_splits
val_ is the indices 
    - if there are 10 records
    - fold = 1, val_ = [0, 1]
    - fold = 2, val_ = [2, 3]
    .
    .
    - fold = 5, val_ = [8, 9]
'''

for fold, (trn_, val_) in enumerate(kf.split(X=short_df)):
    short_df.loc[val_, 'kfold'] = fold
    print()

print()