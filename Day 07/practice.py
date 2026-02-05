#print list in one line...

heros = ["captain america", "iron man", "thor", "hulk"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heros)