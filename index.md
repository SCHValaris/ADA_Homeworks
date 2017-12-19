---
layout: page
title: Reviews, what are you hiding ?
subtitle: An analysis of Amazon's reviews
use-site-title: true
---

#### Introduction
Reviews systems are a key feature of most online shopping sites such as Amazon. They make available to the customer the experience of multiples other customers, emulating a word of mouth opinion circulation. The force of these systems resides in the fact that the customer does not need to personally know the reviewer to get his/her opinion: it is just available on the shopping site. While this certainly helps customers which do not personally know someone who bought or tested the product they are currently interested in, it may also be misleading because the customer does not know the background of the reviewer. For instance, the reviewers previous experience in the product category, his/her grading exigencies are not always detailed in the review, thus the customer may not be able to judge the reviewer point of view, and eventual biases. Can we infer these information from the data we have on the reviewer, and provide them to the customer to help him evaluate the review ?
The reviews were obtained from [a dataset that contains 142.8 millions reviews spanning May 1996-July 2014](http://jmcauley.ucsd.edu/data/amazon/links.html).

First, let's observe the distribution of ratings across all the Amazon's reviews available

{% include BokehGraph_Review_per_Ratings.html %}
<center><em>Figure 2 : Number of reviews given for each rating for multiple categories</em></center>

Clearly, we see that for every category, the grading are skewed to higher grades. The reviewers have a tendancy to give high grades to the products they review. What about specific categories ? We can observe that the higher grades are given in the "Digital Music" category. This observation is easily explained as the majority of customer knows beforehand what is the music that they buy (by listening to radio, music videos ...) and the quality of the goods is constant which leads to little room for disapointment. Contrary to categories like "Cell phones and accessories" or "Video games" where the ratings is directly impacted by the production quality (materials used, finitions, presence of glitchs ...) which increases the variance of the ratings.

If everyone gives high grades, how can we distinguish a helpful reviews from a less helpful one ? That's where our analysis comes into action. We tried to derive a new grade for each product, by taking into account additional informations about the reviewers :
 - The grading exigencies: does the reviewer tend to give the products high grades, even if they are not fully satisfactory ? Or is he very exigent and never gives a product full score, until it is really outstanding ? We tried to infer this from the set of reviews of a reviewer with a sentiment analysis of the reviews text: if the sentiment of a text is higher than the rating of a review, then the reviewer is rather exigent. On the contrary, if the rating of a review is always higher than the sentiment of the review, then the reviewer easily gives good grades.
 - The reviewer expertise: what is the reviewer knowledge in the product category ? Is he qualified to assess the quality of a product ? A metric we can use to evaluate this is the number of reviews a reviewer has written in the product category: if the reviewer has written many reviews in a category, he is very likely to be able to judge the products in this category.

Before going into the depth of the analysis, let's vizualise the number of reviews given to each product 

{% include BokehGraph_Review_per_Product.html %}
<center><em>Figure 1 : Number of products per number of reviews for multiple categories given in log-scale for both axis</em></center>

We can observe that the distribution nearly follows a power law. The majority of products (showed by the red line) have a low number of reviews. To perform our analysis we decided to take only the reviewers and products that have at least 5 reviews. For that we use a 5-core dataset. We also chose to focus our analysis on the _Electronics_ category as it offer a lot of product diversity and is less prone to subjectivity than categories like _Books,Video Games_. Yolo?? 


Let's take a look at the distribution of the products in the Electronic category:
<p align="center"> 
 <img src="/ADA_Homeworks/img/Sentiment_distribution.svg">
</p>
<center><em>
 Distribution of the Sentiments of the reviews of the products in the "Electronic" category </em></center>

<p align="center"> 
 <img src="/ADA_Homeworks/img/Sentiment_distribution_groupby_product.svg">
</p>
<center><em> 
 Distribution of average of the sentiment of the reviews, per product in the "Electronic" category 
 </em></center>
 
<p align="center"> 
 <img src="/ADA_Homeworks/img/Rating_distribution_groupby_product.svg">
</p>
<center><em>
 Distribution of average of the Rating given in the reviews, per product in the "Electronic" category
 </em></center>

#### How to compute a new grade for a product ?
We will start by computin a new rating for the review of a product, based on the information we have on the reviewer, the rating of the review and the sentiment analysis of the review text.

Let us note $\text{Rating}(r)$ the rating of the review, and $\text{Sentiment}(r)$ the sentiment rating of a review, on a scale from 1 to 5, where 1 is very negative and 5 very positive. Moreover, let us note by $<\cdot>_{\text{product}}$ an average operation on all the reviews of a product.
We propose to compute the new rating of a review as follows :
\begin{equation}
 \text{new rating}(r) = w_s \left( w_sr \left(\text{Sentiment}(r) + \braket{Sentiment(r)} \right) \right)
\end{equation}



 {% include BokehGraph_New_Rating_Review.html %}
 <center><em>Figure 3 : Computation of the new rating for 5 different reviews</em></center>
 
  {% include BokehGraph_New_Rating_Product.html %}
 <center><em>Figure 4 : Computation of the new rating for 5 different products</em></center>
 
 
 _Citations : Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering, R. He, J. McAuley, WWW, 2016_
