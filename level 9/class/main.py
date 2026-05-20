numbers = [12, -5, 97, 34, -194, 7, 20, -11, 45, 291, 8, -97, 50, 13, 100]


print("ლუწი რიცხვები")

for num in numbers:
   if num % 2 == 0:
      print(num)
    
print("კენტი რიცხვები")
for num in numbers:
   if num % 2 != 0:
      print(num)


print('დადებითი რიცხვები')
for num in numbers:
   if num > 0:
      print(num)


print('უარყოფითი რიცხვები')
for num in numbers:
   if num < 0:
      print(num)

print('გათმაგებული რიცხვები')
for num in numbers:
   print(num * 10)

sum_numbers = 0
for num in numbers:
    sum_numbers += num

print("რიცხვების ჯამი:", sum_numbers)

print("97ზე გამყოფი რიცხვები:")
for num in numbers:
    if num % 97 == 0:
        print(num)



