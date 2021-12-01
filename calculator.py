"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
# Replace this with your code

input_string = input("> ")
tokens = input_string.split(' ')
print(f'{tokens}')

if tokens[0] == "q":
    print("Thanks, see ya later!")
    quit
else:
    if tokens[0] == "+":
        answer = add(int(tokens[1]), int(tokens[2]))
        print(answer)
