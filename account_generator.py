import random
import string
from typing import List
from logging_info import LoggingInfo
from user import User, EmailValidator


class AccountGenerator:
    def __init__(self):
        self.all_accounts: List[User] = []
              
    def create_account(self) -> bool:
        email = EmailValidator.ev_user_input()
        if EmailValidator.email_validation(email):
            LoggingInfo.log_info("User Entered a Valid Email Address.")
            id_number = self.generate_id()
            password = self.generate_password()
            
            new_user = User(email, id_number, password)
            self.all_accounts.append(new_user)
            self.all_accounts.sort(key=lambda x: x.id_number)
            LoggingInfo.log_info(f"Account Created: {new_user}")
            print(f"Account created: {new_user}\n")
            return True
        else:
            print("Invalid entry!\n")
            LoggingInfo.log_warning("User Entered an Invalid Email Address.")
            return False
    
    
    def list_all_accounts(self) -> None:
        for index, user in enumerate(self.all_accounts, start=1):
            print(f"{index}. {user}")

            
    def login(self) -> bool:
        email = input("Enter your email: ").lower()
        password = input("Enter your password: ")
        
        for user in self.all_accounts:
            if user.email == email and user.password == password:
                LoggingInfo.log_info("LOGIN Successful.")
                return True
        
        LoggingInfo.log_warning("LOGIN Unsuccessful. Invalid email or password.")
        return False
    
    

    def generate_id(self) -> str:
        digits = random.choices(string.digits, k=4)
        ascii_letters = random.choices(string.ascii_uppercase, k=6)
        combined = digits + ascii_letters
        random.shuffle(combined)
        id_number = "".join(combined)
        return id_number
    
    
    def generate_password(self) -> str:
        digits = random.choices(string.digits, k=4)
        ascii_upper = random.choices(string.ascii_uppercase, k=4)
        ascii_lower = random.choices(string.ascii_lowercase, k=6)
        symbols = random.choices(string.punctuation, k=2)
        combined = digits + ascii_upper + ascii_lower + symbols
        random.shuffle(combined)
        password = "".join(combined)
        return password

