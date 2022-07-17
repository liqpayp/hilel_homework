user_name = input('Please enter your name ')
user_age = int(input('Please enter your age '))

if user_age > 121:
    print(f"You are not real {user_name}!")
elif 70 <= user_age <= 90:
    print(f"You are lucky {user_name} and welcome!")
elif user_age == 16:
    print(f"Dear {user_name} need to wait one year!")
elif user_age >= 16:
    print(f"Welcome, {user_name} on our website!")
else:
    print(f"No one")

