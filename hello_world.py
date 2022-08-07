def create_file():
    num = input("please Enter number: ")
    f = open(f"{num}.txt", "a")
    f.write(f"{num}")
    f.close()


create_file()