department_code = int(input('Enter the department code: '))

def check_department_code(department_code):
    match department_code:
        case 1:
            print('Marketing')
        case 5:
            print('Human Resources')
        case 10:
            print('Accounting')
        case 12:
             print('Legal')
        case 18:
            print('IT')
        case 20:
            print('Customer Relations')
        case _:
            print('Enter a valid department code')

check_department_code(department_code)