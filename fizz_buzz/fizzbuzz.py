#n = int(raw_input("What is the upper limit?"))

while True: 
  try:
    n = int(raw_input("What is the upper limit? (enter an integer): "))
    break
  except ValueError:
    print "That was not a valid entry. Try again... please enter an integer."

print "Fizzbuzz counting up to " + str(n)

for x in range(1,n+1):
  if x % 3 == 0 and x % 5 == 0:
    print "fizzbuzz"
  elif x % 3 == 0:
    print "fizz"
  elif x % 5 == 0:
    print "buzz"
  else:
    print x