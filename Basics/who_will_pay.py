# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
count_names = (len(names) -1)
print(count_names)
print(f"{names[random.randint(0, count_names)]} is going to buy the meal today!")

person_who_will_pay = random.choice(names)
print(person_who_will_pay)

