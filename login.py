username=input("Enter your username: ")
password=input("Enter your password: ")

if username =='aman' and password =='12345':
    print("Login successful!")
elif username !='aman' and password =='12345':
    print("Invalid username. Please try again.")
    input("Enter your username: ")
    if username =='aman':
        print("Login successful!")
    
else:
    print("Invalid username or password. Please try again.")