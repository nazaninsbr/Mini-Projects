file_name = "hello23you.jpg"
print(file_name)
result = "".join([i for i in file_name if not i.isdigit()])
print(result)