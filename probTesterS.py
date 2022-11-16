import random
import time
import threading
import matplotlib.pyplot as plt


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
	reslup=[]
	resldwn=[]
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
				#resldwn.append(r[1])
				#reslup.append(r[2])
				resldwn+=r[1]
				res+=r[0]
				computers.remove(el)
	num=[x for x in range(len(resldwn))]
				
	avg=res/val
	plot(resldwn,reslup,num)
	print(num)
	l=sorted(resldwn)
	return avg,l[0],l[-1]

def plot(list1,list2, list3):
	y1 =list1
	x1=list3
	plt.bar(x1,y1)
	
#	y2=list2
#	x2=list3
#	plt.plot(x2,y2,label="worst cases",marker='o', markerfacecolor='blue', markersize=12)
	#plt.legend()
	plt.show()

	
	
class Computer(threading.Thread):
	
	
	def __init__(self,st,val):
		threading.Thread.__init__(self)
		self.val=val
		self.st=st	
		self.id=random.randint(0,9)
		self.res=0
		self.reslp=[]
		self.running=True
	def run(self):
			self.running=True
			for n in range(self.val):
				#print(1+self.id,end='')
				f=mgen(self.st)
				self.reslp.append(f)
				self.res+=f
				
			self.running=False
	def ret(self):
			#l=sorted(self.reslp)
			return self.res, self.reslp
			
			
print(compute("all work and no play make jack a dull boy", 10000,10))
		
			
		
	
	