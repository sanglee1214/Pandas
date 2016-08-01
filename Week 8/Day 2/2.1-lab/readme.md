---
title: Let me tell you a guy named STAN ...
type: Lab 2.1
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) PyStan Introduction
Week 8 | 2.1

## Introduction

> ***Note:*** This can be a pair programming activity or done independently.

So although the basic idea of Bayesian regressions is not much different from what you saw when doing linear regressions. There will be a major difference in how they are implemented in code. Whereas one simply pushed in columns of data and a target into a regression to get output, the actual "specification" of the model is a bit more involved in the Bayesian variety. In particular, you will have to specify priors, likelihoods etc.

However, fear not, we are not going to write any of these posterior distributions and their associated ingredients manually. 

We're going to introduce a dedicated software packages this week, *PyStan*, that not only gives you leverage in the specification side, but includes a whole lot of really efficient C++ code to do the parameter estimation. Unlike what you did earlier in the week, we won't use MLE to estimate the parameters utilizing the Monte-Carlo Markov Chain (MCMC) - instead, we'll use the magic of code!

Although this topic is in itself not the point of our lecture, it will be a tool we leverage over-and-over again to estimate our models. For those of you who are interested in reading more, check out the following link:

- [Hardcore primer (requires Calculus, and strong mathematical maturity)](http://www4.stat.ncsu.edu/~sghosh/TEACHING/st790/lectures/GillMCMC.pdf)
- [Not as Hardcore](http://statwww.epfl.ch/teaching/3eCycleRomand/printemps-2005/EG.lectures.villars05.pdf)

Unfortunately, there's just no way around a lot of mathematics when dealing with MCMC.

Getting back to our previous discussion, the difference between classical and Bayesian regression can be thought of as thus:

***"Classical regression is a special case of the Bayesian perspective whereby we have a non-informative prior."***

I'm sure you recall what *non-informative* refers to uniform priors (i.e. no prior information assumed to bias things one way or another).

The Bayesian approach also relaxes a few assumptions, we no longer have to assume homoskedasticity etc.

[Just in case you need to review this - here's a good definition of homoskedasticity](https://www.youtube.com/watch?v=zRklTsY9w9c).

You can remember what it means by just breaking the word down to it's component parts - homo : same, skedastic : variation, the later word can be thought of as being related to "skew" i.e. how much your line "skews" from the "true" trend-line.

However, as previously stated, the Bayesian approach is fundamentally the "inverse" trick (i.e `f(X|$\theta$) to f($\theta$|X)`, and is primarily concerned with estimating parameters. In the case of Regressions, estimating` $\beta$'s` and estimating `$\sigma$'s` (and thus `$\sigma^2$'s`).

Why does this matter? Bayesian regressions give you, the modeler/data scientist a lot more control over your model. You can specify priors for each of the parameters in your regression (the $\beta$'s), the error term, and even the constant (as well as the target). Therefore, it's worth to learn, and will give you more latitude to fit your model to the data you

So we know that the joint of $\beta$ and $\sigma^2$ is proportional to the precision, defined as `$\frac{1}{\sigma^2}$`. Further, `$$p(\beta, \sigma^2|{y}) = p(\beta|{y}, \sigma^2)p(\sigma^2|{y})$$`

Of course, we have check that this is not a pathological probability (proper) blah blah, but this ins't a mathematics course, so we'll again be blissfully ignorant of these complexities!

If we had a procedural step-wise perspective of the procedure, here's what it would be:

1. Determine `$\beta$`, `$\sigma$` using posterior distributions
2. Construct `$y_{i+1}, y_{i+2}, ... y_{i+n}$` from a distribution using the parameters from step 1

## Exercise

The most critical element of the PyStan interface is the model specification module. This is also possibly the trickiest, since it's going to be passed in as a bulk-string from Python's perspective, any syntax issues won't immediately be caught by any error-checking feature from your IDE. We all got to remove the training wheels at some point!

#### Requirements

```
data {
// Defining your data
}
transformed data{}

parameters {
// Defining the name of your parameter and it's numerical parameters
// Explicitly required
}

transformed parameters{}

model {
// Specifying your model parameters
// Explicitly required
}

generated quantities{}
```

#### Starter code

Please use the [starter code found here](./code/w8-2.1-starter.ipynb)

> [Solutions](./code/w8-2.1-solutions.ipynb)


#### Deliverable

-Complete Jupyter notebook.
-Analyze the data set using PyStan methods

#### Additional Resources

For those of you who want to read further:

- [PyStan docs](https://pystan.readthedocs.io/en/latest/)
- [Video summary of Bayesian Regression](https://www.youtube.com/watch?v=dtkGq9tdYcI)
