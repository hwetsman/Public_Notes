```mermaid
flowchart TD
Start --> More_Than_50_Samples
  More_Than_50_Samples --> Predicting_a_Category
    Predicting_a_Category --> Labeled_Data

    
    Predicting_a_Category --> Non-labeled_Data



  More_Than_50_Samples --> Not_Predicting_a_Category


Start --> Less_Than_50_Samples
  Less_Than_50_Samples --> Get_More_Data


```

```
  Start --> More_Than_50_Samples
  More_Than_50_Samples --> Predicting_a_Category
  Predicting_a_Category --> Labeled_Data
  Predicting_a_Category --> Non-labeled_Data
  More_Than_50_Samples --> Not_Predicting_a_Category
  Not_Predicting_a_Category --> Predicting_a_Quantity
  Predicting_a_Quantity --> Regression
  Regression --> 100_samples
  Regression --> Less_than_100_samples
  Less_than_100_samples --> fewer_features_important
  fewer_features_important --> ElasticNet lasso
  Less_than_100_samples --> fewer_features_not_important
  Not_Predicting_a_Category --> Not_Predicting_a_Quantity
  Start --> Less_Than_50_Samples
  Less_Than_50_Samples --> Get_More_Data
```

fewer_features_not_important --> SVR_kernalrbf_EnsembleRegressors
  SVR_kernalrbf_EnsembleRegressors --> SVR_works
  SVR_kernalrbf_EnsembleRegressors --> SVR_doesnt_work
  SVR_doesnt_work --> RidgeRegressionSVR_kernal_linear


Start
>50 samples?
  no get more data

  yes predicting a category?
    no predicting a quantity?
      yes (then we'll do regression) < 100 samples?
        yes fewer features important?
          yes - ElasticNet Lasso
          No - SVR(kernel = 'rbf') EnsembleRegressors if not working, RidgeRegression SVR(kernal='linear')
        No - SGD Regressor
      No - just looking?
        yes - (then we'll do dimensionality reduction) randomized PCA if not working, if less than 10K samples Isomap Spectal Embedding or LLE, otherwise Kernal Approx.
        No - Predicing structure? tough luck
    yes labeled data?
      yes (then we'll do classification) <100K samples?
        yes Linear SVC if not working is text? if yes, naive bayes, if not text then Kneighbors classifier or if not working SVC ensemble classifiers
        No SGD classifier and if not working kernal approx.
      no (then we'll do clustering) Are number of categories known for sure?
        No - <10K samples 
          yes - Meanshift VBGMM
          no - otherwise tough luck
        Yes - <10K samples?
          yes Kmeans or spectral clustering GMM
          no  minbatch Kmeans
  
