import random
import time
import threading
import matplotlib.pyplot as plt


def main():
    print(simulate("all work and no paly make jack a dull boy",10000,"avg",10))


class Computer(threading.Thread):

	def __init__(self,st,val):
		threading.Thread.__init__(self)
		self.val=val
		self.st=st	
		#self.id=random.randint(0,9)
		self.result=0
		self.results_list=[]
		self.running=True
	def run(self):
			self.running=True
			for n in range(self.val):
				#print(1+self.id,end='')
				singleTry=guesser(self.st)
				self.results_list.append(singleTry)
				self.result+=singleTry	
			self.running=False
	def ret(self):
			#l=sorted(self.results_list)
			return self.results_list

def guesser(st):
    tries=0
    alph=['a', 'b', 'c', 'd', 'e', 'singleTry', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'",',','.']
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
            #print(s+alph[i])
        tries+=1
        #time.sleep(0.03)
    return tries
def plot():
    return
def display():
    return

def simulate(st,times,Output,threads=None,Continue=None,wanted=None,bigger=None):
    #Variables
    trials_sum=0
    trials_results=[]
    computers_list=[]
    Continue_list=[]
    Continue_avg=[]
    currentVal=0
    Min_Val=0
    Max_Val=0
    t=0

    if Continue:
        while(True):
            t+=1
            currentVal=simulate(st,times,"avg",threads)
            Continue_list.append(currentVal)
            if bigger and currentVal>=wanted:
                break
            elif bigger==False and currentVal<=wanted:
                break
            else:
                pass
            
    else:
        #Computers initializer
        if threads!=None:
            for x in range(threads):
                c=Computer(st,times//threads)
                c.run()
                computers_list.append(c)
        else:
            c=Computer(st,times)
            c.run()
            computers_list.append(c)


        #Getting the datas
        while True:
            if len(computers_list)==0:
                break
            for c in computers_list:
                if c.running:
                    pass
                else:
                    SingleData=c.ret()
                    trials_results+=SingleData
                    computers_list.remove(c)
    
    #Outputs
    Min_Val=min(trials_results)
    Max_Val=max(trials_results)

    if Output=="avg":
        trials_sum=sum(trials_results)/len(trials_results)
        return trials_sum
    elif Output=="B-W":
        return Min_Val,Max_Val
    elif Output=="all":
        return trials_results
    elif Continue:
        Min_Val=min(Continue_avg)
        Max_Val=max(Continue_avg)
        Continue_avg= sum(Continue_list)/len(Continue_list)
        return currentVal, t
    elif Output== "everything":
        trials_sum=sum(trials_results)/len(trials_results)
        return trials_sum,Min_Val,Max_Val



main()