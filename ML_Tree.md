````mermaid
flowchart TB
  Machine_Learning(Machine<br>Learning)
  Supervised(Supervised<br>Algorithms)
    Supervised-->Nearest(Nearest<br>Neighbor)
      Machine_Learning--->Supervised
    Nearest --> KNN
    Nearest --> Radius_Neighbors
    Nearest --> Nearest_Centroid
    Supervised --> Decision(Decision<br>Tree)
    Decision --> Bagging
    Decision --> Random_Forest
    Decision --> Adaboost
    Decision --> Gradient_Boosted_Tree
    Supervised --> Linear(Linear<br>Regression)
    Linear --> GLM
    GLM --> GAM
    GLM --> Logistic_Regression
    Logistic_Regression --> Neural_Networks
    Neural_Networks --> Deep_Neural_Networks
    Deep_Neural_Networks --> CNN
    Deep_Neural_Networks --> RNN
    Deep_Neural_Networks --> Transformers
    Linear --> Lasso_Ridge
    Linear --> Elastic_Net
    Linear --> SVM
````
    Unsupervised(Unsupervised<br>Learning)
    Unsupervised--->Data without label
      Machine_Learning--->Unsupervised







   
