---
title: Interview Prep
duration: "1:20"
creator:
    name: Robby Grodin
    city: BOS
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Interview Prep
Week 11 | Lesson 3.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand the goals of whiteboard interviewing
- Recognize the correct approach to whiteboarding interview problems
- Clearly explain the thought process behind their solutions

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Evaluate potential candidate opportunities in the field
- Address basic interview questions from a Data Science perspective

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | The Data Collection Problem  |
| 5 min  | [Introduction](#introduction)   | What is Whiteboarding  |
| 15 min  | [Discussion](#discussion)  | Whiteboarding Steps  |
| 25 min  | [Demo](#demo)  | Attempting a Problem  |
| 25 min  | [Guided Practice](#guidedpractice)  | Interview Time  |
| 5 min  | [Conclusion](#conclusion)  | Conclusion  |

---

<a name="opening"></a>
## The Data Collection Problem (5 mins)

Imagine you are locked in a room with a complete stranger for 1 hour. In the room are the following objects:
- A table
- A garbage can
- a whiteboard

Once you emerge from the room, you'll be asked to decide whether or not the stranger will be worth the investment your company wants to make. 

Will they produce a good ROI on their yearly salary? Will they be able to work well with you and your other coworkers? Will they remain at the company long enough for it to matter?

So which of the above do you use to help answer these questions? I'll give you a hint- sitting at a table won't help, and unless they are truly a terrible candidate, the garbage can won't either.

<a name="introduction"></a>
## Introduction: What is Whiteboarding? (5 mins)

> Instructor's Note: Ask the students if they've ever had a technical interview with a whiteboard component (outside of practice in class). Ask some probing questions, i.e. What did they think of it? Did they do well? Did they feel prepared?

Simply put, whiteboarding is when you're asked to solve a problem using a whiteboard (or sometimes even a laptop) to show your work. It's a very commonly used interview technique in the Tech industry to learn more about the means by which you produce work. In Data Science especially the output isn't the most important aspect to a project, it's the *means by which you accomplished it.*

For example, knowing that your model has the best RMSE is meaningless if it takes 30 days to train. If you're interviewing for a role that will have you coding a lot, you may be asked to write an algorithm in pseudocode. In this case, even if you get the right answer, the interviewer usually won't care. All they want is to see that you can write code that is bug free and efficient. 

What does that mean, necessarily?

For a solution to be bug free, look for any flaws in your logic. Did you misuse a component? Did you leave something out? By tracing through your logic step by step, identify areas where your response may be incorrect, or cloudy. Efficiency is not based on accuracy, it's based on the overall approach. Did you take 3 steps where you could have only taken 1? Are you replicating work, or are there steps that aren't necessary? 

Ask these critical questions about your solution, and be open minded to feedback from the interviewee. There's nothing wrong with admitting you made a mistake, as long as you are aware of it and show that you are interested in fixing that mistake, rather than throwing your hands up and surrendering.

**Check:** Does whiteboarding sound effective? Can you think of any other way to accurately gauge a candidate's worth?

Whiteboarding sessions typically follow this format:

1. Interviewer poses a question
2. Interviewee talks through the problem, solving it on the board
3. Interviewer applauds and offers a huge signing bonus

The particulars regarding step 2 can sometimes get a bit lost. Let's break this down into discrete steps:

<a name="discussion"></a>
## Discussion: Whiteboarding Steps (15 mins)

A quick disclaimer before we start- these steps are mostly aimed at technical problems, the kind that would be solved by coding. Some steps can be ignored for more abstract questions such as brain teasers or benchmarking problems.

#### 1. Clarify specifications

In the whiteboarding session it is most likely that you will have _N_ minutes to solve a problem that would typically take _N_ + 10 minutes. One of the worst mistakes a candidate can make is to incorrectly assume that they understand the question, forging ahead down the wrong path. Time lost can be very dangerous! Repeat the problem in your own words to the interviewer. Ask any questions you may have about how you're expected to address the problem. 

This part should only take a few minutes, enough to get you started and show that you are conscientious about _looking before you leap_.

#### 2. Write tests

**Note:** This is mainly for coding problems, but could be useful in other product design problems.

This step can be seen as a continuation of step 1. Now that you know what your code should do, formalize your inputs and your outputs. We're not looking for fully coded unit tests, but a simple explanation of your expected results. This will help you along the way to make sure you're on the path. Think of it as defining a starting and end point before you devise a route.

Let's assume you were asked to define a process for dividing two numbers. Your 'tests' should be written roughly in this format (and yes, they should be written on the board):

division(1, 2) => 0.5

division(0, 3) => infinite

division(1, 0) => ERROR
    
These 'tests' should cover all possible inputs to your solution, whether it's a set of features or some sort of pre-conditions for your answer to run. If there are any inputs that would break your solution, now is a good time to identify them. See the 'Additional Resources' section for a link to a great discussion on writing tests.


#### 3. Find naive solution

Whiteboarding is more about how a problem is solved than the solution, but you still are expected to solve it. Quickly find a naive solution that works. Make sure you talk out what you're doing and explain your reasoning. This naive solution can be almost anything- a brute force algorithm, a simpler version of the problem, a drawn representation of the problem/solution, whatever it takes to get something working. 

Some tips for this part:

- _Never be silent_ - it's difficult for the interviewer to gather data if you don't provide a signal. 

- _Use your space wisely_. Don't write yourself into a hole by covering the whole board, you'll need room to correct any errors. 

- _Admit what you don't know_. You're not expected to know everything, but you're expected to know how to find the answers. If you don't know the best way to do something, what would you do on the job? You'd probably Google it. Tell the interviewer this. It doesn't make you look weak, it shows that you are realistic about the work you'll do. 

- _SLOW DOWN!_ All too often candidates rush through and make silly mistakes. Odds are the person interviewing you has been subjected to quite a few of these interviews. They don't expect you to solve the problem in super-human time, and if they do, you probably don't want to be working with them anyway.

#### 4. Optimize!

After you've gotten a simple solution down, evaluate it. Does it satisfy the tests you've written? Does it utilize a lot of space? Is it time efficient? Does your model fit properly? Did you select the right features? Verbally ask yourself these questions and evaluate their answers. 

This is your time to turn to the interviewer and discuss what you've done. Think of this as your code review. Be very careful with your language, both verbal and physical. When you're told that you're wrong, that's when the interview truly begins. If you react poorly you can pack up and leave. Nobody wants to work with someone who gets defensive or combatative over a difference in opinion. 

#### 5. Take feedback

Maybe you didn't get the optimal answer. You might not have gotten a working solution at all. That's ok, you tried. Even if you did get a solution, ask the interviewer if there's anything they would have done differently. If you were doing well, this shows that you care about collaborating to do things the best way you can. If you failed, use this as a learning experience. Always be open to feedback.

#### 6. Debrief

In between interviewers, take a minute to debrief. Have an internal conversation about what went well and what went wrong. Each new interviewer is an opportunity to show someone something about yourself that they may connect with. Don't get shook by a difficult problem. Center yourself, and get ready for the next one.


**Check:** Let's review the steps. Can you recall the strategies discussed regarding achieving a naive solution? Can you think of anything else to keep in mind?

<a name="demo"></a>
## Demo: Attempting a Problem (25 mins)

Let's walk through a problem together. This is a simple problem with no correct answer, but plenty of business implications. We're going to discuss each step as we go, with me playing the role of interviewee. Don't focus on the right or wrong answers, let's focus on the process. 

**The Problem:** Design a strategy for recommending products for visitors to your e-commerce site who have never been to the site before.

> Instructor's Note: Feel free to swap this problem out with any you prefer. In front of the class, use the whiteboard to walk though the previously defined steps for whiteboarding. You'll play the part of the interviewee, with an invisible interviewer. Make sure you talk through your process with the class.
> The solution to this problem is very open. You should design a process in high-level pseudo code. Your solution will likely be to use a model that takes into account information you can get from the user's browser (location, referal ID, etc.), and matches that to top selling SKUs from similar customers. You also could utilize information such as seasonal prodcuts or sales. You should discuss business implications, such as filtering out SKUs that are at risk for backorder, or giving preference to items that lend themselves to upsells or repeat purchases.

<a name="guidedpractice"></a>
## Guided Practice: Interview Time (25 mins)

We're going to do this again, but now I'm going to have one of you play the role of the interviewee. Any volunteers?

For the rest of you, pretend there's an invisible wall up- you can see us, but cannot communicate with us. Watch, observe, and hold your questions until the end.

** The Problem: ** There's a coin that may or may not be fair. This coin has some probability of landing on heads, notated as p(H). To make matters worse, someone else will be flipping the coin and reporting the results to you. This person has a tendency to lie at a given frequency- we'll call that p(L). Given p(L), how many coin tosses are needed to determine a reason value for p(H)?

> Instructor's Note: The solution to this problem is a graph similar to the one [here](./assets/images/coin.png). The main concepts the student should graps are:
> 1) When they lie every time, you need no more flips than if they never lied. The function is symmetrical.
> 2) There is some lower limit at p(L) = 0 and p(L) = 100. You'll always need some coin tosses to make an estimate, so you will never approach a Y of 0.
> 3) At p(L) = 50, Y is infinite. If they lie half the time you will never be able to guess p(H).


**Check:** What went well? What didn't? What can we learn?

<a name="conclusion"></a>
## Conclusion (5 mins)

We've now covered many aspects of approaching the Data Science job search and interview process. Every company tends to have their own methods, so don't get too comfortable with any of this- you will invariably get thrown a curveball at some point. Remember that every interview is aimed at gathering data. Be a Data Scientist- figure out what questions are being ask, and deduce how best to answer those questions. 

Don't forget, however, that you are also interviewing the company. While your goal is to get a job offer, you should also be gathering your own information. Did you enjoy speaking with everyone? Do you think you'll enjoy working next to them? Were you treated respectfully? The way a company interviews you can tell you a lot about how they are run. Keep an eye out for any red flags, and don't be afraid to ask your own questions.

***

### ADDITIONAL RESOURCES

- [Discussion on Unit Testing](http://programmers.stackexchange.com/questions/750/what-should-you-test-with-unit-tests)
- [Discussion on Whiteboard Interviewing](https://www.quora.com/What-are-some-ways-to-get-better-at-whiteboard-interview-questions)
