import hashlib

#hash_s = hashlib.sha3_224(data.encode('utf-8')).hexdigest()

base = {}
def registration():
    print("Login: ")
    login = input()
    password = "password";
    password2 ="password2"
    while password != password2:
        print("Password: ")
        password = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        print("Confirm password: ")
        password2 = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        if password == password2:
            break
        else:
            print ("Error confirm password")
    base.update([(login , password)])
    print("Registration completed successfully!")
    print(base)

def autorisation():
    while True:
        print("Login: ")
        login = input()
        print("Password: ")
        password = hashlib.sha3_224(input().encode('utf-8')).hexdigest()
        if base.get(login) == password:
            print("Autorisation completed successfully!")
            break
        else:
            print ("Error password")
    
registration()
autorisation()
