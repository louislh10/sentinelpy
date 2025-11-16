with open("test.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            print(line)
