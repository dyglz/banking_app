
from typing import Optional


class User:
    def __init__(self, email: str, id_number: str, password: str):
        self.email = email
        self.id_number = id_number
        self.password = password
        
    def __str__(self):
        return f"ID Number: {self.id_number}, Email: {self.email}, Password: {self.password}"



class EmailValidator:
    
    @staticmethod
    def ev_user_input() -> Optional[str]:
        user_input = input("Enter your email address: ").lower()
        email = user_input.replace(" ", "")
        if email == "":
            return None
        return email
        
    @staticmethod 
    def email_validation(email: str) -> bool:
        if not email:
            return False
        if not EmailValidator.ev_at_sign_count(email):
            return False
        if not EmailValidator.ev_email_parts(email):
            return False     
        return True        

    @staticmethod
    def ev_at_sign_count(email: str) -> bool:
        at_sign_count = email.count("@")
        if at_sign_count != 1:
            return False
        else:
            return True   
        
    @staticmethod
    def ev_email_parts(email: str) -> bool:
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