from User import User
from Password import Password
import hashlib
import os
import bcrypt


hash_object = bcrypt.hashpw((b'123_x32&'), bcrypt.gensalt())

password = os.environ.get(b"bobo")

user1 = User()
user1.set_name("Bert")

p = Password()

hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

p.hash_check(password, hashed_password)
