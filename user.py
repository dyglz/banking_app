
import random
import string
from logging_info import LoggingInfo
from typing import List, Optional

class User:
    def __init__(self, email: str, id_number: str, password: str):
        self.email = email
        self.id_number = id_number
        self.password = password
        
    def __str__(self):
        return f"ID Number: {self.id_number}, Email: {self.email}, Password: {self.password}"
    
    
class AccountGenerator:
    def __init__(self):
        self.all_accounts: List[User] = []
    
            
    def create_account(self) -> bool:
        email = self.ev_user_input()
        if self.email_validation(email):
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
    
    
    
    def ev_user_input(self) -> Optional[str]:
        user_input = input("Enter your email address: ").lower()
        email = user_input.replace(" ", "")
        if email == "":
            return None
        return email
        
        
    def email_validation(self, email: str) -> bool: # nesamone
        if not email:
            return False
        if not self.ev_at_sign_count(email):
            return False
        if not self.ev_email_parts(email):
            return False     
        return True        


    def ev_at_sign_count(self, email: str) -> bool:
        at_sign_count = email.count("@")
        if at_sign_count != 1:
            return False
        else:
            return True   
        
        
    def ev_email_parts(self, email: str) -> bool:
        email_parts = email.split("@")
        domain = email_parts[1]
        dot_sign_count = domain.count(".")
        if dot_sign_count < 1:
            return False
        else:
            last_dot_sign = domain.rfind(".")
            if len(domain) - int(last_dot_sign + 1) >= 2:
                return True
            else:
                return False              
          


    def list_all_accounts(self) -> None:
        for index, user in enumerate(self.all_accounts, start=1):
            print(f"{index}. {user}")

            
    def login(self) -> bool:
        email = input("Enter your email: ").lower()
        password = input("Enter your password: ")
        
        for user in self.all_accounts:
            if user.email == email and user.password == password:
                print("You logged in!\n")
                LoggingInfo.log_info("LOGIN Successful.")
                return True
        
        print("Invalid email or password.\n")
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




    
