# Reviews, do you help me ?

# Abstract
Amazon reviews play a part in the final decision of a customer when buying an item. However the reviewers previous experience in the product category, his/her grading exigencies are not always detailed in the review, thus the customer may not be able to judge the reviewer point of view, and eventual biases. The goal of our data analysis is to determine the bias of a review and provide this information to the buyer to help him determine the degree of usefulness of the review.

# Research questions
- Can we determine if a reviewer is biased in his reviews ?
- Are there reviewers more prone to give useful information on a new review based on their old reviews ?
- Are all reviews trustworthy ? Is it possible to detect fake reviews ?
- Are reviewers influenced by the price of the products ?


# Dataset
- We use the Amazon Review Dataset (http://jmcauley.ucsd.edu/data/amazon/). More precisely, we first processed the full ratings dataset and the full electronics category. We then did a more thorough analysis on the 5-core electronics dataset, our pipeline is easily usable to other categories. We tried several sentiment analysis libraries on the reviews to compute the sentiment score. We will now expand our analysis and try to find correlations and interesting insights in our data. More information on the processing can be found in the notebook.


# Who did what ?
- Nelson Antunes :
- Clément Lefebvre : Analysis of the large parts of the dataset using Spark (e.g ratings per category, number of reviews per category ...). Managing the construction of the website. Plotting of the interactive graph using Bokeh to put on the website.
- Vincent Pollet : 


# Citations : 
- Dataset : _Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering, R. He, J. McAuley, WWW, 2016_
- NLTK/Vader library : _Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014._
- Bokeh library : _Bokeh Development Team (2014). Bokeh: Python library for interactive visualization_
