import json
from bson import ObjectId
import pymongo


# 数据库列表
def listDB(mgClient):
    print('listDB ------------')
    dbList = mgClient.list_database_names()
    for db in dbList:
        print(db)


# 创建数据库，并插入数据
def createDB(mgClient):
    print('createDB ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    dic = {"a": "2", "b": "22"}
    mycol.insert_one(dic)


# 创建数据库，并插入数据(数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建)
def findAllCollection(mgClient):
    print('findCollection ------------')
    myDB = mgClient["demo"]
    collections = myDB.list_collection_names()
    for col in collections:
        print(col)


# 查询单个
def find(mgClient):
    print('find ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    doc = mycol.find_one()
    print(doc)


# 查询 demo 库下面所有 collection a字段倒序(1 为升序，-1 为降序，默认为升序)
def findAll(mgClient):
    print('findAll ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    for doc in mycol.find().sort("a", -1):
        print(doc)


# 查询指定条件，显示特定字段
def findBy(mgClient):
    print('findBy ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1（默认是1）
    # 查询结果 _id不显示 a显示 b显示
    for doc in mycol.find({}, {"_id": "0", "a": 1, "b": 1}):
        print(doc)
    # 查询结果 a不显示 其余都显示
    for doc in mycol.find({}, {"a": 0}):
        print(doc)
    # 查询结果 都显示 查询条件a=1
    for doc in mycol.find({"a": "1"}, {"a": 1, "b": 1}):
        print(doc)
    else:
        print("未找到")
    # 高级查询，查询结果 _id不显示 查询条件a>1 json格式化输出
    for doc in mycol.find({"a": {"$gt": "1"}}, {"_id": 0}):
        print(json.dumps(dict(doc), sort_keys=True, indent=2, separators=(',', ':')))
    print('------------')
    # 高级查询，查询结果 _id不显示 查询条件匹配2个长度正则 json格式化输出
    for doc in mycol.find({"b": {"$regex": "^.{2}$"}}, {"_id": 0}):
        print(json.dumps(dict(doc), sort_keys=True, indent=2, separators=(',', ':')))


# 更新
def update(mgClient):
    print('update ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.update_many({"a": "2"}, {"$set": {"b": "345"}})
    print(doc.modified_count)


# 更新 模糊查找
def updateLike(mgClient):
    print('updateLike ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.update_many({"b": {"$regex": "^.{1}$"}}, {"$set": {"b": "345"}})
    print(doc.modified_count)


# 删除
def delete(mgClient):
    print('delete ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.delete_many({"_id": ObjectId('60069fac7e7a96e21e5d7181')})
    print(doc.deleted_count)


# 删除所有
def deleteAll(mgClient):
    print('deleteAll ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.delete_many({})
    print(doc.deleted_count)


# 删除 collection
def deleteCollection(mgClient):
    print('deleteCollection ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    mycol.drop()


# 删除 db
def deletDB(mgClient):
    print('deletDB ------------')
    myDb = mgClient["demo"]
    myDb.command("dropDatabase")


if __name__ == '__main__':
    mgClient = pymongo.MongoClient('mongodb://192.168.13.220:27017')
    # createDB(mgClient)
    # find(mgClient)
    # findBy(mgClient)
    # update(mgClient)
    # updateLike(mgClient)
    # delete(mgClient)
    # deleteAll(mgClient)
    # findAll(mgClient)
    # deleteCollection(mgClient)
    # findAllCollection(mgClient)
    # deletDB(mgClient)
    # listDB(mgClient)

