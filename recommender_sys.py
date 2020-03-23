# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:02:05 2020

@author: uni tech
"""

# ********** MOVIE RECOMMENDER SYSTEM ************


# Importing libraries
import numpy as np
import pandas as pd

column_names= ['user_id','item_id','ratings','timestamp']
df=pd.read_csv('Book3.csv', names=column_names)


movie_title= pd.read_csv('Movie_Id_Titles.csv')


#Joining both dataframes
df=pd.merge(df, movie_title,on='item_id')



#Grouping the movies on the basis of their mean ratings
ratings= pd.DataFrame(df.groupby('title')['ratings'].mean())



# Creating a column for total number of ratings
ratings['no_of_ratings']= pd.DataFrame(df.groupby('title')['ratings'].count())



# Creating a matrix for all movie ratings
moviemat= df.pivot_table(index='user_id', columns='title', values='ratings' )
print(moviemat.head(10))


starwars_rating = moviemat['Star Wars (1977)']
print(starwars_rating.head())



# We can then use corrwith() method to get correlations between two pandas series:
starwars_correlation_with= moviemat.corrwith(starwars_rating)

starwars_corr = pd.DataFrame(starwars_correlation_with, columns=['Correlation'] )
print(starwars_corr.head())



# Now sort the values in the order of their correlation
print(starwars_corr.sort_values('Correlation',ascending=False).head(10))


starwars_corr= starwars_corr.join(ratings['no_of_ratings'])
print(starwars_corr.head())


starwars_final_corr = starwars_corr[starwars_corr['no_of_ratings']>100].sort_values('Correlation',ascending=False)
print(starwars_final_corr.head(10))



