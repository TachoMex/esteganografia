import math
import random
import os		
	
def GCD(a, b):
	while b:
		a,b=b, a%b
	return a
	
def probablyPrime(n):
	return pow(2,n-1,n)==1



def nextProbablyPrime(n):
	while not probablyPrime(n):
		n+=1
		#print "trying:",n
	return n;

def lookForProbablyPrime(digits):
	num="";
	for i in range(digits):
		num+=str(random.randint(0,10))
	num=nextProbablyPrime(int(num))
	return num

def extendedEuclidean(a,b):
	stack=[]
	while b!=0:
		stack.append(a)
		stack.append(b)
		a,b=b,a%b
	d,x,y=a,1,0	
	while len(stack)!=0:
		b=stack.pop()
		a=stack.pop()
		d,x,y=d,y,x-(a/b)*y
	return d,x,y
	
	

def inverse(a,p):
	d,x,y=extendedEuclidean(a,p)
	return (x+p)%p
	
class RSA:
	def __init__ (self, a=0 , b=0 ):
		if a!=0 and b!=0:
			self.p=a
			self.q=b
			self.n=self.p*self.q
			self.phi_n=(self.p-1)*(self.q-1)
			self.e=random.randint(1,self.phi_n)
			while GCD(self.e,self.phi_n) != 1:
				self.e=random.randint(1,self.phi_n)	
			self.d=inverse(self.e,self.phi_n)
		else:
			self.p=0
			self.q=0
			self.n=0
			self.phi_n=0
			self.e=0
			self.d=0
	
	def setPublicKey (self, a):
		self.e=a
	
	def getPrivateKey(self):
		return self.d 
	
	def setPrivateKey(self,a):
		self.d=a
	
	def encrypt(self,m):
		return pow(m,self.e,self.n)
		
	def decrypt(self,c):
		return pow(c,self.d,self.n)
	
	def cryptFile(self,finput,foutput):
		f=open(finput,'rb')
		cifrado=open(foutput,'wb')
		f.seek(0, os.SEEK_END)
		size=f.tell()
		f.seek(0, 0)
		i=0
		k=0
		while i<size:
			tamPorsion=random.randint(1, 70)+100
			if i+tamPorsion > size:
				tamPorsion = size - i
			cad=f.read(tamPorsion)
			m=0
			for j in range(tamPorsion):
				m+=(256**j)*ord(cad[j])
			
			c=self.encrypt(m)	
			cad=""
			while c :
				cad+=chr(c%256)
				c/=256
			
			cifrado.write(chr(tamPorsion))
			cifrado.write(chr(len(cad)))
			cifrado.write(cad)
			i+=tamPorsion
		
	def decryptFile(self,finput,foutput):
		f=open(finput,'rb')
		salida=open(foutput,'wb')
		while True:
			try:
				u=f.read(1)
				if len(u)==0:
					break;
				tamPorsion=ord(u)
				size=ord(f.read(1))
				cad=f.read(size)
				num=0
				for i in range(size):
					num+=(256**i)*ord(cad[i])
				num=self.decrypt(num)
				for i in range(tamPorsion):
					salida.write(chr(num%256))
					num/=256	
			except ValueError:
				f.close()
				salida.close()
				return 