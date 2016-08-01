---
title: Autocorrelation Lab
type: lab
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Autocorrelation Lab


## Introduction

> ***Note:*** _This can be a group programming activity or done independently._

Now that we've practiced analyzing changes over time, it's time to put your skills to use. Everyone knows the stock market is an easy way to make- or lose- a lot of money. Using time series analysis, let's take a look at a five stocks and see what you can learn.

You will report n at least 5 different publicly traded companies and describe the trends you've observed. It's up to you to decide which industries to investigate, but the 5 companies should be from the same industry. You will put your findings, including visuals, in a jupyter notebook with detailed comments.

## Exercise

#### Requirements

- Select a minimum of 5 companies to investigate.
- Find stock data that can be exported (See below for details).
- Use trend lines, autocorrelation, partial autocorrelation, and windowing functions to analyze the stock changes over time for the industries.
- Present your findings with explanations in a jupyter notebook.
- BONUS: Examine the relationships between the companies. Can you predict the trends in one company from the others? Does using windowing functions help with the predictions?

#### Exporting Stock Data

You can visit any company's summary page (e.g., http://finance.google.com/finance?q=nasdaq:goog) to export data.

Load the time series into `pandas` and do your analysis on the resulting DataFrame. Use your notes from the Autocorrelation lesson to use **trend lines**, **autocorrelation**, **partial autocorrelation**, and **windowing/differencing functions** to complete this lab.

#### Deliverable

Your deliverable should be a three part PDF submitted via Github PR. It should include the following three sections:

1. A description of the industry (or industries) and companies investigated (**minimum of 5 companies in 1 industry**).
2. Separate analyses of each publicly traded company investigated.
3. A summary of your findings including advice on investment strategies.
4. Your code used to analyse the data, clearly documented as needed.
