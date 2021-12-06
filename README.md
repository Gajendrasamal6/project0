"This repository is all about project_0 which is using mongoDb in shell and pymongo "
# Analyze Zipcode data

## Project Description

i set up mongodb environment and add all data into the respective folder and perfrom operation.
## Technologies Used

* MongoDb
* pymongo
* Git -version 2.32.0.windows.1

## Features

List of features ready and TODOs for future development
using this project some query are solved using Mongodb and pymongo ,following questions are listed below:

01. Write a MongoDB query to display all the documents in the collection restaurants.

02. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.

03. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.

04. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.

05. Write a MongoDB query to display all the restaurant which is in the borough Bronx.

06. Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.

07. Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.

08. Write a MongoDB query to find the restaurants who achieved a score more than 90.

09. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.

10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.Go to the editor

11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.
	
	db.restaurants.find({$and:[{"cuisine" : {$ne :"American "}}, {"grades.score" : {$gt : 70}}, {"address.coord" : {$lt : -65.754168}} ] } ).pretty()

12. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
Note : Do this query without using $and operator.
	
	db.restaurants.find({"cuisine" : {$ne : "American "},"grades.score" :{$gt: 70},"address.coord":{$lt : -65.754168}}).pretty()

13. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.
	
	db.restaurants.find({$and:[{"cuisine" : {$ne :"American "}}, {"grades.grade" : {$gte : "A"}}, {"borough" : {$ne :"Brooklyn"}} ] } ).sort({cuisine:-1})pretty()

14. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.
	db.restaurants.find({name: {$regex: /^Wil/i}},{name:1,restaurant_id:1,borough:1,cuisine:1}).pretty()
15. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces' as last three letters for its name.
	db.restaurants.find({name: {$regex: /ces$/i}},{name:1,restaurant_id:1,borough:1,cuisine:1}).pretty()
16. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name.
	db.restaurants.find({name: {$regex: /.*Reg.*/i}},{name:1,restaurant_id:1,borough:1,cuisine:1}).pretty()
17. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.
	db.restaurants.find({},{})
18. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.

19. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.

20. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.

21. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'.

22. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..

23. Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z".

24. Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52..

25. Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.

26. Write a MongoDB query to arrange the name of the restaurants in descending along with all the columns.

27. Write a MongoDB query to arranged the name of the cuisine in ascending order and for that same cuisine borough should be in descending order.

28. Write a MongoDB query to know whether all the addresses contains the street or not.

29. Write a MongoDB query which will select all documents in the restaurants collection where the coord field value is Double.

30. Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.

31. Write a MongoDB query to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.

32. Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.







## Getting Started
   

To start this project user need to install MongoDB in your system and follow the below procedure 

#to_start the mongo db shell
"C:\Program Files\MongoDB\Server\5.0\bin\mongod" --dbpath="c:\data\db"

#AFTER THIS OPEN ANOTHER CMD AND TYPE:
"C:\Program Files\MongoDB\Server\5.0\bin\mongo"

#to check how many database are there
show dbs 

#go to that file where from import
cd "C:\Users\USER\Desktop\project(p0)"


#import json file into mongo shell
"C:\Program Files\MongoDB\mongodb import\bin\mongoimport" --db products --collection restaurants --type json --file restaurants.json

#again start mongo shell command using "c:\program........\bin\mongo"

>> use products
>>db.getCollectionNames()
>>db.restaurants.find()
>>db.restaurants.find().pretty()


## Usage

>Using this project any one can perform analysis with the Zipcode dataset





