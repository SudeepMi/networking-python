# Create a Python script that securely hashes user passwords using SHA-256. Implement a function for user registration and another for password verification.

import hashlib

db = {}

def hash_password(password):
   salt = "somesalt"  # Generate a random salt for each user
   hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
   return hashed_password

# Save username and hashed_password to the database
def register_user(username, password):
   hashed_password = hash_password(password)
   print("Hash => "+hashed_password)
   db[username] = hashed_password
  
# Retrieve hashed_password from the database based on the username
def verify_password(username, entered_password):
   saved_hashed_password = db[username]
   entered_password_hashed = hash_password(entered_password)
   return entered_password_hashed == saved_hashed_password

if __name__=='__main__':
   for i in range(1):
       username = input('Enter username: ')
       password = input('Enter password: ')
       register_user(username=username,password=password)
   print('For authentication: ')
   username = input('Enter username: ')
   password = input('Enter password: ')
   if(verify_password(username=username,entered_password=password)):
       print('congratulations!! you are valid user')
   else:
       print('Please Try Again')