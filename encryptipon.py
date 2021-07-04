import hashlib
x=input("enter your name:")
a=hashlib.md5(x.encode('utf-8')).hexdigest()
b=hashlib.sha256(x.encode('utf-8')).hexdigest()
c=hashlib.sha512(x.encode('utf-8')).hexdigest()
print("Hash in SHA 256 :"+b)
print("hash in MD5 :"+a)
print("hash in SHA 512 :"+c)
