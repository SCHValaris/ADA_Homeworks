---
layout: page
title: Reviews, do you help me ?
subtitle: An analysis of Amazon's reviews
use-site-title: true
---

# Introduction
Reviews systems are a key feature of most online shopping sites such as amazon. They make available to the customer the experience of multiples other customers, emulating a word of mouth opinion circulation. The force of these systems resides in the fact that the customer does not need to personally know the reviewer to get his/her opinion: it is just available on the shopping site. While this certainly helps customers which do not personaly know someone who bought or tested the product they are currently interested in, it may also be missleading because the customer does not know the background of the reviewer. For instance, the reviewers previous experience in the product category, his/her grading exigencies are not always detailed in the review, thus the customer may not be able to judge the reviewer point of view, and eventual biases. Can we infer these information from the data we have on the reviewer, and provide them to the customer to help him evaluate the review ?

In our analysis, we tried to learn two characteristic of the reviewers :
 - the grading exigencies: does the reviewer tend to give the products high grades, even if they are not fully satisfactory ? Or is he very exigent and never gives a product full score, until it is really outstanding ? We tried to infer this from the set of reviews of a reviewer with a sentiment analysis of the reviews text: if the sentiment of a text is higher than the rating of a review, then the reviewer is rather exigent. On the contrary, if the rating of a review is always higher than the sentiment of the review, then the reviewer easily gives good grades.
 - the reviewer expertise: what is the reviewer knowledge in the product category ? Is he qualified to assess the quality of a product ? A metric we can use to evaluate this is the number of reviews a reviewer has written in the product category: if the reviewer has written many reviews in a category, he is very likely to be able to judge the products in this category.

The analysis was performed on the set of amazon reviews [???]. We first present the data on several category of products, and then narrow our analysis to the Electronic category to present our grading system. 


{% include BokehGraph_Review_per_Product.html %}
{% include BokehGraph_Review_per_Ratings.html %}
