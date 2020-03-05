from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.testIDD  # 'testID'라는 이름의 db를 만듭니다.


# db.CheckInTest.insert_one({"Date": "1/1", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/4", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/8", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/11", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/15", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/18", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/22", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/25", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "1/29", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/1", "Day": "Saturday"}, {'_id': 0})
#
# db.CheckInTest.insert_one({"Date": "2/2", "Day": "Sunday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/3", "Day": "Monday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/5", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/7", "Day": "Friday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/8", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/9", "Day": "Sunday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/12", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/13", "Day": "Thursday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/14", "Day": "Friday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/15", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/16", "Day": "Sunday"}, {'_id': 0})
#
# db.CheckInTest.insert_one({"Date": "2/19", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/20", "Day": "Thursday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/22", "Day": "Saturday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/26", "Day": "Wednesday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/27", "Day": "Thursday"}, {'_id': 0})
# db.CheckInTest.insert_one({"Date": "2/28", "Day": "Friday"}, {'_id': 0})


# MongoDB에 insert 하기(완료)
# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.testIDD.insert_one({"ownerID": "jjjj",
#                       "URLz": "https://www.youtube.com/watch?v=N6nf4lYF8A0&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp",
#                       "Title": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
#                        "thumbnailURL"
# }
#                       )
# db.testIDD.insert_one({"ownerID": "jjjj",
#                       "URLz": "https://www.youtube.com/watch?v=qwZ0yAQA-QI&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"})
# db.testIDD.insert_one({"ownerID": "jjjj",
#                       "URLz": "https://www.youtube.com/watch?v=qwZ0yAQA-QI&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"})
#
# db.testIDD.insert_one({"ownerID": "jjjj",
#                       "URLz": "https://www.youtube.com/watch?v=EOwFs_0CfUw&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"})

## MongoDB에 delete 하기
# db.testID.delete_one({'ID':'sunny99'})
# db.testID.delete_one({'ID':'jeff94'})
# db.testID.delete_one({'ID':'justin97'})
# /* 1 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cebe"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=N6nf4lYF8A0&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
#
# /* 2 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cebf"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=dGJya2dpjko&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
#
# /* 3 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cec0"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=qwZ0yAQA-QI&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
#
# /* 4 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cec1"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=EOwFs_0CfUw&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
#
# /* 5 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cec2"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=sVAA3NfsLj4&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
#
# /* 6 */
# {
#     "_id" : ObjectId("5e590f0e361072b1c931cec3"),
#     "ownerID" : "jjjj",
#     "URLz" : "https://www.youtube.com/watch?v=BQrKb-1IJOc&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp"
# }
