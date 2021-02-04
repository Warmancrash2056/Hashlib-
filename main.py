import hashlib  # Hash characters

user_create = input('Enter Characters')
crypto = hashlib.md5()
crypto.update(b'user_create')
crypto.hexdigest()
print(crypto)



