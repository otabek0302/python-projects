# a-z 0-9 . _ % + -
# @
# a-z 0-9 . -

import re
email_condations = "^[a-z]+[\.]?[a-z0-9]+[@][a-z]+[\.][a-z]{2,3}$"

user_email = input("Enter your email: ")

if re.search(email_condations, user_email):
    print("Valid email address")
else:
    print("Invalid email address")