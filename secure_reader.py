import os 
secret_token = os.getenv("MY_SECRET_TOKEN") 

if secret_token: 
    print("Secret loaded successfully.") 
    print(secret_token)
else: 
    print("Secret not found.")