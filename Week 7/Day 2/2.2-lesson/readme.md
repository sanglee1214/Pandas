---
title: Intro to Principal Component Analysis
duration: "1:25"
creator:
    name: Patrick D. Smith
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Principal Component Analysis
Week 7 | Lesson 2.2

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Conduct a full PCA analysis manually and using scikit-learn
- Explain the mathematical process behind PCA

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Understand how to calculate principal components without using scikit-learn
- Have a basic understanding of linear algebra

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | From Eigenvalues to Principal Componants  |
| 10 min  | [Introduction](#introduction)   | A Mathematical Introduction to Principal Componant Analysis |
| 15 min  | [Demo](#demo)  | Two Approaches to Principal Componant Analysis  |
| 25 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | PCA using Scikit-learn |
| 25 min  | [Independent Practice](#ind-practice)  | Manual PCA  |
| 5 min  | [Conclusion](#conclusion)  | What did we learn?  |

---

<a name="opening"></a>
## Opening (5 mins)

> **Instructor Note**
- Review prior labs/homework, upcoming projects, or exit tickets, when applicable
- Review lesson objectives
- Discuss real world relevance of these topics
- Relate topics to the [Data Science Workflow](https://drive.google.com/file/d/0Bx2SHQGVqWasOGY4dE95OFVvZjQ/view?usp=sharing) - i.e. are these concepts typically used to acquire, parse, clean, mine, refine, model, present, or deploy?
**Check:** Ask students to define, explain, and recall the basics of dimensionality reduction.

<a name="introduction"></a>
## Introduction: A Brief Mathematical Introduction to Principal Component Analysis (15 mins)

Last lesson we learned the about dimensionality reduction overall; now we're going to take an in-depth look at a very useful form of dimensionality reduction - **Principal Component Analysis** or **PCA**. Principal Component Analysis, in very simple terms, is a method to *simplify* the data so that any analysis becomes easier to conduct and more accurate. 

When conducting Principal Component Analysis there are two methods one could use - the covariance method and the correlation method. Last lesson, we looked at the more common covariance method, which is what we will explore in depth today. 

### The Covariance Matrix

Last lesson we learned how to create the covariance matrix using Numpy in Python: 

```python
covariance_matrix = np.cov(x_standard.T)
```

The basis of the covariance matrix, of course, is the **covariance** itself - best defined as a measurement of how much each of the **dimensions** vary about the mean with respect to each other. The **covariance matrix** itself is a representation of covariance across dimensions. 

### Eigenvalues and Eigenvectors

> Note: Draw this on the board to illustrate concept while discussing

An **eigenvalue** tells us how much variance exists in the data in a certain direction, which is represented by the **eigenvector**. When conducting a PCA, think of our data as an ellipse, with the datapoints marking the outside rim of this elipse. When decomposed, the selected datapoints forming the outside of this ring are our **eigenvalues**.

Now, let's imagine we drew a straight axis through the middle of this elipse; the distance between these points the axis would represent our **eigenvectors** From this, the *eigenvectors* that has the highest associated *eigenvalues* are our **principal components**

As you can see, there is an intuitive relationship between the covariance matrix and the eigenvectors/eigenvalues. Where the covariance matrix represents covariance across dimensions, its decomposition directly results in the eigenvector, which measures variance - we are simply reducing the dimensions so that we are left with fewer values.

### Explained Variance

Explained variance is exactly what it seems to be - it is the amount of variance that can be attributed to each of the principal components we discovered by finding the eigenvalues. This will help us choose which eigenvalues to keep for our Principal Component Analysis.

In python, we calculated the explained variance as: 

```python
eigenValSum = sum(eigenValues)
varianceExplained = [(i / eigenValSum)*100 for i in sorted(eigenValues, reverse=True)]
cumulativeVarianceexplained = np.cumsum(varianceExplained)
```

Where we sum the eigenvalues, and calculate the percentage of contribution to the variance, and then take a cumulative sum of the explained variance. The result will tell us which of our principal components we should keep.

### Tying it all together

Once we have the principal components that we'd like to keep, we create a **projection matrix** of their eigenvectors and plot these onto a graph to find our principal components. Next, we'll run through a demo of how these approaches work in real-time.

**Check:** Restate the theory behind PCA in your own words!

<a name="demo"></a>
## Demo: Two Approaches to Principal Component Analysis - Mathematical and Automated (20 mins)

Last lesson, we stopped at calculating the eigenvectors and eigenvalues - today we're going to take this a step further 

First, we're going to use the eigenvalues to calculate the **explained variance**. The explained variance is a measure that tells us how much of the total variance can be explained by each of the Principal Components. 

```python
totalEigen = sum(eig_vals)
varExpl = [(i / totalEigen)*100 for i in sorted(eig_vals, reverse=True)]
cumulativevarExpl = np.cumsum(varExpl)
```
Now, we'll calculate the projection matrix. Again, this is just a re-alignment of the **eigenpairs**, which are the combined eigenvalues and eigenvectors.

```python
Pmatrix = np.hstack((eigenPairs[0][1].reshape(4,1),
                      eigenPairs[1][1].reshape(4,1)))

```

After this, we calculate the new projected values using the **dot product**. We calculate *Y = X * M*, where X equals our standardized x values ```xStandardized = StandardScaler().fit_transform(X)``` where the large "X" is our feature attributes from when we originally split the dataset in lesson 2.1:

```python
X = data.ix[:,0:4].values
y = data.ix[:,4].values
```

and "M" is the matrix ```Pmatrix``` that we just calculated above. 

In Python, this is implemented as: 

```
Y = xStandardized.dot(Pmatrix)
```

#### PCA using Scikit-Learn

For a practical implementation of Principal Component Analysis, we can use Scikit-Learn's PCA function. 

This time, we'll import the PCA module from sklearn. As before, we'll split our dataset and standardize "x".

```python
from sklearn.decomposition import PCA 

x = data.ix[:,0:4].values
y = data.ix[:,4].values
xStandardized = StandardScaler().fit_transform(x)
```

Then, instead of calculating the eigenvalues and eigenvectors, we'll simply call the PCA function from sklearn and set the components at 2, much like we estimated "k" when learning about k-means clustering. 

```python
PCA_sk = PCA(n_components=2)
Y_sk = PCA_sk.fit_transform(x_std)
```

**Check:** Do students understand how the math translates into code? Do they understand the process? 

<a name="guided-practice"></a>
## Guided Practice: Topic (20 mins)

Now that you know the procedure, let's run through an implementation of PCA with a real dataset. 

We're going to be revisiting the classic [iris dataset](./assets/datasets/iris.csv) that we worked with last lesson. 

Open the [starter code](./code/starter-code/Starter-Code-Guided.ipynb) and follow along with the instructor. 

> Note: [solution code](./code/solution-code/Solution-Code-Guided.ipynb).

<a name="ind-practice"></a>
## Independent Practice: Topic (30 minutes)

Now that we've gone over the long-form approach to dimensionality reduction and worked through an example, let's put your skills to the test! We're going to be working with the [wine dataset](./assets/datasets/wine_v.csv) and we want to conduct a full PCA analysis on the data. Grab the [starter code](./code/starter-code/starter-code.ipynb) to begin!

> Note: [solution code](./code/solution-code/solution-code.ipynb).

**Check:** Were you able to complete the independent practice notebook? Did you run into any difficulties or roadblocks?


<a name="conclusion"></a>
## Conclusion (5 mins)

PCA is a useful tool for reducing our data down to it's core points, however it's important to remember it's an intermediate tool! For instance, say we have a large noisy data set that we want to cluster - PCA is a manner to reduce this dataset to make that clustering easier. We'll examine a case like this in your final project!

To recap: 

- We form the covariance matrix first
- Reduce the matrix to find the eigenvalues and eigenvectors
- Sort the combined eigenpairs and select the highest values
- Project the eigenpairs onto a new subspace using the dot product


> **Instructor Note**
- Review the math and overall process of PCA
- Ensure that students understand how all of the parts work together
- Review potential use cases of PCA

***

### ADDITIONAL RESOURCES

- [A graphical explanation of Principal Component Analysis](http://setosa.io/ev/principal-component-analysis/)
- [Documentation for PCA in Scikit-Learn](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
