from pymongo import MongoClient
from pprint import pprint
# Establish connection.
client = MongoClient() #creating object from mongoClient
db = client.products 
print(db)
print(db.list_collection_names())
x = db.restaurants
#Question 1 .======================================================
# restaurants=x.find()
# for k in restaurants:
#     pprint(k)
# #Question 2.=======================================================
# restaurants=x.find({},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1})
# for k in restaurants:
#     pprint(k)
# # #Question 3========================================================
# restaurants=x.find({},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1,"_id":0})
# for k in restaurants:
#     pprint(k)
##Question 4 =======================================================
# restaurants=x.find({},{"name":1,"restaurant_id":1,"borough":1,"zipcode":1,"_id":0})
# for k in restaurants:
#     pprint(k)
##Question 5========================================================
# restaurants=x.find({"borough":"Bronx"})
# for k in restaurants:
#     pprint(k)
##Question 6 =========================================================
# restaurants=x.find({"borough":"Bronx"}).limit(5)
# for k in restaurants:
#     pprint(k)
##Question 7 =========================================================
# restaurants=x.find({"borough":"Bronx"}).skip(5).limit(5)
# for k in restaurants:
#     pprint(k)
##Question 8 ==========================================================
# restaurants=x.find({"grades" : { "$elemMatch":{"score":{"$gt" : 90}}}})
# for k in restaurants:
#     pprint(k)
##Question 9 ==========================================================
# restaurants=x.find({"grades" : { "$elemMatch":{"score":{"$gt" : 80,"$lt":100}}}})
# for k in restaurants:
#     pprint(k)
##Question 10 ===========================================================
# restaurants=x.find({"address.coord":{"$lt":[-95.754168]}})
# for k in restaurants:
#     pprint(k)
##Question 11 ===========================================================
# restaurants=x.find({"$and":[{"cuisine" : {"$ne" :"American "}}, {"grades.score" : {"$gt" : 70}}, {"address.coord" : {"$lt" : -65.754168}} ] })
# for k in restaurants:
#     pprint(k)
#Question 12 ============================================================
# restaurants=x.find({"cuisine" : {"$ne" :"American "}, "grades.score" : {"$gt" : 70}, "address.coord" : {"$lt" : -65.754168} })
# for k in restaurants:
#     pprint(k)
#Question 13 ============================================================
# from pymongo import  ASCENDING, DESCENDING
# restaurants=x.find({"$and":[{"cuisine" : {"$ne" :"American "}}, {"grades.grade" : {"$gte" : "A"}}, {"borough" : {"$ne" :"Brooklyn"}} ] } ).sort([('cuisine', DESCENDING)])
# for k in restaurants:
#     pprint(k)
# #Question 14 ============================================================
# restaurants=x.find({"name": {"$regex": "^Wil"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1} )
# for k in restaurants:
#     pprint(k)
# #Question 15 ============================================================
# restaurants=x.find({"name": {"$regex": "ces$"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1} )
# for k in restaurants:
#     pprint(k)
# #Question 16 ============================================================
# restaurants=x.find({"name": {"$regex": ".*Reg.*"}},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1} )
# for k in restaurants:
#     pprint(k)
# #Question 17 ============================================================
# restaurants=x.find({  "borough": "Bronx" ,  "$or" : [ { "cuisine" : "American " }, { "cuisine" : "Chinese" } ]  } )
# for k in restaurants:
#     pprint(k)
# #Question 18 ============================================================
# restaurants=x.find({"borough" :{"$in" :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } )
# for k in restaurants:
#     pprint(k)
# #Question 19 ============================================================
# restaurants=x.find({"borough" :{"$nin" :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } )
# for k in restaurants:
#     pprint(k)
# #Question 20 ============================================================
# restaurants=x.find({"grades" : { "$elemMatch":{"score":{"$lt":10}}}},{ "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 })
# for  k in restaurants:
#     pprint(k)
# #Question 21 ============================================================
# restaurants=x.find({"$or": [{"name": "^Wil"},{"$and": [{"cuisine" : {"$ne" :"American "}},{"cuisine" : {"$ne" :"Chinees"}}]}]} ,{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1})
# for  k in restaurants:
#     pprint(k)
# # #Question 22 ============================================================not
# restaurants=x.find({"grades.date.ISODate":{"ISODate":("2014-08-11T00:00:00Z")},"grades.grade":"A" ,"grades.score" : 11},{"restaurant_id" : 1,"name":1,"grades":1})
# for  k in restaurants:
#     pprint(k)
# #Question 23 ============================================================not
# restaurants=x.find({ "grades.1.date": "ISODate"("2014-08-11T00:00:00Z"),"grades.1.grade":"A" ,"grades.1.score" : 9},{"restaurant_id" : 1,"name":1,"grades":1})
# for  k in restaurants:
#     pprint(k)
# # #Question 24 ============================================================
# restaurants=x.find({"address.coord.1": {"$gt" : 42, "$lte" : 52}},{"restaurant_id" : 1,"name":1,"address":1,"coord":1})
# for  k in restaurants:
#     pprint(k)
# #Question 25 ============================================================
# from pymongo import  ASCENDING, DESCENDING
# restaurants=x.find().sort([('name', ASCENDING)])
# for  k in restaurants:
#     pprint(k)
# #Question 26 ============================================================
# from pymongo import  ASCENDING, DESCENDING
# restaurants=x.find().sort([('name', DESCENDING)])
# for  k in restaurants:
#     pprint(k)
# #Question 27 ============================================================
# from pymongo import  ASCENDING, DESCENDING
# restaurants=x.find().sort([("cuisine",ASCENDING),("borough",DESCENDING)])
# for  k in restaurants:
#     pprint(k)
# #Question 28 =============================================================
# restaurants=x.find({"address.street" :{ "$exists" : "true" }})
# for  k in restaurants:
#     pprint(k)
# #Question 29 =============================================================
# restaurants=x.find({"address.coord" :{"$type" : 1}})
# for  k in restaurants:
#     pprint(k)
# #Question 30 =============================================================
# restaurants=x.find({"grades.score" :{"$mod" : [7,0]}},{"restaurant_id" : 1,"name":1,"grades":1})
# for  k in restaurants:
#     pprint(k)
# #Question 31 =============================================================
restaurants=x.find({"name" :{ "$regex": ".*mon.*"}},{"name":1,"borough":1,"address.coord":1,"cuisine" :1})
for  k in restaurants:
    pprint(k)
# # #Question 32 =============================================================
# restaurants=x.find({"name" :{ "$regex": "^mad"}},{"name":1,"borough":1,"address.coord":1,"cuisine" :1})
# for  k in restaurants:
#     pprint(k)








