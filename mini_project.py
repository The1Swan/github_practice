# Restaurant Ranker
restaurants = []
thing = True
while thing:
  new_restaurant = input("What restaurant would you like to add to the list?")
  if new_restaurant == "stop":
    break
  else:
    restaurants.append(new_restaurant)

print(restaurants)