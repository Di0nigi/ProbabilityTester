import random
import time
import threading


glob=0

def mgen(st):
	c=0
	
	alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'",',','.']

	stlist=list(st)
	counter=0
	s=''
	while True:
		if counter==len(stlist):
			break
		i=random.randint(0,len(alph)-1)
	
		if alph[i].lower()==stlist[counter].lower():
			if stlist[counter].isupper():
				s+=alph[i].upper()
			else:
				s=alph[i]+s
			
			counter+=1
			#print(s)
		else:
			pass
			#print(alph[i]+s)
		c+=1
	return c
		

def compute(st, val,div):
	res=0
	resl=[]
	computers=[]
	
	for x in range(div):
		c=Computer(st,val//div)
		c.run()
		computers.append(c)
	while True:
		if len(computers)==0:
			break
		
		for el in computers:
			if el.running:
				pass
			else:
				r=el.ret()
				resl.append(r[1])
				resl.append(r[2])
				res+=r[0]
				computers.remove(el)
				
	avg=res/val
	l=sorted(resl)
	return avg,l[0],l[-1]


	
class Computer(threading.Thread):
	
	res=0
	reslp=[]
	running=True
	def __init__(self,st,val):
		threading.Thread.__init__(self)
		self.val=val
		self.st=st	
		self.id=random.randint(0,9)
	def run(self):
			self.running=True
			for n in range(self.val):
				#print(1+self.id,end='')
				f=mgen(self.st)
				self.reslp.append(f)
				self.res+=f
				
			self.running=False
	def ret(self):
			l=sorted(self.reslp)
			return self.res, l[0],l[-1]
			


def main():
	c=0
	while True:
		c+=1
		eo=compute("all work and no play make jack a dull boy", 100000,100)
		if eo[1]<=500:
			print((eo))
			print(c)
			break
		print(c)

		
main()			
		
	
	