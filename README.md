# Machine Learning Problems

The idea is to solve machine learning problems, organize them to be used for referernces later, build good utilities which can be used in a generic way and  get a hands on about when to use what algorithm.
The repository also contains details about the ml algorithms used, their important aspects like working, performance, memory used

## Index
- Clustering
  - Mnist clustering
    - Using t-SNE to cluster handwritten digits

## Algorithms Index
- Clustering
  - tSNE
      - Type : dimensionalty reudciton, clustering
      - Use : visulaize high dimentional data
      - Properties :
        - more computaionally expensive than PCA
        - better to be used as exploration than clustering
      - Documentation : https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
      - References :
        - How it works : https://www.youtube.com/watch?v=NEaUSP4YerM&t
        - https://towardsdatascience.com/an-introduction-to-t-sne-with-python-example-5a3a293108d1
        - PCA vs tSNE : 
          - https://medium.com/analytics-vidhya/pca-vs-lda-vs-t-sne-lets-understand-the-difference-between-them-22fa6b9be9d0
          - https://medium.com/analytics-vidhya/pca-vs-t-sne-17bcd882bf3d#:~:text=t%2DSNE%20is%20also%20a,large%20pairwise%20distance%20maximize%20variance.&text=It%20takes%20a%20set%20of,it%20into%20low%20dimensional%20data.
  - PCA
      - Type : dimensionalty reudciton, clustering
      - Use : visulaize high dimentional data
      - References :
        - what :
          - https://www.youtube.com/watch?v=FgakZw6K1QQ
          - https://medium.com/analytics-vidhya/a-beginners-guide-for-dimensionality-reduction-using-principle-component-analysis-pca-c4c515ae49c1
          - https://medium.com/analytics-vidhya/how-does-pca-really-work-e53f640e5323
          - (with maths) : https://medium.com/analytics-vidhya/understanding-principle-component-analysis-pca-step-by-step-e7a4bb4031d9
        - PCA vs tSNE with code : https://medium.com/analytics-vidhya/pca-vs-t-sne-17bcd882bf3d
        
