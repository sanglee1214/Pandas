---
title: Case Study in Bayesian Analysis 2
type: lab 2.3
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Case Study in Bayesian Analysis 2
Week 8 | 2.3

## Introduction

Today's lab will focus on handling missing data, something we haven't had a ton of practice with. We will review some of the previous techniques covered in the immersive course thus far, but utilize it to something that we probably haven't really discussed much of: how to handle missing data -in depth.

In general this topic is probably way more on the "art" in the science/art spectrum in the world of data science, but there are some well-established ways to deal with and impute missing data, depending on what you want to accomplish in the end (increase the power, remove NaNs, impute with a numerical/label to prevent errors from your ML algorithms etc.).

Our overall goal today will be to show there is some kind of "functional relationship" between the "missingness" of the data, and features found in our data. By doing this, we can categorize the kind of "missingness" we are dealing with for a particular data-set.

We'll briefly cover the 3 types of "missingness" and go straight to coding from there.


## Exercise

### Types of "missingness"

| Type  | Description  |
|---|---|
| Missing Completely at Random  | This is basically the best scenario, all NaN, NA, or blanks are distributed totally "at random" can be safetly omitted  |
| Missing at Random  | This is less strong, but is "random" given the sample you are using. This is what we're aiming at for our analysis, functionally, we want to show that our missing data isn't dependent on data we haven't observed or accounted for in our data set   |
| Missing not at Random  | "There is a data generating process that yields missing values". Basically, it means there is some "pattern" to the 'missingness' |

To summarize, we'll need to the following:

- Load up the data and the libraries we will need to get started!
- Load up data with missing values
- Use Logistic Regression to model the "missingness"
- Use K-Nearest Neighbor for imputing missing data

Specifically:

As stated, the type of “missingness” we are most concerned about is the last row, "Missing not at Random". And as good Statis... Data Scientist, we understand what "data generating process" really means: We can make an equation of sorts to "model" the “missingness” in our data set. If we can convincingly show that this model accounts for "most" (again we're not being stringent statisticians so that word will be left up to you to define for the moment) of the observable variation, we can be (relatively) well-at-ease that our "missingness" isn't functionally related to some features we don't have control/accounted/recorded in our data.

Before we move forward, we have to define the *inclusion indicator*. We say `I` is an inclusion indicator if: `$$\begin{array}{cc}`

```
  I=\{ &
    \begin{array}{cc}
      1 & x: missing \\
      0 & x: \neg{missing} \\
    \end{array}
\end{array} $$
```

Simple enough? Let's read on, and maybe we'll see how Bayesian analysis slips its slimy tenticles into seemingly simple things.


#### Requirements

We'll be studying a version of the polling data we used previously in Lab 1.4. In that lab we actually removed all missing values to better streamline our analysis and so we could focus more on the modeling aspect with respect to Bayes and not issues extraneous to that central theme. Now we've re-introduced the missing values, and will use this opportunity to address a very interesting subject of dealing with missing values, as well as a chance to review some previous techniques we've discussed in other weeks that may be put to use to deal with/or assess this problem.

Please review Bayesian lab 1.4 of this week, review what you've covered about missing data in previous weeks, as well as some techniques like bootstrapping, random forest, logistics etc., as many of them will make a reappearance here.


#### Starter code

[Start your engines! Here's the starter code](./code/w8-2.3-starter.ipynb)

> [Solution code](./code/w8-2.3-solutions.ipynb)

#### Deliverable

Submit a notebook with the code written to complete the exercises

#### Additional Resources

For those of you who want to read further:

- [Doing Bayesian Data Analysis](http://doingbayesiandataanalysis.blogspot.com/2014/01/bayesian-variable-selection-in-multiple.html)
