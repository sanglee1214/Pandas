---
title: Intro to LDA
type:  lab
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  The Revenge of the Fisher (Or a Bayesian in Sheep's clothing)
Week 8 | 3.3


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

1. Understand the basic apparatus for performing LDA (Linear Discriminant Analysis)
2. Use scikit-learn to perform basic LDA


### STUDENT PRE-WORK
*Before this lesson, students will need to be able to:*

1. Recall fundamentals of linear algebra
1. Demonstrate familiarity with Scikit-learn
1. Recall structure of basic algorithms
1. Review some additional materials:
 - PCA (for context and similarity)
 - Review Classification procedures (for context)

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| Timing | Type | Topic |
| --- | --- | --- |
| 5 min | [Opening](#opening) | A Brief overview of LDA |
| 10 min | [Introduction](#introduction) | Looking at the formal procedure behind LDA |
| 15 min | [Demo](#demo) | Blast from the past - The Bayesian Underpinnings of LDA |
| 25 min | [Guided Practice](#Guided)  | Comparing LDA and PCA with Python |
| 25 min | [Independent Practice](#Indy) | Using Scikit-Learn LDA method |
| 5 min |  [Conclusion](#conclusion)| Concluding Remarks |

---

<a name = "opening"></a>
## A Brief Overview of LDA (5 min)

LDA is an interesting topic, the full name is "Fisher's Linear Discriminant Analysis" yet, the underpinning of the formalism utilizes Bayes’ relation, which was known to Fisher as "the inversion procedure". Although the mathematical derivation of LDA is just the posterior probability formula, it isn't explicitly a Bayesian approach to statistics, as we must assume multi-variate normality as a foremost predicate for our analysis. Further, the algorithm between PCA and LDA is identical except for one or two important steps (more on that below). Yet, firmly in the 'guided learning' camp and the other is unguided.

Although seemingly contradictory, we'll see that it's fairly straight-forward, especially after working through the PCA algorithm.


<a name = "introduction"></a>
## Introduction: Looking at the Formal Procedure behind LDA (10 mins)

There are a few formal assumptions to the LDA procedure, which similar to the Naive Bayes classifier that we will go over later, are fairly robust even if these predicates are not always met "to-the-letter".

The first assumption we need to make for LDAs is that our data is multi-variate normal. Further, LDAs explicitly require a target/feature relationship (like Classification Trees or Logistic Regressions), and we further have to assume that the feature set are mutually independent, and there is one covariance matrix for the multi-class target.


#### The Secret Sauce - The Scatter Matrix

Since our data is multi-variate normal, we can do ourselves a big favor by normalizing the data to a standard-normal data (0 mean, variance of 1). The next step is to compute the means for each feature and for each class-label. Then, we compute the "within -class scatter matrix" and the "without-class scatter matrix".

The within-scatter matrix is as follows:

``$$\sum_{j=1}^{|c|}\sum_{i=1}^n (x-\mu)(x-\mu)^T$$``, which is a sum of 'outer-products' in fancy linear algebra jargon.

The without-scatter matrix is as follows:

``$$\sum_{i=1}^{{c|} n(\mu_{i}-mu)(\mu_{i})^T $$``

such that $\mu$ is just the mean of the data, |c| is just the number of class-labels

**Note**: Sometimes in math jargon "the number of something" or "the size of the set" or "how many elements there are in a sample" are denoted with the | x | where x is whatever variable. This symbol is called *modulus*.

Take a moment and think about these formulas. In just a little bit you'll be tasked to code up both of these matrices!

> Instructor Note: I think a great exercise is to have students translate simple equations/structures into Python code. It serves as a good substitute to proving something or doing typical math finger like exercises.


The rest of the steps are identical to PCA; in other wrods, it's basically a bunch of linear algebra: Find eigenvalues of eigenvectors of a matrix product, order your eigenvalues by magnitude, and construct a matrix with these values and project your sample by multiplying them with this matrix.

Thankfully, that all will be done by the computer! So we will ignore most of it :)

Recall that we have two optimizations working at once here, we wish to not only minimize the within-class matrix distance, but also maximize the without distance. The scatter-matrix values takes a familiar functional form:

`$$S_i = \sum_x = i ^{n} (x-\mu_{i})(x-\mu_{i})' $$`


<a name = "demo"></a>
## Demo: Blast from the past - The Bayesian Underpinnings of LDA (15 mins)

> Instructor: You may want to expand upon this result, and talk in depth about each step. It uses all of the mathematics they've seen before (the log transformation, the posterior distribution, and it's a basic LHS/RHS direct proof/result - similar to some of the finger exercises we did earlier in the week

Recall that we are interested in understanding the properties of the multi-class target. For simplicity, let's assume we just have a 2-class model. Given our study of Bayesian Analysis, we could contextualize our problem by using the posterior probability:

`$$ P(C_{1} | X = x) = \frac{f_{1} * \pi_{1}}{\sum_{i=1}^N f_{2}(x)\pi_{2}} $$`

Now LDA is concerned about the quotient between class 1 and class 2.

`$$log(\frac{P(C_{1}|X = x)}{P(C_{2}|X = x)} = log(\frac{f_{1}(x)}{f_{2}(x)} + log(\frac{\pi_{1}}{\pi_{2}} $$`

which is just:

`$$ log(\frac{\pi_1}{\pi_2} - \frac{1}{2}(\mu_{1}+\mu_{2})^T(\sum^-1(\mu_{1}-\mu_{2}))$$`



<a name = "Guided"></a>
## Comparing LDA and PCA with Python (25 mins)

LDA and PCA occupy the opposite spectrum in the class of machine learning techniques in one perspective, one is a supervised technique (LDA), and PCA is an unsupervised technique. In particular, LDA has an explicit objective to maximize class separation with a "linear line" (but in reality a 'hyper-plane' - but we usually don't visualize it that way).

PCA's main goal is to find the best set of orthogonal projections that maximize explained variance. Ok. But what does that mean? Well, in practice, some linear algebra, normalizing, computing eigenvalues (vectors), and doing projections... wait, this sounds just like PCA? Well that's one of the reasons people tend to confuse the two.

The kernel of the difference between the two centers on the matrix (really, no pun(s) intended...)

Write both the within-class and the without-class matrix for the iris data set:


```python
# Constructing the Without-Class Matrix
feature_num = int(X.shape[1])

mat_contain = np.zeroes((feature_num, feature_num))

vec1 = []
vec1.append(np.mean(X[0])); vec1.append(np.mean(X[1])); vec1.append(np.mean(X[2])); vec1.append(np.mean(X[3]))

for i in range(len(vec1)):
    for j in range(int(X.shape[0])):
        scatter_val = np.zeroes((feature_num, feature_num))
        ...
        # Complete the code!

```


<a name = "Indy"></a>
## Independent Study: Using Scikit-Learn LDA method (25 min)

So let's load up the data sets, import both the target and the potential features from the IRIS data set:

```python

# Possible solution

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.lda import lda

iris = datasets.load_iris()
X = iris.data; y = iris.target

target_names = iris.target_names
```

Now, invoke the LDA method to compute and fit the model:

```python
# Possible solution

lda_classifier = lda(n_components=2)
lda_x_axis = lda_classifier.fit(X, y).transform(X)
```
Now output a simple visualization of the model result:

```python
# Possible solution

color_scheme = ['r', 'g', 'b']

for c, i, target_name in zip(color_scheme, [0, 1, 2], target_names):
    plt.scatter(lda_x_axis[y == i, 0], lda_x_axis[y == i, 1], c = c, label = target_names)

plt.xlabel('First LDA); plt.ylabel('Second LDA')
plt.show()
```


<a name = "conclusion"></a>
## Conclusion (5 min)

Now that we have gotten our hands dirty with LDA, let's see if we can start to apply some of that using the data we have created!

### ADDITIONAL RESOURCES

- [Linear Discriminant Analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
