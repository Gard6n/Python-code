import string
import random


def password_generator():
    set1=string.ascii_lowercase
    set2=string.ascii_uppercase
    set3=string.digits

    combined="".join(set1+set2+set3)
    password="".join(random.choices(combined,k=10))
    return password

while True:
    print(password_generator())