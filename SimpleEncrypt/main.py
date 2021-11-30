import json
from typing import *

def CreateEncryptionSystem(system_name=None, **kwargs) -> dict:
    # system should be saved in a json file (letter -> new letter)
    system_name = "system_1" if system_name is None else system_name    
    with open("EncryptSystems.json", "r") as f:
        systems = json.load(f)
        systems[system_name] = kwargs
        with open("EncryptSystems.json", "w") as f:
            json.dump(systems, f, indent=4)
    return systems[system_name]
    
def UpdateEncryptionSystem(system_name, **kwargs):
    # update the system with new letters
    system = LoadEncryptionSystem(system_name)
    if system is None:
        return
   
    system.update(kwargs)
    with open("EncryptSystems.json", "w") as f:
        json.dump(system, f, indent=4)

def DeleteEncryptionSystem(system_name) -> bool:
    # delete the system
    system = LoadEncryptionSystem(system_name)
    if system is None:
        return False
    
    with open("EncryptSystems.json", "w") as f:
        systems = json.load(f)
        del systems[system_name]
        
    with open("EncryptSystems.json", "w") as f:
        json.dump(systems, f, indent=4)
    return True
      
def LoadEncryptionSystem(system_name=None) -> dict or None:
    if system_name is None:
        return None
    
    with open("EncryptSystems.json", "r") as f:
        systems = json.load(f)
        return systems[system_name]
    
def GenerateEncryptionSystem(shift=1) -> dict:
    # generate a new encryption system
    system = {}
    for letter in "abcdefghijklmnopqrstuvwxyz": 
        system[letter] = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
    return system
    
def Encrypt(message, system_name=None) -> str:
    # encrypt the message using the system
    if system_name is None:
       return message
   
    system = LoadEncryptionSystem(system_name)
    if system is None:
        return message
    message = message.lower()
    return "".join([system[letter] if letter in system else letter for letter in message])

def Decrypt(message, system_name=None) -> str:
    # decrypt the message using the system
    if system_name is None:
        return message
   
    system = LoadEncryptionSystem(system_name)
    system = {v: k for k, v in system.items()}
    if system is None:
        return message
   
    return "".join([system[letter] if letter in system else letter for letter in message])