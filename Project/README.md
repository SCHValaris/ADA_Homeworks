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

# A list of internal milestones up until project milestone 3
- Complete the large analysis of all the datasets on Spark.
- Expand and complete the analysis on the 5-cores electronic dataset.
- Expand the analysis on other categories.
- Try to optimize the sentiment and similarity analysis.
- Write the data story.

# Questions for TAs
- We tried several sentiment analysis libraries and we are not really satisfied of the results: it doesn't detect heavy negativity. Have you any idea of a library which could help us ? We tried NLTK (Vader model), Spacy, Stanford Core NLP. The better results were with NLTK (see notebook).
- Same question for similarity analysis. We tried Spacy and some custom code (see in notebook).
