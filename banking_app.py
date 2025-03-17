# terminal based

# Ask user to create account 
# (In that case you need to provide your email address, 
# and then the app will give you ID and password)


# Log In to bank service (you check email and password . 
# Email and ID should be linked) email -> ID -> password.

# separate modules, class structures and access modifiers (private and protected)

while True:
    print("===  Welcome to BestBank App!  ===")
    print("1. Create Account\n2. Log In\n0. Exit App")
    
    try:
        menu_selection = int(input("Enter your selection: "))
        if 0 <= menu_selection <=2:
            if menu_selection == 0:
                print("===    Exiting BestBank App    ===")
                break
            elif menu_selection == 1:
                pass
            elif menu_selection == 2:
                pass   
        else:
            print("Invalid selection!")
    except ValueError:
        print("Invalid symbol entered!")
    except Exception as e:
        print(f"Unexpected error occured: {e}")







