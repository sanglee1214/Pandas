---
title: Logistic Regression with PyStan
type: Lab
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---


# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Logistic Regression with PyStan
Week 8 | 2.2

## Introduction

As you recall, for linear regressions, we estimate parameters by deploying some kind of least square technique, the usual suspect being the ordinary least squares (OLS). However, a logistic regression breaks one of the cardinal assumptions of OLS, namely the normality of the target (dependent) variable, since logistics are binary.

You'll recall that we have to deploy the apparatus of the MLE to do parameter estimation for the right-hand side of the equation. Recall that MLE seek to find the maximum probability given the data at hand.

MLE's require a few ingredients: one is a well defined likelihood function. Given the fact that we are dealing with binary targets, we can easily model these using Bernoulli scheme: `$$ P(x_i)^{r_i}(1-P(x_i)^{1-r_i})$$`

Recall also that we seek to maximize the following: `$$\prod_{i=1}^n P(x_i)^{r_i}(1-P(x_i)^{1-r_i})$$`, yet because off the annoying property of computing the derviatives numerically, it's best to trasform this with the logarithm, which makes this into computing a derivative of a product chain to computing a derivative of a sum: `$$\sum_{i=1}^n [r_i * ln(P(x_i)) + (1-r_i)ln(1-P(x_i))]$$`

A much "cleaner" functional form with respect to computing a derivative. From here, the problem is transferred to solving a constraint optimization problem. Rarely will you have to do this by hand, and we did some simple finger exercises previously for you to get the feel of it, but in general, the software will handle these in the background for you.

For those of you with the mathematical background, you should read up on iterative numerical methods for least square problems.

#### Requirements
- Review Logistic Regression
- Review MLE
- Review the ingredients of Logistic Regression to understand motivations of PyStan Code

#### Starter code

[Get started here!](./code/w8-2.2-starter.ipynb)

> [Here are the solutions](./code/w8-2.2-solutions.ipynb)


#### Deliverable

Complete the lab stub and provide a solutions.

#### Additional Resources

- [PyStan Docs](https://pystan.readthedocs.io/en/latest/)
- [Least Square Problems](https://en.wikipedia.org/wiki/Least_squares)
