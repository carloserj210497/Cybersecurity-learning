
while True:
    password = input ("Please introduce your password, it must have at least 8 characters, one number and one uppercase letter: ")

    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)

    if len(password) < 8 :
        print("Weak password is short")
    elif not has_number:
        print("weak password, it must have at least one number")
    elif not has_uppercase:
        print("weak password, it must have at least one uppercase letter")
    else:
        print("Your password is good")
        break

