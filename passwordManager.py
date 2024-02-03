master_pwd =input("What is the master passowrd? ")

def view():
    with open('password.tx', 'r') as f:
        for line in f.readline():
            data = line.rstrip()
            user,passw = data.split("|")

def add():
    name = input("Account Name :");
    pwd  =  input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("would you like to add  a new password or view existing ones (views/add)? , press q to quit? ").lower();
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid code")
        continue
 