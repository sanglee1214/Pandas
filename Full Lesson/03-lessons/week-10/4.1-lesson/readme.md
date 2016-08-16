---
title: Database Design Case Study
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Database Design Case Study
Week 10 | Lesson 4.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- critically assess the needs of a client
- discuss the pros/cons of different database designs
- submit a proposal of a database design

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- perform queries in SQL
- perform queries in Hadoop & Hive
- perform queries in Spark

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min | [Opening](#opening) | Opening |
| 20 min | [Guided-practice](#guided-practice_1) | Phase 1: Research |
| 20 min | [Guided-practice](#guided-practice_2) | Phase 2: Database design 1 |
| 20 min | [Guided-practice](#guided-practice_3) | Phase 3: Database design 2 |
| 20 min | [Guided-practice](#guided-practice_4) | Phase 3: Presentation |

<a name="opening"></a>
## Opening (5 min)
In this lecture we will also work in 3 groups. Each group will get a different problem to solve.

- Group 1: Your client is a major bank, concerned with Credit card fraud. They would like you to take a look at their data on transactions in order to detect fraud.
- Group 2: Your client is a traditional hedge fund which is currently underperforming. They engaged your consulting services to help them with stock prediction as well as with their general infrastructure.
- Group 3: Your client is an ecommerce platform that allows people to buy and sell furniture. They have 100,000 100MB Images of desks, chairs, and other pieces of furniture and they would like your help to classify them into their respective categories.

<a name="guided-practice_1"></a>
## Phase 1: Research (20 min)

Your first task is to find out as much as possible about the problem at hand. Given the short time, it's best if you divide and conquer and have different team members in the group research different aspects of the problem.

In particular you should figure out:

- what is the problem exactly
- what is the size of data your client is typically dealing with (Volume)
- what is the speed required to manage the data (Velocity)
- what may be othe requirements in terms of compliance to regulations (if any)
- what is the expected outcome from your services

<a name="guided-practice_2"></a>
## Phase 2: Proposal (20 min)

In this phase you'll have to work collaboratively within your group to propose a platform to solve the client's needs. You are free to choose from any of the tools you've learned about so far. In particular you have to answer the following questions:

- what database will you use to meet your client's demand? (SQL, NoSQL, Big Data...)
- is it going to be hosted on the client's premises or in the cloud?
- what will be the major technical challenge?
- where will most of the development time be allocated?
- will the project focus more on ETL and data integration or on Machine Learning?
- if you have a supervised problem, how will you source the labels? does the client have them?
- what limitations will your proposed solution have?

<a name="guided-practice_3"></a>
## Phase 3: Presentation Prep (20 min)

In this phase you will draft a presentation both of your case and of the proposed solution. Make sure to touch on the points you explored in phases 1 and 2. In particular, you should go into the details of:

- how you will model the clients data
- which technology you will use
- which tables or data structures you will use
- why you will make those choices

<a name="guided-practice_4"></a>
## Phase 4: Presentation (20 min)

Each group will get 5 minutes to present their findings to the class.

> **Instructor note:** Here are a few points to lead the discussion:
- Did the team correctly identify the problem?
- Did the team correctly scope the solution?
- Did the team focus on the correct aspects of the implementation?
- Did the team design a database that is appropriate for the problem?

### ADDITIONAL RESOURCES

- [Database design](https://en.wikipedia.org/wiki/Database_design)
- [11 rules for database design](http://www.codeproject.com/Articles/359654/important-database-designing-rules-which-I-fo)
