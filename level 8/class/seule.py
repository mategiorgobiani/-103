
# password = "1234"
# balance = 100

# attempts = 3

# while attempts > 0:
#     user = input("შეიყვანე პაროლი: ")

#     if user == password:
#         print("სწორია!")

#         amount = int(input("რამდენი ლარის გამოტანა გინდა?: "))

#         if amount <= balance:
#             balance -= amount
#             print("გატანილია:", amount, "ლარი")
#             print("დარჩენილი ბალანსი:", balance, "ლარი")
#         else:
#             print("არასაკმარისი ბალანსი!")

#         break
#     else:
#         attempts -= 1
#         print("არასწორია!")
#         print("დარჩენილი მცდელობები:", attempts)

# if attempts == 0:
#     print("ბარათი დაიბლოკა!")

password = "1234"
balance = 100
attempts = 3

while attempts > 0:
    user_input = input("შეიყვანე პაროლი: ")

    if user_input == password:
        print("პაროლი სწორია!")

        print("1 - ბალანსის ნახვა")
        print("2 - თანხის გამოტანა")
        print("3 - თანხის შეტანა")

        choice = input("აირჩიე: ")

        if choice == "1":
            print("შენი ბალანსია:", balance, "ლარი")

        elif choice == "2":
            amount = float(input("რამდენი ლარის გამოტანა გინდა?: "))

            if amount <= balance:
                balance -= amount
                print("გატანილია:", amount, "ლარი")
                print("დარჩენილი ბალანსი:", balance, "ლარი")
            else:
                print("არასაკმარისი ბალანსი!")

        elif choice == "3":
            amount = float(input("რამდენი ლარის შეტანა გინდა?: "))
            balance += amount
            print("შეტანილია:", amount, "ლარი")
            print("ახალი ბალანსი:", balance, "ლარი")

        else:
            print("არასწორი არჩევანი!")

        break

    else:
        attempts -= 1
        print("არასწორია! დარჩენილი მცდელობები:", attempts)

if attempts == 0:
    print("ბარათი დაიბლოკა!")

    

    