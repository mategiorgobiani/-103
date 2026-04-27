



print(5 > 23 and 10 > 2)

print(5 > 10 or 3 < 8)

print(not(5 > 3))

x = 15
print(x > 5 and x < 20)

x = 3
print(x > 5 or x > 3)

x = 321
print(not(x < 7))

a = 43
b = 9
print(a < b and b > 5)

a = 23
b = 82
print(a > 5 or b > 5)

x = 1513
print(not(x < 10))

age = 1823
print(age > 18 and age < 6023)




print(5 > 3 and 10 > 7)

print(4 < 2 or 8 > 5)

print(not(6 == 6))

x = 10
print(x > 5 and x < 15)

x = 3
print(x == 3 or x > 10)

x = 7
print(not(x < 5))

a = 4
b = 9
print(a < b and b != 10)

x = 15
print(not(x <= 10))

a = 2
b = 8
print(a > 5 or b >= 8)

age = 20
print(age >= 18 and age <= 30)

# input არის ფუნქცია, რომელიც საშუალებას აძლევს მომხმარებელს,
# პროგრამის მუშაობის დროს შეიყვანოს მონაცემი კლავიატურიდან.
# როდესაც ვიყენებთ input()-ს, პროგრამა ჩერდება და ელოდება მომხმარებლის შეყვანას.
# input()-ის შიგნით შეგვიძლია ჩავწეროთ ტექსტი (message),
# რომელიც ეკრანზე გამოჩნდება მომხმარებლისთვის.
name = input("სახელი: ")

# input() ყოველთვის აბრუნებს ტექსტს (string ტიპის მონაცემს),
# თუნდაც მომხმარებელმა რიცხვი შეიყვანოს.
age = input("ასაკი: ")

# თუ გვინდა რიცხვად გამოყენება, უნდა გადავიყვანოთ int()-ით ან float()-ით.
age = int(age)

# შემდეგ შეგვიძლია გამოყენება პროგრამაში
print("გამარჯობა,", name)
print("ასაკია:", age)


