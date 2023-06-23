class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    bill = 0
    for item in purchased_items:
      for key,value in self.items.items():
        if item == key:
          bill += value
    return bill

class Franchise:
  def __init__(self, address, menu):
    self.address = address
    self.menu = menu
  def __repr__(self):
    return "Our store is located at {location}".format(location = self.address)

  def available_menus(self, time):
    self.time = time
    menu_list= []
    for menu in self.menu:
      if time >= menu.start_time and time <= menu.end_time:
        for keys in menu.items:
          menu_list.append(keys)
    print(menu_list)

class Business:
  def __init__(self, name,franchises):
    self.name = name
    self.franchises = franchises

#Brunch: 11am to 4pm
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11,16)

#Early-bird: 3pm to 6pm
early_bird = Menu("Early-bird Dinner", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},15,18)

#Dinner: 5pm to 11pm
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},14,20)

#Kids: 11am to 9pm
kids = Menu("Kids' Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)

#Arepa
arepas_menu = Menu("Arepas' Menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

arepas_place = Franchise("189 Fitzgerald", [arepas_menu])

arepas_business = Business("Take a'Arepa!", [arepas_place])

#Franchises
flagship_store = Franchise("1232 West End Road", [brunch,early_bird,dinner,kids])

new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

#Business
first_business = ("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
