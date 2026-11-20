class Restaurant():
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f'{self.rest_name} serveses {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

    def add_num_served(self):
        customers = int(input('How many customers served today? '))
        self.number_served += customers

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self):
        while True:
            rating = input(
                  'How would you rate your experience today '
                  'on a scale of 1-5 (5 being excellent)? '
                )

            if rating.isdigit() and 1 <= int(rating) <= 5:
               rating = int(rating)
               break
            else:
               print('Invalid input. Please enter an integer between 1 and 5.')

        self.customer_ratings.append(rating)

        average = sum(self.customer_ratings) / len(self.customer_ratings)

        print(f'Your rating was {rating}. The average rating for this restaurant is {average:.2f}')

Subway = Restaurant('Subway', 'Fast food')
IN_N_OUT = Restaurant('IN_N_OUT', 'Fast food')
Chipotle = Restaurant('Chipotle', 'Fast food')

Subway.describe_rest()
IN_N_OUT.describe_rest()
Chipotle.describe_rest()

Subway.rest_open()
IN_N_OUT.rest_open()
Chipotle.rest_open()

Subway.print_num_served()

Subway.add_num_served()
Subway.add_num_served()

Subway.print_num_served()


IN_N_OUT.print_num_served()

IN_N_OUT.add_num_served()
IN_N_OUT.add_num_served()

IN_N_OUT.print_num_served()


Chipotle.print_num_served()

Chipotle.add_num_served()
Chipotle.add_num_served()

Chipotle.print_num_served()



Subway.customer_rating()
Subway.customer_rating()
Subway.customer_rating()

IN_N_OUT.customer_rating()
IN_N_OUT.customer_rating()
IN_N_OUT.customer_rating()

Chipotle.customer_rating()
Chipotle.customer_rating()
Chipotle.customer_rating()