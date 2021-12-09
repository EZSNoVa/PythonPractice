import re, json,random

def isValidEmail(email=None):
    if email == None:
        return False
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if email_regex.match(email):
        return True, email
    else:
        return False, email

def isValidID(userID):
    with open("accounts.json", "r") as f:
        data = json.load(f)
    if userID in data:
        return False
    else:
        return True

def GenerateID():
    # id should be a unique number of 20 digits
    userID = [random.randint(0,9) for i in range(20)]
    userID = "".join(str(i) for i in userID)

    while isValidID(userID) == False:
        GenerateID()
    return userID

# create account
def CreateAccount(name=None, email=None, password=None) -> str:
    userID = GenerateID()
    # write data in json
    with open("accounts.json", "r") as f:
        data = json.load(f)
    
    data[userID] = {
        "name": name,
        "email": email,
        "password": password
    }
    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

    return userID

# Get user info
def GetAccount(userID) -> dict:
    with open("accounts.json", "r") as f:
        data = json.load(f)
    if userID in data:
        return data[userID]
    else:
        return None
    
# update user info
def UpdateAccount(userID, **kwargs) -> bool:
    with open("accounts.json", "r") as f:
        data = json.load(f)
    
    if userID in data:
        for key, value in kwargs.items():
            data[userID][key] = value
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
# delete account
def DeleteAccount(userID) -> bool:
    with open("accounts.json", "r") as f:
        data = json.load(f)
    if userID in data:
        del data[userID]
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
