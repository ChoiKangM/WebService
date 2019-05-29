from flask import Flask, render_template
from random import sample
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/mulcam")
def mulcam():
    return "This is Multicampus"

@app.route("/greeting/<string:name>")
def greeting(name):
  return f'반갑습니다. {name}!'

@app.route("/cube/<int:num>")
def cube(num):
  result = num ** 3 
  return f'{num}의 세제곱은 {result}'

# 사람 수 만큼 점심 메뉴 추천
@app.route("/lunch/<int:people>")
def lunch(people):
  menu = ["짜장면", "짬뽕", "라면", "브리또", "사과", "찜닭"]
  return f'{sample(menu, people)}'

@app.route("/html")
def html():
  multiple_string = """
    <h1>This is HTML</h1>
    <p>This is p tag</p>
  """
  return multiple_string

@app.route("/html_file")
def html_file():
  return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
  # Template Variable
  return render_template('hi.html', your_name=name)

@app.route("/menu")
def menu():
  menu = ["짜장면", "짬뽕", "라면", "브리또", "사과", "찜닭"]
  return render_template("menu_list.html", menu_list = menu)

# Flask를 쉽게 켜자
if __name__ == '__main__':
  app.run(debug=True)