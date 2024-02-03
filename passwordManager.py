master_pwd =input("What is the master passowrd? ")

def view():
    pass

def add():
    pass

while True:
    mode = input("would you like to add  a new password or view existing ones (views/add)? , press q to quit?").lower();
    if mode == 'q':
        break
    if mode == 'view':
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid code")
        continue