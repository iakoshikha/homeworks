userage = int(input("enter your dad's age: "))

userdadage= int(input("enter your age: "))


print(userage, userdadage)

for years in range(1, 21):
    userage =+ 1
    userdadage += 1

    differenceAge = userdadage // userage

    # // -/ მთელებს აჭრის და ზუსტი გამოაქვს
#  რამდენი იტერაცია  გვინდა რომ მოხდეს



    print("in" , years, "your father will be", differenceAge, "years older than you")



# target_year = 2030

# for year in range(2023, target_year + 1) :
#     age_in_that_year = year - 1973 + age
#     my_age_in_that_year = year - 2003 + my_age
#     print("in", year "you will be", my_age_in_that_year ")
   