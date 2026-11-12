name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1_lower_case = name_1.lower().title()
name_2_lower_case = name_2.lower().title()
name_3_lower_case = name_3.lower().title()

salary_1_convert = int(salary_1.replace('$', '').replace(',', ''))
salary_2_convert = int(salary_2.replace('$', '').replace(',', ''))

print(salary_1_convert, type(salary_1_convert))