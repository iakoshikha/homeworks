import random
my_arr = []
password = ""
chars = list("qazgfnqournzmfkjdfsueguf")
symbols = list("!@#$%^&*()")
numbers = list("123456789")

for i in range(9):
    random_num = random.choice(numbers)
    my_arr.append(random_num)
    numbers.remove(random_num)

for i in range(15):
    random_char = random.choice(chars)
    my_arr.append(random_char)
    chars.remove(random_char)

for i in range(6):
    random_symbol = random.choice(symbols)
    my_arr.append(random_symbol)
    symbols.remove(random_symbol)
     

# for i in range(4):
#     my_arr.append(random.choice(numbers))
# for i in range (2):
#     my_arr.append(random.choice(chars))
#     my_arr.append(random.choice(symbols))


print("the program chose thesecharacters:" , my_arr)
final_password = ""
for i in range(len(my_arr)):
    current_char = random.choice(my_arr) #z
    final_password += current_char  #z
    my_arr.remove(current_char)   #z რათაარ განმეორდეს ერთი და იგივე სიმბოლო პასვორდში

    print(final_password)