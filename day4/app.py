# 0. flask 패키지 가져오기
import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import random


# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html',name=name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html',menus=menus,pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서 
    text = request.args.get('say')
    print(request.args)
    # 템플릿에 넘겨준다.
    return render_template('pong.html',text=text)

@app.route('/today_luck')
def today_luck():
    return render_template('today_luck.html')

@app.route('/result_luck')
def result_luck():
    # 사용자가 보낸 데이터를 받아와서 
    text = request.args.get('year')
    print(request.args)
    # 템플릿에 넘겨준다.
    return render_template('result_luck.html',text=int(text))

if __name__ == '__main__':
    app.run(debug = True)

#http://85a04c1a.ngrok.io