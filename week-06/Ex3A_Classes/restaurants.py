class Restaurant():
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serveses {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

Subway = Restaurant('Subway', 'Fast food')
IN_N_OUT = Restaurant('IN_N_OUT', 'Fast food')
Chipotle = Restaurant('Chipotle', 'Fast food')

Subway.describe_rest()
IN_N_OUT.describe_rest()
Chipotle.describe_rest()

Subway.rest_open()
IN_N_OUT.rest_open()
Chipotle.rest_open()