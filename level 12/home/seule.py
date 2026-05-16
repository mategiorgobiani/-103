
# #დავალება 1


name = input(str("შეიყვანე სახელი:"))
print(name.capitalize())

# დავალება 2

gmail = input(str("შეიყვანე ემაილია:"))

print(gmail.find(".com"))

#დავალება 3 

password = str(input("შეოიიყვანე პაროლი:"))

print(password.strip())

#დავალება 4

print("მე მიყვარს ჯავასკრიპტი".replace ("ჯავასკრიპტი", "პითონი"))

#დავალება 5

meniu="მარწყვი,ბანანი,ვაშლი,საზამთრო"


print(len(meniu.split(",")))


#დავალება 6

dt = ['2026', '05', '15']

print("/".join(dt))

#დავალება 7

text = "სასწრაფო შეტყობინება: შეცდომა სისტემაში"

print(text.find("შეცდომა"))

#დავალება 8

user_number =  input("შეიყვანე ტელეფონის ნომერი ზედმეტი ნიშნბეის და გამოტოვების გარეშე:")

print(user_number.isdigit())

#დავალება 9

reverse = "აი ია"

print(reverse.count("ა"))

#დავალება 10

a ="https://www.geeksforgeeks.org/python/list-methods-python/"

print(a.startswith("https://"))


