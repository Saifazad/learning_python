#1. Ek file notes.txt banao aur usme apna naam aur ek sentence likho ("w" mode se).

with open("notes.txt", "w") as f:
    f.write("hello world this is my first time to learn file handling topic");

with open("notes.txt", "a") as f:
    f.write("\nword added");

with open("notes.txt", "r") as f:
    contant = f.read()
    print(contant)


