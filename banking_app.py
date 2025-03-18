
from logging_info import LoggingInfo
from account_generator import AccountGenerator
from user import EmailValidator

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
                print("------  Create an account  -------")
                LoggingInfo.log_info("Trying to Create a New Account.")
                if account_generator.create_account():
                    print("Account successfully created!")
                else:
                    print("Account not created.")                
            elif menu_selection == 2:
                print("----  Log In to your account  ----")
                LoggingInfo.log_info("Trying to Log In.")
                if account_generator.login():
                    print("You logged in!\n")
                else:
                    print("Invalid email or password.\n")                           
            elif menu_selection == 3:
                print("---------  Account List  ---------")
                LoggingInfo.log_warning("Sensitive: Displaying Account List with All Users [ID, Email and Password].")
                account_generator.list_all_accounts()             
        else:
            print("Invalid selection!\n")
            LoggingInfo.log_warning("User Entered Non Existing Number in Menu Selection.")
    except ValueError:
        print("Invalid symbol entered!\n")
        LoggingInfo.log_warning("User Entered Symbol/Character in Menu Selection.")
    except Exception as e:
        print(f"Unexpected error occured: {e}\n")
        LoggingInfo.log_critical(f"Unexpected Error: {str(e)}.")




