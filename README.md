# WebService
## 1교시
`Web Service` 도입  

`WWW` : World Wide Web  

현실세계의 `Service` -> `Web Service`  

`Client`, `Server`

`Get`, `Post`

`Python` + [`Flask`](http://flask.pocoo.org/)  

```bash
$ pip install Flask
$ FLASK_APP=hello.py flask run
```
```bash
$ FLASK_DEBUG=1 FLASK_APP=hello.py flask run
```

`hello.py`
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/mulcam")
def mulcam():
    return "This is Multicampus"

# Flask를 쉽게 켜자
if __name__ == '__main__':
  app.run(debug=True)
```
명령어가 많이 줄어듬
```bash
$ python hello.py
```

## 2교시
`__name__`  

<del>`import`, `def`</del>  

`decorator`: `bye.py`

`variable routing`, `path variable`
  - `string`
  - `int`

사람 수 만큼 점심메뉴 뽑기
  - 메뉴 수 보다 많은 사람 수?
  - 중복 가능하도록?

`hello.py`
```python
from flask import Flask
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

# Flask를 쉽게 켜자
if __name__ == '__main__':
  app.run(debug=True)
```

## 3교시
랜더링
  - `html tag` 
    ```python
    @app.route("/html")
    def html():
      multiple_string = """
        <h1>This is HTML</h1>
        <p>This is p tag</p>
      """
      return multiple_string
    ```
  - `.html` + `/templates` + `render_template`
    ```python
    @app.route("/html_file")
    def html_file():
      return render_template('html_file.html')
    ```
  - `Template Variable` - `jinja`
    ```python
    @app.route("/hi/<string:name>")
    def hi(name):
      # Template Variable
      return render_template('hi.html', your_name=name)
    ```

`html`파일에서 파이썬 문법 사용하기
```html
{% for menu in menu_list %}
  <li>{{ menu }}</li>
{% endfor %}
```

## 4교시
`send` # `form` => `receive`

`request.arg.get`

## 5교시
[신이 나를 만들 때](https://kr.vonvon.me/quiz/329) 같이  
URL로 정보 넘기기 `실습`

## 6교시
`JSON`

`dict`
  1. dict 생성
  2. dict item 추가
  3. dict value 가져오기
  4. dict 반복문 활용
    4-1. 기본
    4-2. key 반복
    4-3. value 반복
    4-4. key, value 반복

[`lotto`](https://dhlottery.co.kr/)
`lotto API`, `requests`, `JSON`, `append`

## 7교시
`list comprehension`

`회차 입력`

```python
@app.route('/lotto_check')
def lotto_check():
  return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
  lotto_round = request.args.get('lotto_round')
  url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}"
  response = requests.get(url)
  # response.text # => string
  lotto = response.json() # => dict
  winner = []
  
  # list comprehension
  # a = [n*2 for n in range(1, 7)] # => [2, 4, 6, 8, 10, 12]
  a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
  bonus = lotto['bnusNo']
  winner = f'{a} + {bonus}'
  return render_template('lotto_result.html', lotto=winner, bonus=bonus)
```

## 8교시
`등수 확인`

`Set` = `{요소1, 요소2, ...}` : 집합
  - `&`(합집합), `|`(교집합)

`in`, `len`


