# Validate user input exercise
# 1) Username is not more than 12 character
# 2) Username must not contain any spaces
# 3) Username must not contain any digits

print("*** Rules for entering username ***")
print("#1) Username is not more than 12 character")
print("#2) Username must not contain any spaces")
print("#3) Username must not contain any digits")

username = input("Enter your username: ")


if len(username) > 12:
    print(f"'{username}' can't be more than 12 characters!")
elif not username.find(" ") == -1:
    print(f"'{username}' can't contain any spaces!")
elif not username.isalpha():
    print(f"'{username}' can't contain any digits!")
else:
    print(f"Welcome {username}")
