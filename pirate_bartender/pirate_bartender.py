import random

#Dictonaries for pirate bartender project
questions = {
  "strong":"Do ye like yer drinks strong?",
  "salty":"Do ye like it with a salty tang?",
  "bitter":"Are ye a lubber who likes it bitter?",
  "sweet":"Would you like a bit of sweetness with yer poison?",
  "fruity":"Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def picking_pref():
  """Ask the questions in question dictionary and replace the answers with boolean answers """
  quest_ans = {}
  """Get preferences from the user and prompt them to answer questions"""
  for key in questions:
    print questions[key]
    temp = raw_input("Please enter yes or y: ").lower()
    quest_ans[key] = temp == "y" or temp == "yes"
  return quest_ans  

def cons_drink(quest_ans):
  drinks = []
  for key2 in quest_ans:
    if quest_ans[key2] == True:
      drinks.append(random.choice(ingredients[key2]))
    else:
      continue
  return drinks    

def main():
  pref1 = picking_pref()
  drink1 = cons_drink(pref1)
  print "Those are some good preferences"
  print "There are a lot of good ingredients in there..."
  for ingred in drink1:
    print "A {}".format(ingred)
  firstName = str(raw_input("What would you like to be the first name of your drink? (name an adjective) "))
  secondName = str(raw_input("What would you like to be the second name of your drink? (name a noun) "))
  print ("It has been decided! Your drink name is the %s %s!") % (firstName, secondName)


if __name__ == '__main__':
  main()
      
      
      
  
  

