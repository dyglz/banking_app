#  - Ask user to create account 
# (In that case you need to provide your email address, 
# and then the app will give you ID and password)

import random
import string

class User:
    def __init__(self, email: str) -> dict[int, str]:
        self.email = email

    def generate_id() -> str:
        characters = string.ascii_uppercase + string.digits
        id_number = ''.join(random.choices(characters, k=10))
        return id_number


test = generate_id()
print(test)


    
