# CS4442 Assignment 2: Predict survival on the Titanic
### Due: Monday, March. 18th, 2019 at 9:00 pm
### Weight: 20%
<br>

**Overview:**

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.

**New:**

1. Group work is allowed, with max of 2 students in a group.
2. We will give up to 3% bonus to students who do very well in Assignment 2.

**Goal:**

This textbook <Hands-On Machine Learning with Scikit-Learn and TensorFlow> is recommended to learn the practical machine learning project and implementation.
Follow the hand-on ML chapter 2’s example to build an end-to-end ML project with the “Titanic” dataset. Note you can use other similar or equivalent platforms or tools to accomplish the tasks in this assignment.
- Frame the problem and build a ML task
- Use pandas for data manipulation
- Learn to build models (naive Bayes and neural networks) covered from the lectures with scikit-learn.  You are welcome to try other machine learning algorithms available in scikit-learn.
- Fine tune and evaluate ML models

**Dataset:**

The dataset is from this Kaggle competition.  The data has been split into two groups:
- training set ([train.csv](./data/train.csv))
- test set ([test.csv](./data/test.csv))

This is an on-going competition, and you should submit your result to Kaggle as well.  Hopefully you will be on the Leaderboard.  Please include your “Team name” and score in the submission. The students with the top scores will be given 1% to 3% bonus mark (adding to the final mark).

**Specifications:**

Briefly discuss the problem and form your machine learning task
Get the dataset, describe the data structure with necessary output; visualize the data to discover more insights, apply at least one approach to analyze one perspective like the feature correlation
