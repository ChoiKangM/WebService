from flask import Flask, render_template, request
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

if __name__ == '__main__':
  app.run(debug=True)
