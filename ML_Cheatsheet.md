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
  
