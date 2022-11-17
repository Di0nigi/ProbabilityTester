import random
import time
import threading
import matplotlib.pyplot as plt


def main():
    string="all work and no paly make jack a dull boy"
    Number_of_times=1000
    mode="everything"
    threads_n=10
    Continue_m=None
    wanted_n=None
    bigger_m=None
    print(simulate(string,Number_of_times,mode,threads=threads_n,Continue=Continue_m,wanted=wanted_n,bigger=bigger_m))


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
    loop=0

    if Continue:
        while(True):
            loop+=1
            print(loop)
            currentVal=simulate(st,times,"everything",threads)
            Continue_list+=(currentVal[3])
            if bigger and currentVal[2]>=wanted:
                break
            elif bigger==False and currentVal[1]<=wanted:
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
    if Continue:
        CMin_Val=min(Continue_list)
        CMax_Val=max(Continue_list)
        if Output=="avg":
            Continue_avg= sum(Continue_list)/len(Continue_list)
            return Continue_avg
        elif Output=="B-W":
            return CMin_Val,CMax_Val
        elif Output=="all":
            return Continue_list
        elif Output== "everything":
            Continue_avg= sum(Continue_list)/len(Continue_list)
            return Continue_avg,CMin_Val,CMax_Val,loop
    else:
        Min_Val=min(trials_results)
        Max_Val=max(trials_results)
        if Output=="avg":
            trials_sum=sum(trials_results)/len(trials_results)
            return trials_sum
        elif Output=="B-W":

            return Min_Val,Max_Val
        elif Output=="all":
            return trials_results
        elif Output== "everything":
            trials_sum=sum(trials_results)/len(trials_results)
            return trials_sum,Min_Val,Max_Val,trials_results



main()