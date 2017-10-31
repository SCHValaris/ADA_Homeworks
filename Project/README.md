# Title 
Reviews, do you help me ?

# Abstract
Amazon reviews play a part in the final decision of a customer when buying an item. However the reviewers previous experience in the product category, his/her grading exigence are not always detailed in the review, thus the customer may not be able to judge the reviewer point of view, and eventual biases. The goal of our data analysis is to determine the bias of a review and provide this information to the buyer to help him determine the degree of usefulness of the review.

# Research questions
- Can we determined if a reviewer is biased in his reviews ?
- Are there reviewers more prone to give useful informations on a new review based on their old reviews ?
- Are all reviews trustworthy ? Is it possible to detect fake reviews ?
- Are reviewers influenced by the price of the products ?


# Dataset
- We will use the Amazon Review Dataset (http://jmcauley.ucsd.edu/data/amazon/). More precisely, we will process the user review data and the metadata of the products. We will analyze the reviewer's text review with a sentiment analyzer and compare it to the ratings that he gave. With this analysis we expect to construct a model which will tell us if the rating correspond to the text review. We will also analyze the distribution of the ratings per category, items and reviewers to gain insights in the reviews distribution and build category of reviewers.

# A list of internal milestones up until project milestone 2
- Learn to how to process the dataset in the cluster
- Process the statistics side of our analysis : Mean rating per user / product / category, number of reviews per user ...
- Process the text analysis : Positivity / Negativity of the review, Similarity of the review (Bot detection)

# Questions for TA
- Is it possible to use text-based sentiment detection libraries on the cluster ?
- Is it still possible to change some small part of our project after ? (e.g We find another research questions still in the scope of the project, or add an other dataset in the list like Wikipedia)
