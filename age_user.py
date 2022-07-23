user_year = input("Enter your year of birth: ")

if user_year.isalpha():
        print("Вы ввели текст")
elif int(user_year) == 21:
        print("You should visit Holland.")
elif int(user_year) > 21:
        print("You should visit Vietnam.")
else:
        print("Travell everywhere")





