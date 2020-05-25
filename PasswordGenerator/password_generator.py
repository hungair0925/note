from random import choices
from string import ascii_letters
from string import digits
from sys import exit

def create_password(pwd_length):
    pwd_resource = ascii_letters + digits
    if pwd_length < 8:
        print("8文字以上入力してださい")
        exit()
    else:
        pwd = "".join(choices(pwd_resource, k=pwd_length))
        return pwd

if __name__ == "__main__":
    while True:
        pwd_length = int(input("何文字のパスワードを作りますか:"))
        print(create_password(pwd_length))
