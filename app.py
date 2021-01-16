from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.
client = MongoClient('localhost', 27017)
db = client.seoul_artgallery

@app.route('/')
def home():
    return render_template('map_page.html')

@app.route('/artgallery', methods=["GET"])
def get_artgallery():
    # gu_receive 라는 변수에 전달받은 구 이름을 저장합니다.
    gu_receive = request.args.get('gu_give')
    # 구 이름에 해당하는 모든 미술관 목록을 불러옵니다.
    artgallery_list = list(db.artgallery.find({'gu': gu_receive}, {'_id': False}))
    # artgallery_list 라는 키 값에 미술관 목록을 담아 클라이언트에게 반환합니다.
    return jsonify({'result': 'success', 'artgallery_list': artgallery_list})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
