def pizza():
  pizza_cost = 0
  print("small pizza is 20
, large pizza is 40$.")
  size = input("What size pizza do you want? S, M, or L ").title()
  if size == 'S':
    pizza_cost += 20
  elif size == 'M':
    pizza_cost += 30
  else:
    pizza_cost += 40
  add_pepperoni = input("Do you want pepperoni Y or N ").title()
  if add_pepperoni == 'Y':
    peppy = input("What size pepperoni do you want? S, M, or L ").title()
    if peppy == 'S':
      if size == 'S':
        pizza_cost += 3
      elif size == "M":
        pizza_cost += 4
      else:
        pizza_cost += 6
    elif peppy == "M":
      if size == 'S':
        pizza_cost += 6
      elif size == "M":
        pizza_cost += 8
      else:
        pizza_cost += 10
    elif peppy == "L":
      if size == 'S':
        pizza_cost += 10
      elif size == "M":
        pizza_cost += 12
      else:
        pizza_cost += 14
    else:
      print("Are you a scammer, leave!")
  extra_cheese = input(
      "Do you want extra cheese 5$ for any size pizza? Y or N ").title()
  if extra_cheese == 'Y':
    t = int(input("How many cheese do you want?(1-10) "))
    if t == 0:
      pizza_cost += 5
    else:
      pizza_cost += t * 5

  add_ingreediants = input(
      "do you want jalopeno, pineapple, basil, or olives, or pepper 4$ for each? Y or N "
  ).title()
  if add_ingreediants == 'Y':
    howmuch = int(input(f"how many ingrediants do you want?(number) "))
    if howmuch == 0:
      print("Are you a scammer, leave!")
    else:
      pizza_cost += howmuch * 4
  payment = int(
      input("How much is your payment?(you never know the total price) "))
  change = payment - pizza_cost
  print('here is your pizza🍕')
  if payment < pizza_cost:
    not_enough_money = input(
        'not enough money do you promise to give me money later? Y or N '
    ).title()
    if not_enough_money == 'Y':
      print("go to the bank now")
      bank = int(
          input("how much did you borrow?(NUMBER ONLY, NO DOLLAR SIGN) "))
      if bank == '0':
        print("scram brokie")
        exit()
      elif bank + payment != pizza_cost:
        print("you are a bad person and scram")
        exit()
    else:
      print(f"your change is {change}")
  else:
    print(f"your change is {change}")

  #why and (more pizza (if wanted))


want_pizza = True
print("Welcome to Python Pizza Deliveries!")
pizza()
while want_pizza:
  more_pizza = input("Do you want more pizza? Y or N ").title()
  if more_pizza == "Y":
    pizza()
  else:
    print("scram now and leave")

    want_pizza = False
    exit()
