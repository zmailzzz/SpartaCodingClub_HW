
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.testID  # 'testID'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기(완료)
# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.testID.insert_one({'ID': 'jeff', 'URL': 'https://www.youtube.com/watch?v=dpkK6O8rpI0'})
# db.testID.insert_one({'ID': 'sunny99', 'URL': 'https://www.youtube.com/watch?v=xubBTDqbfUc'})
# db.testID.insert_one({'ID': 'justin97', 'URL': 'https://www.youtube.com/watch?v=CAfDN3m4Qeo'})

## MongoDB에 delete 하기
# db.testID.delete_one({'ID':'sunny99'})
# db.testID.delete_one({'ID':'jeff94'})
# db.testID.delete_one({'ID':'justin97'})
