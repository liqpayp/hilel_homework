username_nick = input("Please input your nickname ")
username_age = int(input("Please input your age "))
username_sex = input("Please input your sex ")

# Пол обознаается буквами F-female  M-male

if username_nick == "admin":
    print("Привет повелитель")
elif username_nick == "Женя":
    print("Советую Вам посмотреть ")
elif username_nick == "Guido":
    print("Огромное спасибо!")
elif username_age < 11 and username_sex == "M":
    print('Советую Вам посмотреть "TMNT"')
elif (username_age > 10 and username_age < 14 and username_sex == "M") or (username_age > 30 and username_sex == "M"):
    print('"Советую Вам посмотреть "StarWars" или "Мандалорец"')
elif username_age > 22 and username_age < 32 and username_sex == "F":
    print('Советую Вам посмотреть "Трансформеры"')
elif username_age > 16 and username_sex == "F":
    print('Советую Вам посмотреть "Инсургент"')
else:
    print("No one")
