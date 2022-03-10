````mermaid
flowchart TB
  Machine_Learning(Machine<br>Learning)
  Supervised(Supervised<br>Algorithms)

    Supervised-->Nearest_Neighbor
    ````
      Machine_Learning--->Supervised
    Nearest_Neighbor --> KNN
    Nearest_Neighbor --> Radius_Neighbors
    Nearest_Neighbor --> Nearest_Centroid
    Supervised_Algorithms --> Decision_Tree
    Decision_Tree --> Bagging
    Decision_Tree --> Random_Forest
    Decision_Tree --> Adaboost
    Decision_Tree --> Gradient_Boosted_Tree
    Supervised_Algorithms --> Linear_Regression
    Linear_Regression --> GLM
    GLM --> GAM
    GLM --> Logistic_Regression
    Logistic_Regression --> Neural_Networks
    Neural_Networks --> Deep_Neural_Networks
    Deep_Neural_Networks --> CNN
    Deep_Neural_Networks --> RNN
    Deep_Neural_Networks --> Transformers
    Linear_Regression --> Lasso_Ridge
    Linear_Regression --> Elastic_Net
    Linear_Regression --> SVM

    Unsupervised(Unsupervised<br>Learning)
    Unsupervised--->Data without label
      Machine_Learning--->Unsupervised







   
