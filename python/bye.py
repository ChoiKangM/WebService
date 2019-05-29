def hello(func):
  def wrapper():
    print('hihi')
    func() #=> bye()
    print('hihi')
  return wrapper()
  
@hello
def bye():
  print('bye bye')

# bye()