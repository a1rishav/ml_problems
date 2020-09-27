## ML concepts

### Supervised : always has one or multiple target
- Regression : predicting a value
- Classification : predicting a category

### Un Supervised : does not have any target
- Example : Credit Fraud detection 
- important appproaches :
  - clustering
  - PCA
  - t-SNE

### Cross Validation : ensures that the model fits and does not overfit, used so that validation data is representative of train data
- k fold cross validation
  - can be used with all kind of datasets
  - splits any dataest into k folds
- stratified k fold cross validation
  - when data set is skewed (examples 90% ppositive samples, 10% negative samples)
  - keeps the ratio of labels in each fold constant
  - if it's a standard classification problem, choose it blindly
  - in regression problem, data size (>10k, >100k) idrectly choose 10 or 20 bins else **Sturges Rule : bins = 1 + log 2(N)**
- hold out based validation
  - mainly used with time series data, example, to predict sales 0f 2020, train (2015-2018), 2019 data is hold out(to check performance like test set)
		- 
- leave one out cross validation
- group k-fold cross validation
	

