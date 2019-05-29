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
  # for n in range(1, 7):
  #   winner.append(lotto[f'drwtNo{n}'])
  
  # list comprehension
  # a = [n*2 for n in range(1, 7)] # => [2, 4, 6, 8, 10, 12]
  a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
  bonus = lotto['bnusNo']
  winner = f'{a} + {bonus}'
  return render_template('lotto_result.html', lotto=winner, bonus=bonus)



if __name__ == '__main__':
  app.run(debug=True)
