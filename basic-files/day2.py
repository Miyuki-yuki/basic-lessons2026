# review
# +-*/ % 
# for loop & if condition
# and / or

# temp = int(input("What's the temperature?"))

# if temp < 0:
#   print("too cold")
# elif 0 < temp <= 10:
#   print("A bit cold")
# elif 11 <= temp <= 20:
#   print("Nice weather")

for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)
 
