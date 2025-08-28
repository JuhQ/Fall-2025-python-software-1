stop1 = "stop"
stop2 = "something other"
prompt_message = f'Give command ("{stop1}" and "{stop2}" stops): '

command = input(prompt_message)


if command != stop1 and command != stop2:
    print(f"User gave command: {command}")
    print("Only printed once")

while command != stop1 and command != stop2:
    print(f"User gave command: {command}")
    print("Printed multiple tims")
    command = input(prompt_message)
    #command = input("Give command (\"stop\" stops): ")

print("We have stopped")
