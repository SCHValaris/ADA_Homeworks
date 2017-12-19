# Import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf
import pandas as pd
import numpy as np


# Import the libraries to draw
import matplotlib.pyplot as plt
import seaborn as sns

def load_file_cat(filename,format,spark_session):
    """Function used to load a dataset using spark"""
    print('Loading : ' + filename)
    df = spark_session.read.format(format).option("header","true").load(filename)
    print('Loaded : ' + filename)
    #df.printSchema()
    return df


def compute_review_per_product(df, csv_filename):
    """Function used to compute the number of review per product using a spark
    dataframe and save it as a pandas dataframe"""
    # Do a Group By Product of all the reviews
    groupByProduct = df.groupBy('asin')
    # Compute the number of reviews by product
    review_count_by_product = groupByProduct.count()
    # Compute the number of reviews by product as a pandas dataframe for easier use
    df_review_count_pd = review_count_by_product.toPandas()
    # Save the number of reviews by product to a csv files
    df_review_count_pd.to_csv(csv_filename)
    return df_review_count_pd

def compute_review_per_rating(df, csv_filename):
    """Function used to compute the number of review per product using a spark
    dataframe and save it as a pandas dataframe"""
    # Do a Group By Product of all the reviews
    groupByProduct = df.groupBy('overall')
    # Compute the number of reviews by product
    review_count_by_product = groupByProduct.count()
    # Compute the number of reviews by product as a pandas dataframe for easier use
    df_review_count_pd = review_count_by_product.toPandas()
    df_review_count_pd.sort_values('overall',inplace=True)
    # Save the number of reviews by product to a csv files
    df_review_count_pd.to_csv(csv_filename)
    return df_review_count_pd


def draw_distribution(df = 0, csv = ''):
    """Function used to draw the distribution of number of reviews per
    number of products"""
    if not csv == '':
        df_review_count_pd = pd.read_csv(csv)

    fig = plt.figure(figsize=[10,5])
    # Plot a log log histogram of the number of reviews by product
    ax1 = fig.add_subplot(121)
    sns.distplot(df_review_count_pd['count'], kde = False,norm_hist = True,ax = ax1)
    ax1.set_yscale("log", nonposy='clip')
    ax1.set_xlabel('Number of reviews')
    ax1.set_ylabel('Number of products')

    # Compute a logx box plot of the number of reviews by product
    ax2 = fig.add_subplot(122)
    sns.boxplot(df_review_count_pd['count'],ax=ax2)
    ax2.set_xscale("log", nonposy='clip')
    ax2.set_xlabel('Number of reviews')
    plt.show()


# Function used to draw the distribution of the ratings
def draw_full_ratings(csv):
    """Function used to vizualise the distribution of the number of Reviews
    in the full dataset """
    df = pd.read_csv(csv)
    df.sort_values('number_of_review', inplace = True)
    df.reset_index(inplace = True, drop = True)
    bins = np.unique(np.logspace(0, np.log10(max(df['number_of_review'])), endpoint = True).astype(int))
    values = np.empty(len(bins)-1)
    for i in range(len(bins)-1):
        values[i] = np.sum(df.loc[np.where(np.logical_and(df['number_of_review']>=bins[i],
                                                    df['number_of_review']<bins[i+1]))]['number_of_product'])
    new_bins = (bins[:-1] + bins[1:]) / 2
    fig, (ax1,ax2) = plt.subplots(ncols=2,figsize=(10,5))
    ax1.bar(new_bins, values, width=np.diff(np.append(new_bins, 0)), log=True,ec="k", align="edge")
    #ax.set_xscale("log")
    ax1.set_xlabel('Number of reviews')
    ax1.set_ylabel('Number of products')
    ax1.set_title('Distribution of the number of ratings')

    ax2.bar(new_bins, values, width=np.diff(np.append(new_bins, 0)), log=True,ec="k", align="edge")
    ax2.set_xscale("log")
    ax2.set_xlabel('Number of reviews')
    ax2.set_ylabel('Number of products')
    ax2.set_title('Distribution of the number of ratings')
    plt.show()
