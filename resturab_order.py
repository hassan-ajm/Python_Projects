def restaurant_greet(name):
     print(f"Hello, {name}! Welcome to our Restaurant.\n")
     print("What would you like to order today?\n")
    
     # Starting menu items from index 1 for clean ordering
     menu = ["", "Patty Burger", "Zinger Burger", "Arabian Shawarma", "Spicy Kebab", "Cheese Nachos"]
    
   
     for i, item in enumerate(menu[1:], start=1):# learned why menu [1:] was imp without it would have still shown the empty index 1 string 
         print(f"{i}. {item}")
        
  
     while True:
         try:
             
             order_choice = int(input("\nEnter the menu number you'd like to order: "))
            
        
             if order_choice < 1 or order_choice >= len(menu):
                 print(f"Please enter a number between 1 and {len(menu) - 1}.")
                 continue# learned conitnue ksip rest the code and goes bakc up 
               
            
             print(f"\nGreat choice! You ordered a {menu[order_choice]}.")
             break
         except ValueError:
             
             print("Invalid input! Please enter a valid number (e.g., 1, 2, 3).")
         
         print("Thanks for your Buisness , Please come againn ")
        

restaurant_greet("Hassan")