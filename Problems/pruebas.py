

while True:
    print("Who are you?")
    name = str(input())
    if name != "Alexia":
        continue
    print("Password: ")
    password = str(input())
    if password == "00":
        break
print("Welcome to your computer Alexia")
