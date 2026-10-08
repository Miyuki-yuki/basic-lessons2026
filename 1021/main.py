# Review
# terminal commands

# github

# array

# input

# while loop


#review
date = "2026/10/21"
weather = "sunny"

colors = ["yellow","pink","orange"]
colors.append("green")
print(colors)

for i in range(1,101):
  if i % 3 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
  	print(i)

# --- Task 1 ---
# make an array -> add items from user input to array

# my_array = []
# array_items = input("What animal do you like?")
# my_array.append(array_items)
# print(my_array)


# --- Task 2-----
# array should store the items one by one
# fav_animals = input("What animal do you like?")
#.split
# print(fav_animals)
# print(len(fav_animals))

# fav_animals = fav_animals.split()
# print(len(fav_animals))

# print("you like..")
# for i in fav_animals:
#   print(i)

# --- Task 1-3 ---
# fav_animals = input("What animal do you like?").split()
# animals = ",".join(fav_animals)
# print(f"you like..{animals}")

# # --- Task 1-4 ---
# fav_animals = input("What animal do you like?")
# fav_animals = fav_animals.lower()
# fav_animals = fav_animals.replace(",", " ")
# fav_animals = fav_animals.replace("and", " ")

# fav_animals = fav_animals.split()
# animals = ",".join(fav_animals)

# print(f"you like..{animals}")


# --- Task 3 ---

# password = input("Enter your password here: ")
# password_length = int(len(password))
# password = '*' * password_length

# if password_length <= 5:
#   print("Too short. Enter something different")
  
# elif password_length >= 12:
#   print("Too long. Enter something different")
# else:
#   print(f"Your password is {password} and the length is {password_length}")
  

# ---- Task 3 ----
