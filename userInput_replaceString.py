name=input("enter your name with 3 character for message:")
while len(name)<3:
    print("Name should have minimum three character")
    name=input("enter your name:")

print(f"Hello {name},how are you?")