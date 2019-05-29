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
  bonus = int(lotto['bnusNo'])
  winner = f'{a} + {bonus}'

  # my_numbers 가져오기
  my_numbers = [int(n) for n in request.args.get('my_numbers').split()]
  # => [1, 2, 3, 4, 5, 6]

  # 같은 숫자 갯수
  # set(a) = {1, 4, 10, 12, 28, 45}
  # set(my_numbers) = {1, 2, 3, 4, 5, 6}
  # set() => {1, 2, 3, 4}
  # 교집합 : set(a) & set(b)
  # 합집합 : set(a) | set(b)
  matched = len(set(a) & set(my_numbers))

  # 같은 숫자의 갯수에 따른 등수
  if matched == 6:
    result = '1등입니다'
  elif matched == 5:
    if bonus in my_numbers:
      result = '2등입니다'
    result = '3등입니다'
  elif matched == 4:
    result = '4등입니다'
  elif matched == 3:
    result = '5등입니다'
  else:
    result = '꽝입니다'
  
  

  return render_template('lotto_result.html', lotto=winner, bonus=bonus, my_numbers=my_numbers,result=result)



if __name__ == '__main__':
  app.run(debug=True)
