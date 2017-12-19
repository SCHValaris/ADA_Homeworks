                            ############################    Importation PART (start)   ############################

import pandas as pd
import numpy as np
import ast
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

                            ############################   Importation PART (end)   ############################


                            ############################   Cleaning PART (start)   ############################

def literal_list(string):
    try:
        return ast.literal_eval(string)
    except:
        return []


def literal_dictionary(string):
    try:
        return ast.literal_eval(string)
    except:
        return {}
    
    
def read_DataFrame_From_CSV(path = 'Electronic_Review_And_MetaData_Dataframe.csv',
                            columns_to_use_as_index = ['Product ID', 'Reviewer ID'],
                            columns_to_read_as_lists = ['Categories', 'Helpfulness Votes'],
                            columns_to_read_as_dictionary = ['Sales Rank', 'Related Products'],
                            columns_to_read_as_string = ['Brand']):
    Dataframe = pd.read_csv(path,index_col = columns_to_use_as_index)
    for column in columns_to_read_as_lists:
        Dataframe[column] = Dataframe[column].map(lambda d: literal_list(d))
    for column in columns_to_read_as_dictionary:
        Dataframe[column] = Dataframe[column].map(lambda d: literal_dictionary(d))
    return Dataframe


                            ############################   Cleaning PART (end)   ############################


                            ############################   Analysis PART (start)   ############################  

def get_number_reviews(reviewer):
    """Function that returns how many reviews a reviewer has write."""
    
    #Take the text of the review.
    reviews = reviewer['Review Text']
    
    #return the length of the text.
    return len(list(reviews))
    
    
    
def get_all_size_review(reviewer):
    """Function that returns the length of all reviews of the reviewer."""
    
    #Take the text of the review and put them into a list.
    reviews = list(reviewer['Review Text'])

    #Map all the texts with our function get_words_review.
    reviews_len = list(map(get_words_review,reviews))
    
    #Return the length of all the text.
    return reviews_len
    
    
def get_mean_reviewText(reviewer):
    """Function that returns the mean of how many words the reviewer writes."""
    
    #Take the text of the review.
    reviews = reviewer['Review Text']
     
    #Return the mean.
    return np.mean(list(map(get_words_review,reviews)))
    
    
    
def get_mean_rate(reviewer):
    """Function that returns the mean rate of a viewer."""
    
    #Take the mean rate of the viewer.
    mean_rates = reviewer['Review Rating'].mean()
    
    #Return this value.
    return mean_rates


def get_all_rate(reviewer):
    """Function that returns all the rates of a viewer."""
    
    #All the rates and put them into a list.
    rates = list(reviewer['Review Rating'])
    
    #Return this list.
    return rates
    

def get_words_review(review):
    """Function that returns the number of words in a review."""
    
    #Number of words in the review.
    number_words = len(review.split())
    
    #Return this value.
    return number_words


def get_category(reviewer):
    """Function that retuns the categories in which the reviewer has purchased an item."""
    
    #All the categories in each the viewer has reviewed and put them into a list.
    categories = list(reviewer['Categories'])
    
    #Dictionnary that will take the categories as keys and the number
    #of articles reviewes as values.
    cat_review={}

    #For loop that take all the articles within the categories and increase
    #its value in the dictionnary.
    for article in categories:
        for x in article[0]:
            if x not in cat_review:
                cat_review[x] = 1
            else:
                cat_review[x] +=1
                
    #return the dictionnary  
    return cat_review


   
def statistics(df,reviewerId):
    """Function that computes statistics on the reviewer, it returns the mean rate, all the rates, the length and the mean 
        lengths of all reviews, the number of reviews and the categories of the item it purchases."""
    
    #We get all the reviews of the reviewer with it's Id.
    reviewer = df.loc[reviewerId]
    
    #computation of the mean rate of the reviewer.
    mean_rate = get_mean_rate(reviewer)
    
    #take all the rates of the reviewer.
    rates = get_all_rate(reviewer)
    
    #take all the length of the reviews of the reviewer.
    reviews_len = get_all_size_review(reviewer)
    
    curr_len = reviews_len[0]
    
    #take the mean of the length of the reviews of the reviewer.
    mean_review_len = get_mean_reviewText(reviewer)
    
    #take the number of reviews the reviewer has done.
    reviews = get_number_reviews(reviewer)
    
    #Create a dictionnary with the categories of the item purchased in key and
    #the number of items purchased as values.
    cat_review = get_category(reviewer)
    
    #Create a dataframe with the corresponding statistics for the reviewer.
    reviewer_df = pd.DataFrame({
        'Reviewer': reviewerId,
        'rates': [rates],
        'mean_rates': mean_rate,
        'number_reviews': reviews,
        'length curr_review': curr_len,
        'review(s)_length': [reviews_len],
        'mean_review_length': mean_review_len
       })
    
    #we add to the dataframe the categories of the items.
    for x in cat_review:
        reviewer_df[str(x)] = cat_review[x]
        
    #return the statistics.
    return reviewer_df



