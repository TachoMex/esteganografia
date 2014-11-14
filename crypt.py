import encription
import sys
rsa=encription.RSA()
key=sys.argv[1]
try:
	file=open(key, "r")
	rsa.n=long(file.readline())
	rsa.e=long(file.readline())
except:
	print "Couldn't open "+key
	exit()
	
mensaje=sys.argv[2]
fout=sys.argv[3]
rsa.cryptFile(mensaje,fout)
