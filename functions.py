import json

def checkLibrary():
    
    try:
        f = open ("books.json")
        info = json.load (f)
        f.close
        return info
    
    except:
        print("ERROR")