def statistics_product(df,productId):
    """Function that returns the statistics about all the reviewer 
        of a product"""
    
    #Reset the index.
    df_prod = df.reset_index()
    
    #Set the index as 'Product ID'.
    df_prod = df_prod.set_index('Product ID')
    
    #Location of the product given its productId.
    df_prod = df_prod.loc[productId]
    
    #List of all the reviewer.
    reviewerId = list(df_prod['Reviewer ID'])
    
    #list of the rates of the article.
    current_rates = list(df_prod['Review Rating'])
    
    #usefull lists.
    stat = []

    #list with all the statistics of the reviewers via our statistics function.
    for id_ in reviewerId:
        stat.append(statistics(df,id_))
        
    #Keep the important columns to display the dataframe.
    important = ['Reviewer','Rate reviewer','mean_rates','length curr_review','mean_review_length','number_reviews',
                 'rates','review(s)_length', 'Electronics']
    
    #Concatenation of the statistics of the reviewers.  
    stat_reviewer = pd.concat(stat,ignore_index=True)
    
    #Column of the rates.
    stat_reviewer['Rate reviewer'] = current_rates
    
    
    #list the order of the columns of the dataframe.
    reordered = important + [c for c in stat_reviewer.columns if c not in important]
    
    #reordering the columns of the dataframe.
    stat_reviewer = stat_reviewer[reordered]
    
    #Fill the na values with 0.
    stat_reviewer = stat_reviewer.fillna(0)
    
    #Return the dataframe.
    return stat_reviewer

                            ############################   Analysis PART (end)   ############################ 
    
    
    
                            ############################   Plot PART (start)   ############################  
        
plt.style.use('ggplot')

def analyse_pair(df):
    """Function that plot the parity of the columns of interest of our review-dataframe"""
    
    #The columns we want to analyse to check.
    #We will have plots of one column in function of one other.
    pp = df[['Rate reviewer', 'mean_rates', 'length curr_review', 'mean_review_length', 'number_reviews']]
    
    #Prepare the results.
    sns.pairplot(pp)
    
    #Show the results.
    plt.show()

    
def analyse_ref(df):
    """Function that plot some interesting plots"""
    
    #Create figure of 4 plots.
    f, ax = plt.subplots(2, 2, figsize=(20,10))
    
    #useful lists.
    rates = [] 
    review_lengths = []
    
    ##First plot: histogram of all the rates of all the
    ##reviewers of the review.
    
    #taking all the rates.
    for x in df.rates:
        rates += x
        
    #creation of the histogram
    pd.DataFrame(rates).hist(ax=ax[0,0])
    
    #setting the title.
    ax[0,0].set_title('Rates')
    
    ##Second plot: histogram of all the length review of
    ##all the reviewers of the review.
    
    #taking all the lengths of the reviews.
    for x in df['review(s)_length']:
        review_lengths += x
        
    #creation of the histogram
    pd.DataFrame(review_lengths).hist(ax=ax[0,1])
    
    #setting the title.
    ax[0,1].set_title('Review length')
    
    ##Third plot: plotting all the categories in each all
    ##the reviewers of the review has purchased an item.
        
    #taking the lasts columns of our dataframe which corresponds
    #to the categories we want, summing them and plot them.
    df[df.columns[9:]].sum(axis=0).sort_values()[::-1][:15].plot.bar(ax=ax[1,0], rot=90)
    
    #setting the title.
    ax[1,0].set_title('Categories purchased')
    
    ##Last plot: we show the difference beetween the rate of the
    ##review of the reviewer and the mean rate of the reviewer
    ##for all the reviewers of the review.
    
    #Taking the mean rate and the rate of the reviewer.
    dff = df[['mean_rates', 'Rate reviewer']]
    
    #Substracting them.
    dff.differ = df['Rate reviewer'] - df.mean_rates
    
    #Plotting the results.
    dff.differ.plot.bar(ax=ax[1,1])
    
    #Setting the title.
    ax[1,1].set_title('Deviation from the mean')
    
    #Setting the x-labels.
    ax[1,1].set_xticklabels(df['Reviewer'])
    
    #Finally showing the results.
    plt.show()
    
    
def hist_length_review(df):
    """Function that plot the distribution of the length of the reviews"""
    
    #using seaborn to create it.
    sns.distplot(df['length curr_review'])
    
    #showing the result.
    plt.show()
    
def corr_len_rate(df):
    """Function that calculate the correlation between the length of the review and the rate of the review"""
    
    #calculate the correlation.
    corr = df[['length curr_review', 'Rate reviewer']].corr()
    
    #return the result.
    return corr


                            ############################   Plot PART (end)   ############################ 
