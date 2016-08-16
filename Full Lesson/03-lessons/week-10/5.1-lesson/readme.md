---
title: Big Data Review: Case Study
duration: "1:25"
creator:
  name: Francesco Mosconi
  city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Big Data Review: Case Study
Week 10 | Lesson 5.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- explain how different big data tools are used to aggregate large quantities of weather data
- explain the advantages of big data tools to a non-technical audience

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- perform queries in Hadoop / Hive
- perform queries in SQL
- build pipelines in Spark

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
| 20 min | [Guided](#guided_practice_2) | Phase 2: Discussion |
| 20 min | [Demo](#demo) | Phase 3:  Mashup |
| 20 min | [Demo](#demo) | Phase 4:  Presentation |

<a name="opening"></a>
## Opening (5 min)

In this class we will analyze a case study of analysis of Real-Time and Archived NEXRAD Weather Data on AWS.

[Our starting point is this article](https://aws.amazon.com/blogs/publicsector/nexrad/)

We will work in 3 groups once more, and each group will focus on a particular technical aspect of the project.

- Group 1 will focus on database backend
- Group 2 will focus on real-time
- Group 3 will focus on visualization

<a name="guided-practice_1"></a>
## Phase 1: Research (20 min)

In this phase each group should read the article and then look for more information in particular concerning its specific focus.

- Group 1 should look into the data storage tools proposed in the article and understand deeply the data format, size and types.

- Group 2 should look into the tools for real-time analysis that are mentioned in the article and clearly understand what each one does. Also you should investigate what requirements there are.

- Group 3 should look into the requirements for visualization. What is necessary? how big is the data to be visualized? What's the frequency? If we are assuming a nontechnical audience, how should you present the key findings?

Each group can choose how to perform this phase, either each on their own or in smaller subgroups.

<a name="guided_practice_2"></a>
## Phase 2: Discussion (20 min)

Within your group you should discuss the results of the research phase and draft a document that details:
- issues involved
- solution proposed
- intended audience
- risks
- limitations
- benefits (in relation to audience)

<a name="demo"></a>
## Phase 3:  Mashup (20 min)

Now each of the three groups should divide in half, each forming two subgroups: A and B.

- All the A subgroups unite to form a new group
- All the B subgroups unite to form a new group

The two newly formed mega-groups will contain experts from each of the 3 original groups. In this phase you have to share your findings and discuss how to implement the system.

In particular you should come up with a roadmap to implement the system including:
- data you will access
- databaset contraints, pros/cons
- key visualizations

Is the system proposed in the article the best possible solution? can you suggest improvements?

Note that the system proposed in the article is [implemented here](https://github.com/stephenlienharrell/WeatherPipe) using [Java](https://en.wikipedia.org/wiki/Java_(programming_language)). Can you propose an alternative technology to achieve the same result?


<a name="demo"></a>
## Phase 4:  Presentation (20 min)

Each of the 2 groups A and B gets 5 minutes to present their solution and their findings to the class.

The group playing the audience role should look for similarities and differences with their own implementation and ask clarifying questions when a difference is found.

### ADDITIONAL RESOURCES

- [NEXRAD](https://en.wikipedia.org/wiki/NEXRAD)
- [Weatherpipe](https://github.com/stephenlienharrell/WeatherPipe)

