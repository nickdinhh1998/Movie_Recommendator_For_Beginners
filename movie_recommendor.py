#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:44:26 2020

@author: mac
"""

import numpy as np
import pandas as pd

data = pd.read_csv('ratings1.csv')
movies = pd.read_csv('movies.csv')
data = data.merge(movies, on ='movieId' , how ='left')

avarage_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

avarage_ratings['total ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

movie_users=data.pivot_table(index='userId',columns='title',values='rating')

correlaions = movie_users.corrwith(movie_users['Toy Story (1995)'])
