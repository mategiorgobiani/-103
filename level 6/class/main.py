#for ციკლს ვიყენებთ მაშინ როდესაც ვიცით იტერაციის რაოდენობა 
#ხოლო while ციკლს ვიყენებთ ,როდესაც არ ვიცით იტერაციის რაოდენობა.
#while ციკლი მუშაობს იქამდე სანამ პირობა არის ჟეშმარიტი

#seats = 5
#while seats > 0: 
#    print('Sell ticket')
#    seats = seats - 1


seats = 5

#while seats > 0:
#    print("Sell ticket")
#    seats -= 1



name = input("სახელი: ")
password = input("პაროლი: ")


a = input("შეიყვანე სახელი: ")
b = input("შეიყვანე პაროლი: ")

while a != name or b != password:

    a = input("შეიყვანე სახელი: ")
    b = input("შეიყვანე პაროლი: ")

print("access granted")

