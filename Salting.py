import hashlib
x=input("enter your name:")
a=hashlib.md5(x.encode('utf-8')).hexdigest()
salt="hello"

for i in range(5):
    a="".join([a,salt])
    a = hashlib.md5(a.encode('utf-8')).hexdigest()


print("hash in MD5 :"+a)