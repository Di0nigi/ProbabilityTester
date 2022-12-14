import random
import time
import threading
import matplotlib.pyplot as plt


def main():
    string="all work and no play make jack a dull boy"
    Number_of_times=100000000
    mode="everything"
    threads_n=1
    Continue_m=None
    wanted_n=None
    bigger_m=None
    tup=simulate(string,Number_of_times,mode,threads=threads_n,Continue=Continue_m,wanted=wanted_n,bigger=bigger_m)
    tim=[]
    tim2=[]
    #print(tup[3])
    for x in tup[3]:
        if x not in tim2:
            tim.append(tup[3].count(x))
            tim2.append(x)
    s= f"{tup[0]}, {tup[1]}, {tup[2]}"
    print(s)
    plot((tim2,tim))


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
    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'",',','.']
    stlist=list(st)
    counter=0
    counter_1=0
    s=''
    singletry=0
    singletry_list=[]
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
            singletry+=1
            #print(s+alph[i])
        tries+=1
        #time.sleep(0.03)
    return tries
def plot(datas):
    xAxis=sorted(datas[0])
    Yaxis=datas[1]
    #get datas
    #if mode=="everything":
     #   pass
    #elif mode
    plt.bar(xAxis,Yaxis)
    plt.show()


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