
### Using the mobile price prediction dataset from Kaggle
import pandas as pd
import numpy as np

from sklearn import model_selection

df = pd.read_csv('mobile_train.csv')
X = df.drop("price_range", axis =1).values
y=  df.price_range.values

scl = preprocessing.StandardScaler()
pca = decomposition.PCA()

rf = ensemble.RandomForestClassifier(n_jobs=-1)
#classifier = pipeline.Pipeline([("scaling",scl), ("pca", pca), ("rf", rf) ])
classifier = ensemble.RandomForestClassifier(n_jobs=-1)
param_grid = {
        "n_estimators": np.arange(100,1500,100),
        "max_depth": np.arange(1,20),
        "criterion": ["gini", "entropy"],
}

model = model_selection.RandomizedSearchCV(
    estimator = classifier,
    param_distributions = param_grid,
    n_iter =10,
    scoring = "accuracy",
    verbose= 10,
    n_jobs= 1,
    cv=5,)
model.fit(X,y)
print(model.best_score_)
print(model.best_estimator_.get_params())


