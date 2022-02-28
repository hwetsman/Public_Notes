# Decision Trees (DTs) 
are a non-parametric supervised learning method used for classification and regression. 
The goal is to create a model that predicts the value of a target variable by learning simple decision rules 
inferred from the data features.

## Entropy

Entropy (0-1) with 0 being completely pure sets and 1 being equal numbers of all labels in the set. DTs try to minimize entropy
when they draw lines at which to divide datasets.
sum of all variables of -P(variable) * log2 of P(variable)

## Information Gain

Information gain is defined by the entropy of the parent minus the weighted average of the entropy of the children. 
The way to think about this intuitively is how good the child feature is at decreasing entropy. Remember, entropy has to do
with the labels, so we're really asking with IG how much of the variance is explained by this feature. The feature that has
the greatest information gain, should be the first we use in the algorithm.

## Bias/Variance tension

This actually has to do with all supervised ML. A highly biased algorithm would practically ignore the training data because
it has a BIAS. A high variance algorithm would be very sensitive to training data but would have a problem generalizing if
it was exposed to something that it hadn't been trained on. We don't want either of these, but something in the middle. We
can't have perfect - there's a tension between the two and they tradeoff.

`from sklearn import tree`
`clf = tree.DecisionTreeClassifier()`
`clf = clf.fit(training_features, training_labels)`

`pred = clf.predict(test_features)

`from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)`

The tree can be plotted:
`tree.plot_tree(clf)`
or exported via graphviz
`import graphviz`
`dot_data = tree.export_graphviz(clf, out_file=None)`
`graph = graphviz.Source(dot_data)`
`graph.render("output")`
and the output is saved as output.pdf

Tunable Parameters and defaults:
criterion='gini', 'entropy'
splitter='best', 
max_depth=None, 
min_samples_split=2, 
min_samples_leaf=1, 
min_weight_fraction_leaf=0.0, 
max_features=None, 
random_state=None, 
max_leaf_nodes=None, 
min_impurity_decrease=0.0, 
class_weight=None, 
ccp_alpha=0.0
