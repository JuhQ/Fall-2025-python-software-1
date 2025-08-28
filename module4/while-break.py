command = input("Give command (\"stop\" stops): ")

while command != "stop":
    print("running while")

    if command == "MAYDAY":
        break

    print("Yay")
    command = input("Give command: ")

print("Out of the loop")