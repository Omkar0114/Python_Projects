import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            #Easy level password generator:
print(" * * * Welcome to Password Generator * * * ")
letters_l = int(input("how many letters you want ?\n"))
numbers_n = int(input("How many numbers you want ?\n"))
symbols_s = int(input("How many symbols you want ?\n"))

# password = ""
# for char in range(1,letters_l+1):
#     password += random.choice(letters)
#
# for char in range(1 , numbers_n+1):
#     password += random.choice(numbers)
#
# for char in range(1,symbols_s+1):
#     password += random.choice(symbols)
#
# print(password)

                        #Hard Level password Generator:

password_list = []

for char in range (1,letters_l+1):
    password_list.append(random.choice(letters))

for char in range (1,numbers_n+1):
    password_list += random.choice(numbers)

for char in range (1,symbols_s):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")



