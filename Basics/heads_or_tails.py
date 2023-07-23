#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
print("Heads or Tails Game. Toss a coin.")
print("Press a key")
input()
result = random.randint(0, 1)
if result == 0:
  print("Tails")
else:
  print("Heads")

