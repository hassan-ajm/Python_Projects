print("--------------------------------------")
print("Welcome to temperature unit converter!")
print("--------------------------------------")
choice = input ("Enter (1) for C to F or Enter (2) for F to C : ")
value=float(input("Enter The Temprature Value : "))
if choice == "1":
  result = (value * 9/5) + 32
  print(f"{value}C is equalt to {result:.2f}F")
elif choice == "2":
  result = (value - 32) * 5/9
  print(f"{value}F is equalt to {result:.2f}C")
else:
  print("Invalid choice. Please enter 1 or 2.")
