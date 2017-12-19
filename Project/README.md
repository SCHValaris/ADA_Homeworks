# Reviews, what are you hiding ?

## Website : https://c-lefebvre.github.io/ADA_Homeworks/ 

# Abstract
Reviews systems are a key feature of most online shopping sites such as Amazon. They make available to the customer the experience of multiples other customers, emulating a word of mouth opinion circulation. The force of these systems resides in the fact that the customer does not need to personally know the reviewer to get his/her opinion: it is just available on the shopping site. While this certainly helps customers which do not personally know someone who bought or tested the product they are currently interested in, it may also be misleading because the customer does not know the background of the reviewer. For instance, the reviewers previous experience in the product category, his/her grading exigencies are not always detailed in the review, thus the customer may not be able to judge the reviewer point of view, and eventual biases. Can we infer these information from the data we have on the reviewer, and provide them to the customer to help him evaluate the review ? 


# Dataset
- We use the Amazon Review Dataset (http://jmcauley.ucsd.edu/data/amazon/). More precisely, we first processed the full ratings dataset and the full electronics category. We then did a more thorough analysis on the 5-core electronics dataset, our pipeline is easily usable to other categories. We tried several sentiment analysis libraries on the reviews to compute the sentiment score. We will now expand our analysis and try to find correlations and interesting insights in our data. More information on the processing can be found in the notebook.


# Who did what ?
- Nelson Antunes : Processed the dataset by creating functions to parse it. Coded the functions to compute the new ratings.
- Clément Lefebvre : Analysis of the large parts of the dataset using Spark. Construction and maintenance of the website. Plotting of the interactive graph.
- Vincent Pollet : Derived the sentiment analysis. Developed the idea and algorithm to compute the new ratings. Wrote the analysis part of the data story.


# Citations : 
- Dataset : _Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering, R. He, J. McAuley, WWW, 2016_
- NLTK/Vader library : _Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014._
- Bokeh library : _Bokeh Development Team (2014). Bokeh: Python library for interactive visualization_
