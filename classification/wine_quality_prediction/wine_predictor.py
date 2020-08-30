import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn import metrics

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
# get size and shape
print("Shape of dataset : {}, Size : {}".format(df.shape, df.size))

# get unique sorted values of target
uniqe_targets = df['quality'].unique().tolist()
uniqe_targets.sort()
print("targets : {}".format(uniqe_targets))

# historgram of wine qualities
df.hist('quality')
# plt.show()
plt.savefig(os.path.join(props.data_dir, 'wine_quality_hist.png'), format='png')

# map quality
quality_mapping = {
    3 : 0,
    4 : 1,
    5 : 2,
    6 : 3,
    7 : 4,
    8 : 5,
}

df.loc[:, 'quality'] = df.quality.map(quality_mapping)

# see the affect of columns
MlUtils.corrplot(df)
plt.savefig(os.path.join(props.data_dir, 'wine_params_corr.png'), format='png')

# Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

# Split dataset
df_train = df.head(1000)
df_test = df.tail(599)

# Train model dataset
classifier = tree.DecisionTreeClassifier(max_depth=3)

# Train model dataset
feature_cols = df.columns.tolist()
feature_cols.remove('quality')
classifier.fit(df_train[feature_cols], df_train.quality)

# generate predictions on training set
train_predictions = classifier.predict(df_train[feature_cols])

# generate predictions on test set
test_predictions = classifier.predict(df_test[feature_cols])

# calculate train & test accuracy
train_accuracy = metrics.accuracy_score(df_train.quality, train_predictions)
test_accuracy = metrics.accuracy_score(df_test.quality, test_predictions)

print("Train accuracy : {}".format(train_accuracy))
print("Test accuracy : {}".format(test_accuracy))

matplotlib.rc('xtick', labelsize=20)
matplotlib.rc('ytick', labelsize=20)

train_accuracies = [0.5]
test_accuracies = [0.5]

# test different depth of decision tres
# hold out cross validation
for depth in range(1, 30):
    # train
    classifier = tree.DecisionTreeClassifier(max_depth=depth)
    classifier.fit(df_train[feature_cols], df_train.quality)

    # predict
    train_predictions = classifier.predict(df_train[feature_cols])
    test_predictions = classifier.predict(df_test[feature_cols])

    # store accuracies
    train_accuracy = metrics.accuracy_score(df_train.quality, train_predictions)
    test_accuracy = metrics.accuracy_score(df_test.quality, test_predictions)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
plt.plot(train_accuracies, label="train_accuracy")
plt.plot(test_accuracies, label="test_accuracy")
plt.legend(loc="upper left", prop={'size' : 15})
plt.xticks(range(0, 26, 5))
plt.xlabel("max_depth", size=20)
plt.xlabel("accracy", size=20)
# plt.show()
plt.savefig(os.path.join(props.data_dir, 'decision_tree_accuracy_vs_depth.png'), format='png')
'''
observation :
Even if the depth is set to 100, the test accuracy doesn't go down, had it been neural network
the test accuracy would have increased 
'''
