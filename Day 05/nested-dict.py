dict = {
    "name" : "durjoy",
    "subjects" : {
        "bangla": 98,
        "english": 99,
    }
}

print(dict["name"])    
print(dict.get("name"))

#print(dict["name1"])               #error..
print(dict.get("name1"))           #None