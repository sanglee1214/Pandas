---
title: Case Study in Bayesian Analysis 3
type: lab 2.4
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Case Study in Bayesian Analysis 3
Week 8 | 2.4

## Introduction

For today's lab we will build a basic Bayesian regression using PyMC. We're going to use a data-set procured from a credit card company with basic demographic data, and a limit balance. The later will be the target for our regression, and we will use the categorical column: sex, education, marriage, and the numerical column age, as our features.

The point of the lab will be to have greater familiarity with the PyMC environment as well as see how constructing a Bayesian regression is different from a classical multiple variable regression model. You'll note while doing the lab that building a Bayesian regression is often more involved, however, you'll also note that Bayesian regressions will give you, the data scientist more control over assumptions in the analytic model itself.

With this added complexity, comes a cost in terms of actually executing/estimating the parameters of your model, and thus you'll have to leverage a powerful procedure (*Monte-Carlo Markov Chains*) to actually compute the regression. You should be excited, as with a little more work, and learning in this sub-area of data science can quickly lead to exciting topics like deep learning.

Let's begin!



#### Requirements

We'll be working with our second UCI Machine Learning Repository data set.

The description of the data is as follows from the website (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients#):

    This research aimed at the case of customersâ€™ default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel â€œSorting Smoothing Methodâ€ to estimate the real probability of default. With the real probability of default as the response variable (Y), and the predictive probability of default as the independent variable (X), the simple linear regression result (Y = A + BX) shows that the forecasting model produced by artificial neural network has the highest coefficient of determination; its regression intercept (A) is close to zero, and regression coefficient (B) to one. Therefore, among the six data mining techniques, artificial neural network is the only one that can accurately estimate the real probability of default.

In this lab we're going to see what relationship simple demographics like sex, education, marriage status, and sex identifier have to the limit balance columns, but we'll build the regression model via the Bayesian paradigm and with PyMC, so you'll get more practice with this library and the associated methodologies.

Review your previous lab with PyMC and read the docs on the various methods so you can familiarize yourself with how to specify models in it.


#### Starter code

Please utilize the starter code found in the directory to start the students on today's activities
[starter code](./code/starter-code/)

#### Deliverable

Submit a notebook with the code written to complete the exercises

### Additional Resources

For those of you who want to read further:

- Model fitting doc in PyMC (https://pymc-devs.github.io/pymc/modelfitting.html)#
- MCMC model fitting https://pymc-devs.github.io/pymc/modelfitting.html#markov-chain-monte-carlo-the-mcmc-class
- PyMC class types: https://pymc-devs.github.io/pymc/modelbuilding.html
