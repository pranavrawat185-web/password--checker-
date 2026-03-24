def check_password():
    while True:
        password = input("Enter your password = ")
        if len(password) >= 8:
            return password
        else:
         print("PASSWORD IS TOO SHORT")
        
pwd= check_password()
print("PASSWORD ACCEPTED!!")
