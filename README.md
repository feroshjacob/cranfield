# Cranfield Search 

### What is this?
This is very simple search implementation for the cranfield dataset.

### What is the cranfield dataset?
Cranfield is a small curated dataset that is very extensively used in the information retrieval experiments.
In the dataset, there are 226 queries (search terms), 1400 documents, and 1837 (evaluations).
The dataset is supposed to be complete in the sense that the documents that should be returned for each known are known.
This makes the evaluation easier. [Click here more details](http://ir.dcs.gla.ac.uk/resources/test_collections/cran/)

### Can I run this search implementation and see the output?
Yes!. Try to run the class `edu.kennesaw.cs.core.EvalSearch`. The expected output looks like as below:
```text
172)solution of the blasius problem with three-point boundary conditions . dcg=7.523719014285829, ideal=10.158777744901698,ndcg= 0.7406126212438987
192)papers dealing with uniformly loaded sectors . dcg=4.0, ideal=11.793836475517567,ndcg= 0.3391602052736162
Total ndcg score=0.004798990340077844
```

### What is nDCG score?
[nDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) is a very common metric used in search evaluations. 
Higher nDCG score (close to 1.0 ) describes a search system that gives all the relevant results with most relevant ones on the top.

### What should be the goal for this project?

Try to modify the code such that you can increase the nDCG score. 