---
title: Naive Bayes
type: lesson
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Naive Bayes - The Gateway drug into Bayesian Computation
Week 8 | 4.3


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe Naive Bayes
- Start to become familiar with the scikit-learn's implementation of Naive Bayes

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Work with methods in scikit-learn
- Conceptually explain the Bayesian posterior distribution
- Write simple Python code to call methods/classifiers/predictors

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Review the Naive Bayes classifier
- Understand Bayesian Statistics
- Be prepared to tutor people on scikit-learn multinomialNB method

### LESSON GUIDE
| Timing | Type | Topic |
| --- | --- | --- |
| 5 min | [Opening](#opening) | Coming full-circle, it all comes back to Bayes Rule |
| 10 min | [Introduction](#introduction) | The basic formalism of Naive Bayes |
| 15 min | [Demo](#demo) | More in-depth foundations for Naive Bayes  |
| 25 min | [Guided Practice](#Guided)  | Using the Naive Bayes Implementation in Scikit-learn |
| 25 min | [Independent Practice](#Indy) | Apply your Naive Bayes on the data |
| 5 min |  [Conclusion](#conclusion)| Concluding Remarks |

---

<a name = "opening"></a>
## Coming full-circle, it all comes back to Bayes Rule (5 min)

By now, you should expect to see this formula (again and again, and again), and can safely assume it will play either the central (or highly influential) component of anything with the label "Bayesian" in it. Just in case you've forgotten the formula, here it is (yet again):

`$$ P(Class = value_i | Event ) = \frac{P( Event | Class = value_i)P(Class = value_i)}{P( Event)} $$`

Notice that this version of the Bayes formula is on a set of events, which will make assessing/resolving/interpreting it much simpler. In fact, this classifier is often used (similar to a logistic regression and/or CART) to analyze a 2-class target (i.e a target that assumes only 0 or 1 say).

As usual, `P(Class = i)` is the probability that `$ value_i $` has occurred, and the posterior can be interpreted as the probability of event `$i$` occurring after observing previous events. Further, the great thing about naive Bayes is that it only requires one simplifying assumption, and still performs well even if it's not fully satisfied!





---
<a name = "introduction"></a>
## The basic formalism of Naive Bayes (10 mins)

We're going to extend the Bayesian formula/relation a little to the following:

`$$ P(Class = i) = \frac{P(Event_1|Class = i)P(Event_2|Class = i)...P(Event_n|Class = i)}{P(Event)},$$`

for each `i` in the set of classes (again, if we had only two classes, i = 0 or i = 1), and where Event_1, ..., Event_n forms a partition of Event. We've seen this before, in the first lesson of the week. However, as you recall, for us to be able to make this substitution, we must assume that the probability of these events are independent.

To circle back and review, let's take an example, we can use canonical Spam classifier problem:

![](./assets/images/Naive Bayes SPAM.PNG)

This is the ordinary posterior distribution. Note the denominator is just the total probability. We can interpret the various components as follows;

- `P(S|W)`: Probability that Message is spam given word W occurs in it.

- `P(W|S)`: Probability that word W occurs in a spam message.

- `P(W|H)`: Probability that word W occurs in a Ham message.

More can be read about [Span filtering here](https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)


The cool thing about Naive Bayes however, is that in practice, we don't really need these assumptions strictly satisfied to get great performance out of the procedure (the miracle of Machine Learning!).


<a name = "demo"></a>
## Using the Naive Bayes Implementation in Scikit-learn (15 mins)

We've gone over the formalism of Bayesian analysis several times now, so we should be safe there. Let's get more hands-on work with analyzing Naive Bayes for computing.


```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Import data into a numpy array
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

#Initialize a variable as the Guassian Naive Bayes classifier and fit it with the data
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()

# Predict a few instances
print(clf.predict([[-0.8, -1]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
GaussianNB()
print(clf_pf.predict([[-0.8, -1]]))

```



<a name = "Guided"></a>
## Write your own Naive-Bayes classifier for real data (25 mins)

We're going to now try our hand at classifying some SPAM, a perennial problem, and a canonical example for machine learning with naive Bayes. Let's first load up the data

```python
# Work here
impor sklearn import naive_bayes
import numpy as np; import csv; import urllib

urllink = urllib('https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data')

read_csv_data = csv.reader(urllink)

```

Following with our first example, since we want to use scikit-learn's naive Bayes implementation we'll have to do some juggling to get the numpy array "just right". I know it's not as convenient as Pandas, but you should get use to also porting data into Numpy arrays, as a lot of heavy-duty machine learning will work better if you push vectors of data in numpy containers.

For computing reasons, it makes much more sense to define our numpy data matrix beforehand (instead of dynamically iterating the numpy array:

```python
# Work here - 2 different ways to load up the data
# Using Numpy
ri = 0
for row in read_csv_data:
    ri = ri + 1

numpy_data_mat = np.array(-1*np.ones((ri, 58), float), object)

numpy_iter = 0
for ri in read_csv_data:
    numpy_data_mat[numpy_iter, :] = numpy.array(ri)
    numpy_iter = numpy_iter + 1

numpy_data_mat_2 = -1*np.ones_like(numpy_data_mat)

# Using Pandas
pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data')


```


<a name = "Indy"></a>
## Apply your Naive Bayes on the data  (25 min)

Now we should take the results above and try our hand with Naive Bayes. Which Naive Bayes classifier should we utilize? There are 3 variants (Normal, Bernoulli, Multinomial). Could we do some conversion of the data and try one or the other? How should we think about diagnosing the model performance?

Again, we must defer to the docs:

- [Docs 1](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)
- [Docs 2](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
- [Docs 3](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)

The differences can be summarized as follows
-    ***BernoulliNB*** is designed for binary/boolean features
-    The ***multinomial Naive Bayes classifier*** is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as `tf-idf` may also work
-    ***GaussianNB*** is designed for continuous features (that can be scaled between 0,1) and is assumed to be normally distributed

> Note: Either pulling the data via Pandas or Numpy, you can go over with them the trivial solution, which is to literally include all numerical features (untransformed) with the target. Have them think through how they could improve the performance of the model

```python
# Work here

# We need to separate the features from the target.

feature_set = numpy_data_mat[:, :-1]
target = numpy_dat_mat[:, -1]


classifier1 = MultinomialNB().fit(feature_set, target)

# Define several different feature sets, I just dumped everything into the model, but do we get more or better accuracy #based on what set of features we put in? Is more always better?

# Discuss... and think about what kind of diagnosis metrics we could utilize for the model

```

<a name = "conclusion"></a>
## Conclusion (5 min)

This lesson, we observed how to instrument the data to feed into the Naive Bayes classifier. We can proceed to applying this next!

#### Additional Resources

- [An interesting slide from a Stanford MOOC which had a section on Naive Bayes](https://web.stanford.edu/class/cs124/lec/naivebayes.pdf)
- [A much more technical paper comparing Naive Bayes to Logistics Regressions](https://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf)
- [More exposition on Naive Bayes](http://blog.yhat.com/posts/naive-bayes-in-python.html)
