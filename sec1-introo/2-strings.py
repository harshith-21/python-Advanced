string1  = "hello there \n"

string2  = 'hello thereeee \n'

string3  = 'hello thereeee "apple" \n'

string4 = "heloo there this machine is harshith's "

print(string1, string2, string3, string4)


# to use same quotes u can use the escape character
string5 = "apple ball \"cat\" dog"


multiline_string = """
hey
this 
is
funny
!!!!
"""
print(multiline_string)




# this is also fine but no one will be able to use it because its not assigned to a variable
"""
this is also
a multiline
string
"""



name = "harsheyy"
gree = "Hello, " + name
print(gree)



age = 21
agestr = str(age)
print("1. age is " + agestr)
print("2. age is", age)

# fstrings
print(f"3. age is {age}")


name = "harshi"
greeting = f"hello {name}"
print(greeting)



# f strings fn's
greet = "hellloooooo, {}"

name1 = "bob"
greet1 = greet.format(name1)
print(greet1)

name2 = "jim"
greet2 = greet.format(name2)
print(greet2)


print()
#### ANOTHER way

name = "apple"
greet = "hello there, {name}" # not a fstring

apple_greet = greet.format(name=name)
print(apple_greet)

# ALSO
greet = "helo {}"
name = "harshi"
print(greet.format(name))