```mermaid
flowchart TD
id1{More Than 50 Samples?}
  id2{Predicting a category?}
    id1-->|Yes|id2
    id4{Labled Data?}
      id2-->|Yes|id4
      id6{>100K Samples?}
        id4-->|Yes|id6
        id14(Clustering)
        id15{Known number of categories?}
          id16{>10K samples?}
          id17{>10K samples?}
          id15-->|Yes|id16
            id20(Meanshift_VBGMM)
            id98(Tough Luck)
            id17-->|Yes|id20
            id17-->|No|id98
          id15-->|No|id17
            id18(Minibatch Kmeans)
            id19(Kmeans or spectral clustering GMM)
            id16-->|Yes|id18
            id16-->|No|id19
        id14-->id15
        id4-->|No|id14
        id7{Liner SVC works?}
        id6-->|No|id7
        id8{SGD Classifier works?}
          id13(kernal approx)
          id8-->|No|id13
        id6-->|Yes|id8
          id9{Is data text?}
          id7-->|No|id9
            id10(Naive Bayes)
            id9-->|Yes|id10
            id11{Kneighbors classifier works?}
            id9-->|No|id11
              id12(SVC ensemble classifiers)
              id11-->|No|id12
              id99(Done)

    id5{Predicting a Quantity?}
      id2-->|No|id5
      id30(Regression)
        id32{Less than 100 samples?}
          id33{Are fewer features important?}
            id32-->|Yes|id33
            id34(ElasticNet Lasso)
              id33-->|Yes|id34
            id35(SVR kernal='rbf' ensemble regressors)
              id33-->|No|id35
            id36{SVR works?}
              id35-->id36
            id37(RidgeRegression SVR with linear kernal)
              id36-->|No|id37
        id38(SDG Regressor)
          id32-->|No|id38
      id31(Just Looking?)
        id5-->|Yes|id30
        id30-->id32
        id5-->|No|id31
        id40(Dimensionality Reduction works?)
          id31-->|Yes|id40
        id41(Randomized PCA)
          id40-->|No|id41
        id42(Predicting structure?)
        id31-->|No|id42
          id42-->|No|id99
          id97(Tough luck)
          id42-->|Yes|id97

  id3(Get more data!)
    id1-->|No|id3
```

id1(This is the text in the box)
A-->|text|B
