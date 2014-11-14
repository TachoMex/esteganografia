import encription
import sys
rsa=encription.RSA()
msg=sys.argv[2]
key=sys.argv[1]
fout=sys.argv[3]
try:
	f=open(key,"r")
except:
	print "Couldn't open"+argv[1]
	exit()
rsa.n=long(f.readline())
rsa.d=long(f.readline())
f.close()
rsa.decryptFile(msg,fout)
