from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/hi")
def hi():
    return render_template('hi.html')

@app.route("/hul/<string:name>")
def higyo(name):
    return render_template('hul.html', name = name)

# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route("/lotto")
def lotto():
    num_list = list(range(1,46))
    choice = random.sample(num_list,6)
    return f'이번주 당첨번호는 {choice}'

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route("/cube/<int:num>")
def cube(num):
    return f"<h1>{num**3}</h1>"

# /lunch/사람이름
# 사람아 menu 먹어
@app.route("/lunch/<string:name>")
def lunch(name):
    lunch_list = ['한식', '스페셜A', '스페셜B']
    lunch_menu = random.choice(lunch_list)
    return render_template('lunch.html', name=name, lunch_menu=lunch_menu)

# sever를 동적으로 변경
if __name__ == '__main__':
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)