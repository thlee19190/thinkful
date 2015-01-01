def subtractor(a,b):
  """I subtract b from a and return the result"""
  print "I am a function. My name is {}".format(subtractor.__name__)
  print "I am about to subtract {} and {} \n\n".format(a,b)
  return a-b

def print_function():
  """I am also a function but I don't take any parameters"""
  print "I am {}, and I am printing now".format(print_function.__name__)
  
def function3(a=1,b=1):
  """I am a function that calls other functions"""
  print "I'm {} and I am about to call on the subtractor functions".format(function3.__name__)
  total = subtractor(a,b)
  print_function()
  print "I'm {} and I am about to return the total".format(function3.__name__)
  return total

if __name__ == '__main__': 
  total = function3(5,4)
  print "total is {}".format(total)
