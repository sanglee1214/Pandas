---
title: Hive Queries Lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Hive Queries Lab

### AWS Credentials Required
Note: This lab requiress additional prep in order to run successfully:

1. [Sign up for AWS Account & Credits](../AWS-instructions.md).
    - Note: Instructors will need to distribute individual URLs for the signup form. See linked instructions.

## Introduction

For this lab we will use data from the [Bay Area Bike Share Open Data Website](http://www.bayareabikeshare.com/open-data)

We've downloaded a part of it which is available in your assets folder. Each trip is anonymized and includes:

- Bike number
- Trip start day and time
- Trip end day and time
- Trip start station
- Trip end station
- Rider type – Annual or Casual (24-hour or 3-day member)

If an annual member trip, it will also include the member’s home zip code

The data set also includes:

- Weather information per day per service area
- Bike and dock availability per minute per station


## Exercise

#### Requirements

- Spin up EMR cluster
- Log into HUE
- Import Data and create tables
- Top start station
- Chart of top start station
- Top destinations + Map

**Bonus:**
- Analyze trips hourly

#### Starter code

[Starter Code](./assets/code/starter-code/starter-code.ipynb)
> [Solution Code](./assets/code/solution-code/solution-code.ipynb)

## IMPORTANT:
Make sure to terminate your cluster and remove logs from S3 once you're done to avoid unnecessary costs.

- Open your AWS console
- Make sure you're in the correct geographic region (top right)
- Go to the EMR window
- Stop all clusters and make sure they stop
- Go to the S3 window
- Check that there are no buckets you didn't want
- Go to the EC2 window
- Check that there are no running instances


### Additional resources

- [Bay Area Bike Share Open Data Website](http://www.bayareabikeshare.com/open-data)
- [AWS EMR](https://us-west-2.console.aws.amazon.com/elasticmapreduce/home?region=us-west-2)
