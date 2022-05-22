import hashlib

my_string = ''
file = open('csvFIle.csv', 'r')
my_lines = file.readlines()

index = len(my_lines)

for x in range(0, index, 2):
    my_string += my_lines[x].split(",")[2]

hashed_string = hashlib.md5(my_string.encode())

print(hashed_string.hexdigest())
