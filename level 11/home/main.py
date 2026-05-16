
numbers = [12, 7, 19, 24, 33, 40, 55]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)





brands = ["adidas", "puma", "reebok", "nike"]

if "nike" in brands:
    index = brands.index("nike")
    print(f"nike ნაპოვნია ინდექსზე: {index}")
else:
    brands.append("nike")

print(brands)


names = ["Anano", "Nika", "Anano", "Luka", "Anano"]

while names.count("Anano") > 1:
    names.remove("Anano")

print(names)





numbers = [10, 20, 30, 40, 50]

total_sum = 0

while len(numbers) > 2:
    removed = numbers.pop()
    total_sum += removed

print("დარჩენილი სია:", numbers)
print("ჯამი:", total_sum)




class1_grades = [78, 90, 85]
class2_grades = [88, 92, 70]

class1_grades.extend(class2_grades)

class1_grades.sort(reverse=True)

print(class1_grades)


orders = [101, 102, 103]

archive_orders = orders.copy()

if archive_orders:
    orders.clear()

print("არქივი:", archive_orders)
print("ორიგინალი სია:", orders)





letters = ['r', 'a', 'd', 'a', 'r']

reversed_letters = letters.copy()
reversed_letters.reverse()

if letters == reversed_letters:
    print("სიტყვა პალინდრომია")



numbers = [5, 15, 25]

while len(numbers) < 7:
    next_number = numbers[-1] + 10
    numbers.append(next_number)

print(numbers)


fruits = ["apple", "banana", "kiwi", "mango", "pear"]

for fruit in fruits.copy():
    if 'a' in fruit:
        fruits.remove(fruit)

print(fruits)



letters = ['A', 'B', 'C', 'D']

new_list = []

for letter in letters:
    new_list.append(letter)
    new_list.append('-')

print(new_list)





fruits = ["apple", "banana", "kiwi", "mango", "pear"]

for fruit in fruits.copy():
    if 'a' in fruit:
        fruits.remove(fruit)

print(fruits)


name = "Gio"
age = 20

print("My name is (name) and I am (age) years old")
