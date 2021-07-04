import hashlib
x=input("enter your name:")
a=hashlib.md5(x.encode('utf-8')).hexdigest()
print("hash in MD5 :"+a)