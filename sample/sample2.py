def side_effect_test(value):
  """Do something to modify the value"""
  value[1] = "orange"
  print "inside the function, the value becomes {}".format(value)
  
if __name__ == "__main__":
  #create the value
  value = ["red","green","blue"]
  
  print "outside the function, the value starts at {}".format(value)
  
  side_effect_test(value)
  
  print "outside the function, the value is now {}".format(value)