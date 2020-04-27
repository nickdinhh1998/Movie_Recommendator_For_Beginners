#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:44:26 2020

@author: nickdinh
"""
#Import the necessary libraries
import numpy as np
import pandas as pd

#Load the datasets
data = pd.read_csv('ratings1.csv')
movies = pd.read_csv('movies.csv')

#Merge two datasets
data = data.merge(movies, on ='movieId' , how ='left')

#We need to compute the avarage ratings and total ratings for for each movie/title
avarage_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
avarage_ratings['total ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

#Create table to easily visualize dataset
movie_users=data.pivot_table(index='userId',columns='title',values='rating')

#Compute corr between the movie(the one users watching,looking,..) and other movies
correlations = movie_users.corrwith(movie_users['Toy Story (1995)'])

#finally, let's show the movies which could be recommended (also, we need to drop all NaN values)
recommendation = pd.DataFrame(correlations, columns=['correlations'])
recommendation.dropna(inplace = True)
       
                          
