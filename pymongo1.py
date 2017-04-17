# -*- coding: utf-8 -*-
import pymongo
import random
from pymongo import MongoClient

client=MongoClient()
print client
MongoClient('localhost', 27017)
conn=pymongo.MongoClient('localhost', 27017)
db=conn.data


for id in range(2,10):
    name=random.choice(['Steve','Sophia','Bob','Lilian','susuan'])
    sex = random.choice(['male', 'female'])
    db.user.insert({'id': id, 'name':name, 'sex':sex})
    content=db.user.find()
    for i in content:
        print i

result=db.user.distinct('id')

print result
for m in result:
    num=db.user.find({'id':m}).count()
    db.customer.insert({'id':m,'count':num})
    content1=db.customer.find()
for l in content1:
        print l




    #代码目的，先创造一个user表，存放({'id': id, 'name': 'male', 'sex': 'female'}
    #将所有不同的id作为表头，创建表，建立一列count列，根据不同的id检索各个id出现次数计入count列
