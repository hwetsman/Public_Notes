An ensemble supervised learning classifier that uses a forest of trees that can differ in one of two ways. The sub-sample 
size is controlled with the `max_samples` parameter if `bootstrap=True` (default), otherwise the whole dataset is used to 
build each tree. You can vary parameters and RF averages the weightings or you can vary features and RF averages those 
weightings from the various trees. 

## Parameters

`n_estimators=100` - the number of trees in the forest
criterion='gini' or 'entropy' - this effects the trees themselves
max_depth=None - effects the trees
min_samples_split=2 - effects the trees 
min_samples_leaf=1 - tree level
min_weight_fraction_leaf=0.0 - tree level
max_features='auto' - how many features to consider in each tree int=number, float = % of features
max_leaf_nodes=None - if you want to limit number of leaf nodes
min_impurity_decrease=0.0 - sets a limit on not using a cut if it won't help by a certain amount
bootstrap=True - otherwise, the whole data set is used for each tree
oob_score=False - 
n_jobs=None - default is one, -1 is number of processors
random_state=None - set random seed for reproducability 
verbose=0 - controls verbosity
warm_start=False - default starts each from scratch, True uses last run to prestart new with additions
class_weight=None - 'balanced' makes an estimate based on N of samples and N of classes, 'balanced_subsample' gives each tree
its own weighting system.
ccp_alpha=0.0 - parameter for pruning
max_samples=None - if bootstrap is True, the number of samples to include in each tree.

`from sklearn.ensemble import RandomForestClassifier`
`from sklearn.datasets import make_classification`
`X, y = make_classification(n_samples=1000, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)`
`clf = RandomForestClassifier(max_depth=2, random_state=0)`
`clf.fit(X, y)`

`pred = clf.predict(test_features)`

`from sklearn.metrics import accuracy_score
`acc = accuracy_score(pred, labels_test)`
