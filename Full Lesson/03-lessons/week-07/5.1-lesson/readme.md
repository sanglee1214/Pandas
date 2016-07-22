---
title: Unsupervised Learning Case Study
duration: "1:25"
creator:
    name: Patrick D. Smith
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Unsupervised Learning Case Study
Week 7 | Lesson 5.1

### LEARNING OBJECTIVES
- Understand and consider audience scenerios for analyses
- Explain, emphasize, and communicate your results for different types of business stakeholders
- Visualize the results of an analysis in Tableau

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Create graphs and dashboards in Tableau
- Conduct a PCA

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Generate a brief slide deck
- Create a Tableau Dashboard with the data
- Provide students with additional resources
- Assignment should be administered as a case study, with the overall case introduced and the check-ins at the individual sections. 

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Opening](#opening)  | Deciding what's important  |
| 10 min  | [Introduction](#introduction)   | How do we parse through an analysis?  |
| 20 min  | [Independent Practice: Section 1](#ind-practice)  | Create a Dashboard  |
| 20 min  | [Independent Practice: Section 2](#ind-practice-2)  | Create a Dashboard  |
| 20 min  | [Independent Practice: Section 3](#ind-practice-3)  | Create a Dashboard  |
| 5 min  | [Conclusion](#conclusion)  | Conclusion |

---


<a name="opening"></a>
## Opening (10 mins)

- Include a business example of presenting the results of your analysis
    - IE: Many executives won't know how to interperate your results, how do you filter out what's important? 
- Speak to the importance of visualization
- Relate topics to the [Data Science Workflow](https://drive.google.com/file/d/0Bx2SHQGVqWasOGY4dE95OFVvZjQ/view?usp=sharing) 


**Check:** Ask students to define, explain, or recall any relevant prework concepts.

<a name="introduction"></a>
## Introduction: PCA Case Study (10 mins)

**Overview:** 

Given [raw scraped data](./assets/datasets/raw.csv) on the tweets about U.S. airlines for February, 2015; text processing and sentiment analysis was conducted on an original dataset of 50,000 tweets to understand customer sentiment about airlines. These original 50,000 points were paired down to 15,000 to reflect overlap and preserve only quality data. 

**Analysis:**

Given nearly 15,000 tweets, a sentiment analysis was conducted to interperet and understand feelings towards different airlines. NLTK in python was used to derive the sentiment as well as the confidence. 

The analysis looked at tweets about six major US airlines; American, Southwest, United, Delta, Southwest, U.S. Airways, and Virgin America, during the course of February, 2015. The [output](./assets/datasets/Tweets.csv) contains the following variables: 

- tweet_id: A unique identifier for each tweet
- airline_sentiment: The sentiment, with choices "neutral","positive", or "negative". 
- airline_sentiment_confidence: Level of confidence in the outcome
- negativereason: Negative comment, if it can be discerned  
- negativereason_confidence: Level of confidence for if the tweet is in fact negative or not
- airline: The name of the airline
- airline_sentiment_gold
- name: The twitter handle of the user
- negativereason_gold
- retweet_count
- text: The text of the tweet 
- tweet_coord
- tweet_created
- tweet_location
- user_timezone

**Task**

Using the results of the analysis, create a Tableau dashboard that illustrates the data. Afterwards, prepare a brief presentation for each of these key stakeholders: 

- The client, who wants to visually understand consumer sentiment
- Your boss, who wants to understand the process

**Bonus**

Convert the categorical variables to numeric and conduct a Principal Componant Analysis on the data. 

<a name="ind-practice"></a>
## Independent Practice: Setup your Dashboard (20 minutes)

Now, it's time to get to work! Open up your version of Tableau, download the [data](./assets/datasets/Tweets.csv), and get started! 

Your deliverables should be: 
- A finished Tableau dashboard to present to the client 
- Two presentations; one for the client, and one for your boss

For this section, connect to your data source and create your calculations that will run in the background of your dashboard.

<a name="ind-practice-2"></a>
## Independent Practice - Section 2: Put your Dashboard Together (20 minutes)

Now, let's spruce up that dashboard a bit. Here are things to look for: 

- Is your dashboard interative? 
- Can a user distinguish between labels and variables? Are elements of graphs too crowded? 
- How to your graphs weave together to tell a story? Is there anything that seems out of place? 

<a name="ind-practice-3"></a>
## Independent Practice - Section 3: Present your Dashboard (20 minutes)

Now that you have a polished dashboard, it's time to present it! Over the course of the next 20 minutes, present your dashboard and it's workings, and explain the calculations/methodology behind your finished product. 

<a name="conclusion"></a>
## Conclusion (5 mins)
- Dashboards have a wide applicability for a variety of usecases
- Framing and contextualizing your data an important aspect of the data science process
- Takeaways: 
    - Dashboarding is a frequent part of the data science workflow in a business enviroment. Knowing how to create one with a tool like Tableau will allow you to explain your data and analysis quickley and efficiently. 
    - Tableau is an ever-expanding data visualization tool that is valuable in the marketplace
    - Data visualization is quickley becomming a field on its own - learning how to create a dynamic visualization yourself is a beneficial skill

### ADDITIONAL RESOURCES

- See the original [kaggle page](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) for this dataset and analysis. 
- For help creating a great dashbaord, see [6 tips for creating Tableau dashboards](http://www.tableau.com/learn/whitepapers/5-best-practices-for-effective-dashboards)
- For more on Tableau, see the [Tableau training website](http://www.tableau.com/learn/training)
