# Ask user to [create account] 
# (In that case you need to provide your email address, 
# and then the app will give you ID and password)


# [Log In] to bank service (you check email and password . 
# Email and ID should be linked) email -> ID -> password.

# separate modules, class structures and [access modifiers] (private and protected)

import logging
from logging_info import LoggingInfo
from user import User, AccountGenerator

LoggingInfo.configure_logging()
LoggingInfo.log_info("BestBank App is Opened.")

account_generator = AccountGenerator()

while True:
    print("===  Welcome to BestBank App!  ===")
    print("1. Create Account\n2. Log In\n3. List All Accounts\n0. Exit App")
    
    try:
        menu_selection = int(input("Enter your selection: "))
        if 0 <= menu_selection <=3:
            if menu_selection == 0:
                print("===    Exiting BestBank App    ===")
                LoggingInfo.log_info("BestBank App is Closed.")
                break
            elif menu_selection == 1:
                print("===     Create an account      ===")
                LoggingInfo.log_info("Trying to create a new account.")
                account_generator.create_account()
            elif menu_selection == 2:
                print("===   Log In to your account   ===")
                LoggingInfo.log_info("Trying to log in.")
                account_generator.login()       
            elif menu_selection == 3:
                print("===   Account List   ===")
                LoggingInfo.log_info("Sensitive: Displaying account list with user ID, email and password.")
                account_generator.list_all_accounts()             
        else:
            print("Invalid selection!")
            LoggingInfo.log_warning("User Entered Non Existing Number in Menu Selection.")
    except ValueError:
        print("Invalid symbol entered!")
        LoggingInfo.log_warning("User Entered Symbol/Character in Menu Selection.")
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        LoggingInfo.log_critical(f"Unexpected Error: {str(e)}.")




