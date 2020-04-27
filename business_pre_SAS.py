# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:08:42 2020

@author: Mike
"""
#Data Science Capstone
#Michael Bassett

#This is the first set of code used for the "business.json" yelp dataset

import json 
import pandas as pd

#Creating one large dataset with all 8 cities we need

#Opening up the actual yelp data, which is not in a true json form/structure
with open("business.json", errors="ignore") as file:
    #Creating an empty list
    businesses = []
    #For each business, append it to the businesses list
    for line in file:
        business = json.loads(line)
        businesses.append(business)

#Creating a new file which is in a proper json format
with open("business_new.json", "w") as file:
    json.dump(businesses, file)
    
#Print the first element to see how it looks
print(businesses[0])

#Create all_cities_1, which is every BUSINESS that is in our 8 cities of interest

all_cities_1 = [business for business in businesses if 
((business["state"]=="AB") and ("Calgary" in business["city"])) or 
((business["state"]=="ON") and ("Toronto" in business["city"])) or
((business["state"]=="PA") and ("Pittsburgh" in business["city"])) or
((business["state"]=="NC") and ("Charlotte" in business["city"])) or 
((business["state"]=="AZ") and ("Phoenix" in business["city"])) or
((business["state"]=="NV") and ("Las Vegas" in business["city"])) or
((business["state"]=="WI") and ("Madison" in business["city"])) or
((business["state"]=="OH") and ("Cleveland" in business["city"]))]

#Counting how many businesses there are in the 8 cities
#There are 100,261 businesses
print(len(all_cities_1))

#Create all_cities_2, which is only restaurants in the 8 cities of interest
all_cities_2 = [business for business in all_cities_1 if (business.get("categories")) and ("Restaurants" in business.get("categories"))]

#There are 29,558 restaurants. This aligns with your earlier exploratory data analysis
print(len(all_cities_2))

#DEALING WITH ATTRIBUTES
#Attributes are lists within each business
#We need to create new variables for each individual attribute
for i, business in enumerate(all_cities_2):
    #Step 1: Set to N/A if "attribute" doesn't exist
    if business["attributes"] is None: 
        Alcohol = "N/A"
        BikeParking = "N/A"
        BusinessAcceptsCreditCards = "N/A"
        Caters = "N/A"
        GoodForKids = "N/A"
        HasTV = "N/A"
        NoiseLevel = "N/A"
        OutdoorSeating = "N/A"
        RestaurantsAttire = "N/A"
        RestaurantsDelivery = "N/A"
        RestaurantsGoodForGroups = "N/A"
        RestaurantsPriceRange2 = "0"
        RestaurantsReservations = "N/A"
        RestaurantsTakeOut = "N/A"
        WiFi = "N/A"
        
    #Step 2: Pull out the existing variable - if it doesn't exist, set to "N/A"   
    else:
        Alcohol = business["attributes"].get("Alcohol","N/A")
        BikeParking = business["attributes"].get("BikeParking","N/A")
        BusinessAcceptsCreditCards = business["attributes"].get("BusinessAcceptsCreditCards","N/A")
        Caters = business["attributes"].get("Caters","N/A")
        GoodForKids = business["attributes"].get("GoodForKids","N/A")
        HasTV = business["attributes"].get("HasTV","N/A")
        NoiseLevel = business["attributes"].get("NoiseLevel","N/A")
        OutdoorSeating = business["attributes"].get("OutdoorSeating","N/A")
        RestaurantsAttire = business["attributes"].get("RestaurantsAttire","N/A")
        RestaurantsDelivery = business["attributes"].get("RestaurantsDelivery","N/A")
        RestaurantsGoodForGroups = business["attributes"].get("RestaurantsGoodForGroups","N/A")
        RestaurantsPriceRange2 = business["attributes"].get("RestaurantsPriceRange2","0")
        RestaurantsReservations = business["attributes"].get("RestaurantsReservations","N/A")
        RestaurantsTakeOut = business["attributes"].get("RestaurantsTakeOut","N/A")
        WiFi = business["attributes"].get("WiFi","N/A")
      
    #Step 3: Create the new variable itself   
    all_cities_2[i]["alcohol"] = Alcohol
    all_cities_2[i]["bikeparking"] = BikeParking
    all_cities_2[i]["creditcards"] = BusinessAcceptsCreditCards
    all_cities_2[i]["caters"] = Caters
    all_cities_2[i]["goodforkids"] = GoodForKids
    all_cities_2[i]["tv"] = HasTV
    all_cities_2[i]["noiselevel"] = NoiseLevel
    all_cities_2[i]["outdoorseating"] = OutdoorSeating
    all_cities_2[i]["attire"] = RestaurantsAttire
    all_cities_2[i]["delivery"] = RestaurantsDelivery
    all_cities_2[i]["goodforgroups"] = RestaurantsGoodForGroups
    all_cities_2[i]["pricerange"] = RestaurantsPriceRange2
    all_cities_2[i]["reservations"] = RestaurantsReservations
    all_cities_2[i]["takeout"] = RestaurantsTakeOut
    all_cities_2[i]["wifi"]= WiFi
    
    #SAS issue - has trouble reading in the "None" pricerange values
    #Setting these to 0 for now - will clean up in SAS later
    if business["pricerange"]=="None":
        all_cities_2[i]["pricerange"] = "0"
    
#THREE ADDITIONAL ATTRIBUTES
#Ambience, BusinessParking, and GoodForMeal are lists within the "attributes" list
#These need to be handled differently than the attributes above
        
#Creating a new list for each one. These are the keys in the key/value pair
ambience = ['touristy','casual','romantic','intimate','classy','hipster','divey','trendy','upscale']
businessparking = ['garage','street','validated','lot','valet']
goodformeal = ['dessert','latenight','lunch','dinner','brunch','breakfast']

#1. Ambience
for i, business in enumerate(all_cities_2):
    #When there is no "attributes", set them all to "N/A"
    if business["attributes"] is None: 
        for item in ambience:
            all_cities_2[i][item] = "N/A"
            
    #When "attributes" exists, but "Ambience" does not, set them all to "N/A"
    elif business["attributes"].get("Ambience") is None:
        for item in ambience:
            all_cities_2[i][item] = "N/A"
    
    #When "attributes" exists and "Ambience" exists, and is not equal to "None"
    elif business["attributes"].get("Ambience")!="None": 
        #print(type(business["attributes"]["Ambience"])) 
        New_Ambience = business["attributes"]["Ambience"].replace("'",'"').replace("True",'"True"').replace("False",'"False"')
        #print(New_Ambience)
        New_Ambience = json.loads(New_Ambience)
        #print(type(New_Ambience))
        for item in ambience:
            all_cities_2[i][item] = New_Ambience.get(item)
    #When "attributes" exists and "Ambience" exists, but is equal to "None", set them all to "N/A"
    else: 
        for item in ambience:
            all_cities_2[i][item] = "N/A"

#2. BusinessParking
for i, business in enumerate(all_cities_2):
    if business["attributes"] is None: 
        for item in businessparking:
            all_cities_2[i][item] = "N/A"
            
    elif business["attributes"].get("BusinessParking") is None:
        for item in businessparking:
            all_cities_2[i][item] = "N/A"
    
    elif business["attributes"].get("BusinessParking")!="None": 
        New_BP = business["attributes"]["BusinessParking"].replace("'",'"').replace("True",'"True"').replace("False",'"False"')
        New_BP = json.loads(New_BP)
        
        for item in businessparking:
            all_cities_2[i][item] = New_BP.get(item)
            
    else: 
        for item in businessparking:
            all_cities_2[i][item] = "N/A"
            
#3. GoodForMeal            
for i, business in enumerate(all_cities_2):
    if business["attributes"] is None: 
        for item in goodformeal:
            all_cities_2[i][item] = "N/A"
            
    elif business["attributes"].get("GoodForMeal") is None:
        for item in goodformeal:
            all_cities_2[i][item] = "N/A"
    
    elif business["attributes"].get("GoodForMeal")!="None": 
        New_GFM = business["attributes"]["GoodForMeal"].replace("'",'"').replace("True",'"True"').replace("False",'"False"')
        New_GFM = json.loads(New_GFM)
    
        for item in goodformeal:
            all_cities_2[i][item] = New_GFM.get(item)
            
    else: 
        for item in goodformeal:
            all_cities_2[i][item] = "N/A"
        
#Now that we have everything we need, we can output a final json file
with open("all_cities_2.json", "w") as file:
    json.dump(all_cities_2, file, indent=2)
    
#Create a final dataset that can be read into SAS for further data cleaning
    
#First creating an empty list
Final_Dataset = []

for business in all_cities_2:
    temp = {}
    temp["business_id"] = business["business_id"]
    temp["stars"] = business["stars"]
    temp["city"] = business["city"]
    temp["state"] = business["state"]
    temp["postal_code"] = business["postal_code"]
    temp["latitude"] = business["latitude"]
    temp["longitude"] = business["longitude"]
    temp["review_count"] = business["review_count"]
    temp["categories"] = business["categories"]
    temp["state"] = business["state"]
    
    #attributes
    temp["alcohol"] = business["alcohol"]
    temp["bikeparking"] = business["bikeparking"]
    temp["creditcards"] = business["creditcards"]
    temp["caters"] = business["caters"]
    temp["goodforkids"] = business["goodforkids"]
    temp["tv"] = business["tv"]
    temp["noiselevel"] = business["noiselevel"]
    temp["outdoorseating"] = business["outdoorseating"]
    temp["attire"] = business["attire"]
    temp["delivery"] = business["delivery"]
    temp["goodforgroups"] = business["goodforgroups"]
    temp["pricerange"] = business["pricerange"]
    temp["reservations"] = business["reservations"]
    temp["takeout"] = business["takeout"]
    temp["wifi"] = business["wifi"]
    
    #the special handling Attributes
    temp["touristy"] = business["touristy"]
    temp["casual"] = business["casual"]
    temp["romantic"] = business["romantic"]
    temp["intimate"] = business["intimate"]
    temp["classy"] = business["classy"]
    temp["hipster"] = business["hipster"]
    temp["divey"] = business["divey"]
    temp["trendy"] = business["trendy"]
    temp["upscale"] = business["upscale"]
    
    temp["garage"] = business["garage"]
    temp["street"] = business["street"]
    temp["validated"] = business["validated"]
    temp["lot"] = business["lot"]
    temp["valet"] = business["valet"]
    
    temp["dessert"] = business["dessert"]
    temp["latenight"] = business["latenight"]
    temp["lunch"] = business["lunch"]
    temp["dinner"] = business["dinner"]
    temp["brunch"] = business["brunch"]
    temp["breakfast"] = business["breakfast"]
    
    #Adding everything to the empty list
    Final_Dataset.append(temp)

#Printing out the first restaurant to see what it looks like
print(Final_Dataset[0])

#This dataset will be in a structure that I am more familiar with
FD = pd.DataFrame.from_records(Final_Dataset)

#Still 29,558 which is what we expect
print(len(FD))

#Printing out the first restaurants to see what it looks like
print(FD.head())

#Outputting a final csv file, which I will read into SAS for data cleaning
FD.to_csv('FD.csv', index=False)



#EXTRA - Before data cleaning, looked at yelp "categories" variable to see if there were any common categories
 
#Below steps were run for each of the 8 cities

#Creating an empty list   
categories = []  

#Pulling just the category and adding that to the above list

for business in all_cities_2: 
    category = business["categories"]
    categories.append(category)

#Within each line, remove the commas
categories = [line.replace(",", "") for line in categories]


#Creating a dictionary which we need for finding the counts
d = dict()

#For each word, keep track of the count
for line in categories:
    words = line.split()
    for w in words:    
        d[w] = d.get(w,0) + 1

#Print the dictionary      
print(d) 

#Sorting
sorted_d = sorted(d.items(), key=lambda kv: kv[1])
print(sorted_d)   

#End Result - ended up with 8 common categories:
#Bars, Nightlife, Pizza, American, Tea, Sandwiches, Mexican, Burgers
#These 8 categories will become new features during SAS data cleaning 
#Perhaps some of these categories will be significant in predicting star rating