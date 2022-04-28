# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_1= name1.lower()
lower_2= name2.lower()

combine = lower_1+ lower_2
t= rep = combine.count("t")
r= rep = combine.count("r")
u= rep = combine.count("u")
e= rep = combine.count("e")
# print(f"T occurs {t} times")
# print(f"R occurs {r} times")
# print(f"U occurs {u} times")
# print(f"E occurs {e} times")
true_sum = t+r+u+e
# print("Total = ", true_sum)

l= rep = combine.count("l")
o= rep = combine.count("o")
v= rep = combine.count("v")
e= rep = combine.count("e")

# print(f"L occurs {l} times")
# print(f"O occurs {o} times")
# print(f"V occurs {v} times")
# print(f"E occurs {e} times")
sum_love = l+o+v+e
# print("Total = ", sum_love )

love_score = int(str(true_sum) + str(sum_love))
# print(f"love score = {love_score}")

if love_score <10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
