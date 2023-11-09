from shirt import Shirt

new_shirt  = Shirt('red','M','long sleeved',45)
shirt_two  = Shirt('orange','S','short sleeved',30)
print(new_shirt.price)
print(new_shirt.color)
shirt_two.change_price(45)
print(shirt_two.price)
new_shirt.color = 'yellow'
new_shirt.sze = 'L'
new_shirt.price = 38