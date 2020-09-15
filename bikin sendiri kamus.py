import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def diction():
    word = input("masukan kata: ")
    
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word not in data:
        print("apakah maksud anda %s ?" %get_close_matches(word,data.keys())[0])
        keputusan = input("iya atau ngga?")
        if keputusan == "iya":
            return data[get_close_matches(word,data.keys())[0]]
        elif keputusan == "ngga":
            return("salah spelling")
        else:
            return("ketik iya atau ngga")        
    
print(diction())
