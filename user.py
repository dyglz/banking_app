#  - Ask user to create account 
# (In that case you need to provide your email address, 
# and then the app will give you ID and password)

import random
import string
from typing import Dict, List

class User:
    def __init__(self, email: str, id_number: str, password: str) -> Dict[str]:
        self.email = email
        self.id_number = id_number
        self.password = password
        self.all_users: List[User] = []
        
    def __str__(self):
        return f"Email: {self.email}, ID Number: {self.id_number}, Password: {self.password}"
    
    
    def email_validation(email):
        at_sign_count = email.count("@")
        if at_sign_count != 1:
            return False
        elif at_sign_count == 1:
            email_parts = email.split("@")
            domain = email_parts[1]
            dot_sign_count = domain.count(".")
            if dot_sign_count < 1:
                return False
            elif dot_sign_count >= 1:
                last_dot_sign = domain.rfind(".")
                if len(domain) - int(last_dot_sign + 1) >= 2:
                    return True
                else:
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







user = User("example@test.com")
test = user.generate_id()
test1 = user.generate_password()
print(test)
print(test1)


    
