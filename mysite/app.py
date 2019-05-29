from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/send')
def send():
  return render_template('send.html')

@app.route('/receive')
def receive():
  # { 
  #   'user': 'polar', 
  #   'message': 'hello' 
  # }
  user = request.args.get('user') # => 'polar'
  message = request.args.get('message') # => 'hello'
  return render_template('receive.html', user=user, message=message)

@app.route('/lotto_result')
def lotto_result():
  url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=844"
  response = requests.get(url)
  # response.text # => string
  lotto = response.json() # => dict
  winner = []
  for n in range(1, 7):
    winner.append(lotto[f'drwtNo{n}'])
  return render_template('lotto_result.html', lotto=winner)

if __name__ == '__main__':
  app.run(debug=True)
