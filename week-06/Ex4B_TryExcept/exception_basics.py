# ValueError
try:
    age = int("hello")
except ValueError:
    print("ValueError: You entered an invalid value.")
else:
    print(age)
finally:
    print("Let's try another one...")

# NameError
try:
    print(hello())
except NameError:
    print("NameError: You tried to call an undefined function.")
else:
    print("Function executed successfully.")
finally:
    print("Let's try another one...")


# TypeError
try:
    result = 10 + "5"
except TypeError:
    print("TypeError: You cannot add an integer and a string.")
else:
    print(result)
finally:
    print("Let's try another one...")


# SyntaxError
try:
    compile("if True print('Hello')", "<string>", "exec")
except SyntaxError:
    print("SyntaxError: You forgot the colon after the if statement.")
else:
    print("The code has correct syntax.")
finally:
    print("Let's try another one...")