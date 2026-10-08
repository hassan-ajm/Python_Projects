import random
target = random.randint(1 , 100)
tries=0
while True:
  try:
    guess=int(input("Enter The Value:"))
    tries +=1
    if guess > target:
      print("Value Too High")
    elif guess < target:
      print("Value Too Small")
    else:
      print(f"Congrats You guessed it right the Number was {target} and you took {tries} to find the correct number")
      break

  except ValueError:
    print("You Entered incorrect Value Please Try Again")