import re # import the regular expression module

# https://regex101.com/


# Create a string to search
my_string = "Hello World"

# regex functions:
# search(pattern, string)
# findall(pattern, string)
# split(pattern, string)
# sub(pattern, repl, string)

# search(pattern, string)
print(re.search("World", my_string))

# findall(pattern, string)
print(re.findall("World", my_string))

# split(pattern, string)
print(re.split(" ", my_string))

# sub(pattern, repl, string)
print(re.sub("World", "John", my_string))

