from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.testIDD  # 'testID'라는 이름의 db를 만듭니다.

import random


# @app.route('/')
# def home():
#     return 'Way Back Home!'


@app.route('/')
def home():
    return render_template('youtube_login.html')


@app.route('/mypage')
def mypage():
    return render_template('calendar_card.html')


# @app.route('/post', methods=['POST'])
# def post():
#     print('sdfs')
#     print(request.form['test'])
#     return jsonify({'result': 'success'})
#
#     # url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
#     # ID_receive = request.form['ID_give']  # 클라이언트로부터 comment를 받는 부분
#     # info = {'ID': ID_receive, 'url': url_receive}
#     # db.testID.insert_one(info)


########## 체크인 관련 DB##########################

@app.route('/postCheckin', methods=['POST'])
def postCheckin():
    # 클라이언트로부터 데이터를 받는 부분
    date_receive = request.form['date_give']
    day_receive = request.form['day_give']

    # mongoDB에 넣는 부분
    checkinData = {'Date': date_receive, 'Day': day_receive}
    # dummyData = {'Date': 4/1, 'Day': 'sadfdsa'}

    db.CheckInTest.insert_one(checkinData)
    # db.CheckInTest.insert_one(dummyData)

    return jsonify({'result': 'success'})


@app.route('/postCheckin', methods=['GET'])
def test_get():
    # URL_receive = request.args.get('URL')
    checkinInfo = db.CheckInTest.find({}, {'_id': 0})
    # print(list(checkinInfo))
    # print('sdfdsfdsfdsfdsfas')
    return jsonify({'result': 'success', 'CheckInTest': list(checkinInfo)})


# ########   YOUTUBE 관련 DB  ################


@app.route('/post', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content)
    db.personalInfo.insert(content)
    # return render_template('calendar_card.html')
    # 중복제거
    # db.testIDD.distinct("ownerID" and "URLz")
    print('mypage')
    # mypage()
    return 'JSON posted'


@app.route('/post', methods=['GET'])
def view():
    pInfo = db.personalInfo.find({}, {'_id': 0})

    print("dsfds")
    # print(jsonify(pInfo))
    #
    # randomInfo1 = random.choice(list(pInfo))
    # randomInfo2 = random.choice(list(pInfo))
    # randomInfo3 = random.choice(list(pInfo))
    # randomInfo4 = random.choice(list(pInfo))
    # print(randomInfo1)
    # print(randomInfo2)
    # print(randomInfo3)
    # print(randomInfo4)
    return jsonify({'result': 'success', 'personalInfo': list(pInfo)})


# @app.route('/get', methods=['POST'])
# def test_get():
#     return 'helloooo'
#     ID_receive = request.args.get('ID_give')
#     # URL_receive = request.args.get('URL')
#     ID_info = db.testID.find_one({'ID': ID_receive}, {'_id': 0})
#     # print(ID_receive)
#     return jsonify({'result': 'success', 'Info': ID_info})

# @app.route('/test', methods=['GET'])
# def test_get():
#     # return 'helloooo'
#     ID_receive = request.args.get('ID_give')
#     print(ID_receive)
#     # URL_receive = request.args.get('URL')
#     ID_info = db.testID.find_one({'ID': ID_receive}, {'_id': 0})
#     # print(ID_receive)
#     return jsonify({'result': 'success', 'msg': ID_info})


# ## API 역할을 하는 부분
# @app.route('/post', methods=['POST'])
# def saving():
# 	# 클라이언트로부터 데이터를 받는 부분
#     ID_receive = request.form['ID_give']
#
# 	# meta tag를 스크래핑 하는 부분
#
#
#     URL_receive = request.form['URL_give']
#     CheckIn_receive = request.form['CheckIn_give']
#
#     # mongoDB에 넣는 부분
#     data = {'ID': ID_receive, 'URL': URL_receive, 'CheckIn': CheckIn_receive}
#
#     db.testID.insert_one(data)
#
#     return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
