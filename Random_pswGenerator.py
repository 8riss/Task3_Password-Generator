import random

uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letter.lower()
numbers = "0123456789"
symbols = "!^&*-_=+[{]};:<#$%>.?/~\|"

upper, lower, num, sym = True, True, True, True

all = ""


if upper:
    all += uppercase_letter
if lower:
    all += lowercase_letter
if num:
    all += numbers
if sym:
    all += symbols

try:
    x = int(input("Length of Password: "))
    length = x
    amount = 10

    if (x == uppercase_letter or lowercase_letter):

        for c in range(amount):
         password = "".join(random.sample(all, length))

except: print("ERROR!")

print (password)