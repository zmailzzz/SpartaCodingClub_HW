from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.testID  # 'testID'라는 이름의 db를 만듭니다.


# @app.route('/')
# def home():
#     return 'Way Back Home!'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mypage')
def mypage():
    return 'This is My Page!'

# @app.route('/get', methods=['POST'])
# def test_get():
#     return 'helloooo'
#     ID_receive = request.args.get('ID_give')
#     # URL_receive = request.args.get('URL')
#     ID_info = db.testID.find_one({'ID': ID_receive}, {'_id': 0})
#     # print(ID_receive)
#     return jsonify({'result': 'success', 'Info': ID_info})




@app.route('/get', methods=['GET'])
def test_get():
    # return 'helloooo'
    ID_receive = request.args.get('ID_give')
    print(ID_receive)
    # URL_receive = request.args.get('URL')
    ID_info = db.testID.find_one({'ID': ID_receive}, {'_id': 0})
    # print(ID_receive)
    return jsonify({'result': 'success', 'msg': ID_info})

#
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
