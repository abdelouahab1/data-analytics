favorite_candies = ('Snickers', "M&M’s", 'Skittles')
favorite_flavors = ('Almond', 'Milk Chocolate', 'Tropical')

candy_combinations = set()

candy_combinations.add(favorite_candies[0] + " " + favorite_flavors[0])  
candy_combinations.add(favorite_candies[1] + " " + favorite_flavors[1])  
candy_combinations.add(favorite_candies[2] + " " + favorite_flavors[2])  


print("Today’s candy options include:" , candy_combinations)

# the order of the set keep changing.