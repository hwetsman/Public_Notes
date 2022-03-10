````mermaid
flowchart LR
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

    Unsupervised(Unsupervised<br>Learning)
      Machine_Learning--->Unsupervised
        Data(Data<br>without<br>label)
        Unsupervised--->Data

        clustering(Clustering)
          Data--->clustering
          K_mean(K<br>means)
            clustering--->K_mean
          K_med(K<br>median)
            clustering--->K_med
          hierarchy(Hierarchy<br>clustering)
            clustering--->hierarchy
          Expectation(Expectation<br>Maximization)
            clustering--->Expectation

        Association(Association<br>Analysis)
          Data--->Association
          APRIORI
            Association--->APRIORI
          Eclat
            Association--->Eclat
          FP(FP<br>Growth)
            Association--->FP

        Dimension(Dimensionality<br>Reduction)
          Data--->Dimension
          Feature(Freature<br>Extraction)
            Data--->Feature
            PCA(Prinicpal<br>Component<br>Analysis)
              Feature--->PCA
          Selection(Feature<br>Selection)
            Data--->Selection
            Wrapper
              Selection--->Wrapper
            Filter
              Selection--->Filter
            Embedded(Embedded_Mathod)
              Selection--->Embedded

    Reinforcement(Reinforcement<br>Learning)
      



````







   
