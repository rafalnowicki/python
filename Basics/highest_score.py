# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score
print(max_score)
