# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 08:51:48 2020

@author: Mike
"""
#Data Science Capstone
#Michael Bassett

#This is all of the code used for the "review.json" yelp dataset

#NOTE - SOME OF THIS INCLUDED SO MUCH DATA THAT IT WAS REQUIRED THAT I USE COLONIAL ONE AT GWU

import json 
import pandas as pd

#Similar to the business dataset, review.json is not true json data and must be reformatted
with open("review.json", errors="ignore") as file:
    #Creating an empty list
    reviews = []
    #for each business, append it to the businesses list
    for line in file:
        review = json.loads(line)
        #append
        reviews.append(review)

#This creates a new file which is in a proper json format
with open("review_new.json", "w") as file:
    json.dump(reviews, file)

#print the first element to see what it looks like
print(reviews[0])

#There are 6,685,900 reviews

#Pulls all_cities_2 (which we made in the businesses code), pulls review_new, creates dataframes, and performs merge
#Then outputs a merged.csv file

#Part 1 - all_cities_2 piece 
with open("all_cities_2.json", errors="ignore") as file:
    data = json.load(file)

b_list = []

for business in data:
    temp = {}
    
    temp["business_id"] = business["business_id"]
    temp["city"] = business["city"]
    temp["state"] = business["state"]
    
    b_list.append(temp)
    
print(type(b_list))
print(len(b_list))

#Part 2 - review_new piece
with open("review_new.json", errors="ignore") as rfile:
    data_r = json.load(rfile)
    
print(len(data_r))

r_list = []

for line in data_r:
    temp = {}
    
    temp["business_id"] = line["business_id"]
    temp["stars"] = line["stars"]
    temp["text"] = line["text"]
    
    r_list.append(temp)
    
print(type(r_list))
print(len(r_list))

#Part 3 - DataFrame Conversion
bdf = pd.DataFrame.from_records(b_list)
rdf = pd.DataFrame.from_records(r_list)
print(bdf.head())
print(rdf.head())

#Part 4 - Merge
mdf = pd.merge(bdf,
              rdf[['business_id','stars','text']],
              on='business_id')
mdf.head()
print(type(mdf))
print(len(mdf))

#Part 5 - Output a csv file
mdf.to_csv('merged.csv', index=False)


#This is the code for after you've created the "merged" csv files
merged_sample = pd.read_csv('merged.csv')
print(type(merged_sample))
print(merged_sample.head())

#The reviews were split up into good reviews and bad reviews to see how the words vary
#There are no reviews with a rating of 0, and all ratings are whole numbers

#Subsetting to only show reviews with a 4 or 5
merged_good = merged_sample[merged_sample.stars >= 4]
print(merged_good.head())

#another subset that is only bad reviews
merged_bad = merged_sample[merged_sample.stars <= 2]
print(merged_bad.head())

#City 1 - Calgary, AB
calgary_good = merged_good[merged_good.state == 'AB']
print(calgary_good.head())

calgary_bad = merged_bad[merged_bad.state == 'AB']
print(calgary_bad.head())

#City 2 - Toronto, ON
toronto_good = merged_good[merged_good.state == 'ON']
print(toronto_good.head())

toronto_bad = merged_bad[merged_bad.state == 'ON']
print(toronto_bad.head())

#City 3 - Pittsburgh, PA
pittsburgh_good = merged_good[merged_good.state == 'PA']
print(pittsburgh_good.head())

pittsburgh_bad = merged_bad[merged_bad.state == 'PA']
print(pittsburgh_bad.head())

#City 4 - Charlotte, NC
charlotte_good = merged_good[merged_good.state == 'NC']
print(charlotte_good.head())

charlotte_bad = merged_bad[merged_bad.state == 'NC']
print(charlotte_bad.head())

#City 5 - Phoenix, AZ
phoenix_good = merged_good[merged_good.state == 'AZ']
print(phoenix_good.head())

phoenix_bad = merged_bad[merged_bad.state == 'AZ']
print(phoenix_bad.head())

#City 6 - Las Vegas, NV
lasvegas_good = merged_good[merged_good.state == 'NV']
print(lasvegas_good.head())

lasvegas_bad = merged_bad[merged_bad.state == 'NV']
print(lasvegas_bad.head())

#City 7 - Madison, WI 
madison_good = merged_good[merged_good.state == 'WI']
print(madison_good.head())

madison_bad = merged_bad[merged_bad.state == 'WI']
print(madison_bad.head())

#City 8  - Cleveland, OH
cleveland_good = merged_good[merged_good.state == 'OH']
print(cleveland_good.head())
print("There are " + str(len(cleveland_good)) + " reviews with 4 stars or more")

cleveland_bad = merged_bad[merged_bad.state == 'OH']
print(cleveland_bad.head())
print("There are " + str(len(cleveland_bad)) + " reviews with 2 stars or less")

#This is a list of common stopwords, which will be excluded from the counts
stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 
             'again', 'there', 'abou', 'once', 'during', 
             'out', 'very', 'having', 'with', 'they',
             'own', 'an', 'be', 'some', 'for', 
             'do', 'its', 'yours', 'such','into',
             'of', 'most', 'itself', 'other', 'off',
             'is', 's', 'am', 'or', 'who',
             'as', 'from', 'him', 'each', 'the',
             'themselves', 'until', 'below', 'are', 'we', 
             'these', 'your', 'his', 'through', 'don',
             'nor', 'me', 'were', 'her', 'more', 
             'himself', 'this', 'down', 'should', 'our', 
             'their', 'while', 'above', 'both', 'up',
             'to', 'ours', 'had', 'she', 'all', 
             'no', 'when', 'at', 'any', 'before',
             'them', 'same', 'and', 'been', 'have',
             'in', 'will', 'on', 'does', 'yourselves', 
             'then', 'that', 'because', 'what', 'over', 
             'why', 'so', 'can', 'did', 'not', 
             'now', 'under', 'he', 'you', 'herself', 
             'has', 'just', 'where', 'too', 'only',
             'myself', 'which', 'those', 'i', 'after', 
             'few', 'whom', 't', 'being', 'if',
             'theirs', 'my', 'against', 'a', 'by', 
             'doing', 'it', 'how', 'further', 'was',
             'here', 'than',"it's",'about','place',
             'also','about','us',"i've",'got',
             "i'm",'get']

#Module for the good subset

#NOTE - Ran this for every subset, ending with cleveland_good
good = cleveland_good.to_dict('records')
print(type(good))

#Creating an empty list   
good_reviews = []  

#Pulling just the text and adding that to the above list

for line in good: 
    review = line["text"]
    good_reviews.append(review)

#Print to see what it looks like
print(good_reviews[0])

#Within each line, remove symbols
good_reviews = [line.replace(",", "").replace("-"," ") for line in good_reviews]

#Print again to see if it did what we expect
print(good_reviews[0])

#Creating a dictionary which we need for finding the counts
rg = dict()

#For each word, keep track of the count
for line in good_reviews:
    words = line.split()
    for w in words: 
        w = w.lower()
        if w in stopwords:
            continue
        rg[w] = rg.get(w,0) + 1

#Sorting
sorted_rg = sorted(rg.items(), key=lambda kv: kv[1], reverse=True)
sorted_rg = sorted_rg[0:20]
print('Below are the top 20 words for the good reviews')
print(sorted_rg)

#Module for the bad subset
#NOTE - Did this for each subset, ending with cleveland_bad

bad = cleveland_bad.to_dict('records')
print(type(bad))

#Creating an empty list   
bad_reviews = []  

#Pulling just the text and adding that to the above list

for line in bad: 
    review = line["text"]
    bad_reviews.append(review)

#Print to see what it looks like
print(bad_reviews[0])

#Within each line, remove the symbols

bad_reviews = [line.replace(",", "").replace("-"," ") for line in bad_reviews]


#Print again to see if it did what we expect
print(bad_reviews[0])

#Creating a dictionary which we need for finding the counts
rb = dict()

#For each word, keep track of the count
for line in bad_reviews:
    words = line.split()
    for w in words: 
        w = w.lower()
        if w in stopwords:
            continue
        rb[w] = rb.get(w,0) + 1

#Sorting
sorted_rb = sorted(rb.items(), key=lambda kv: kv[1], reverse=True)
sorted_rb = sorted_rb[0:20]
print('Below are the top 20 words for the bad reviews')
print(sorted_rb)

#All output was added to excel Results sheet as well as Tableau visualization