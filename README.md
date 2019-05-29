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

사람수 만큼 점심메뉴 뽑기
  - 메뉴 수 보다 많은 사람 수?
  - 중복 가능하도록?

## 3교시

