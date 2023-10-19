file= open("my_file.txt")
content =file.read()
print(content)
file.close()

#using with Keyword
with open("my_file.txt") as file:
    contents =file.read()
    print(contents)
#using with keyword with mode write (w)
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")
#using a or PPEND IN EXISTING FILE
with open("my_file.txt",mode="a") as file:
    file.write("\nHelloWorld")

