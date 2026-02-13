class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database..")

s1 = student("arjun")
print(s1.name)