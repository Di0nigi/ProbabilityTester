using PlotlyJS, CSV, DataFrames

function main()
    string="all work and no play make jack a dull boy"
    Number_of_times=100
    mode="everything"
    Continue_m=false
    wanted_n=0
    bigger_m=false
    tup=simulate(string,Number_of_times,mode,Continue_m,wanted_n,bigger_m)
    tim=[]
    tim2=[]
    #print(tup[3])
    for x in tup[3]
        if !(x in tim2)
            push!(tim,count(i->(i==x),tup[3]))
            push!(tim2,x)
        end
    end
    #s= f"{tup[0]}, {tup[1]}, {tup[2]}"
    #print(s)
    #plot((tim2,tim))
    #print(tup)
end


function plt(list1,list2)
    data_list=[]
    plot(data_list,x=:year, y=:pop, kind="bar")
end

function isupp(s)
    S=only(s)
    if Int(S)<=90 && Int(S)>=65
        ret = true
    else
        ret= false
    end
    return ret
end

function guesser(st)
    tries=0
    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'",',','.']
    l=length(alph)
    #println(alph[6])
    stlist=split(st,"")
    #print(stlist)
    counter=1
    s=""
    while true
        if counter == length(stlist)+1
            break
        end

        i= trunc(Int,rand()*l-1)+1
        char=string(alph[i])
        char2=stlist[counter]
        
        if cmp(lowercase(char),lowercase(char2))== 0
            
            if isupp(char2)
                s= s*uppercase(char)
            else
            s=s*char
            end
            counter+=1
            #println(s)
        else
            #println(s*char)
        end
        tries+=1
        #sleep(0.03)
    end
    return tries
end


function simulate(st,times,Output,Continue,wanted,bigger)
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

    if Continue
        while true
            loop+=1
            #print(loop)
            currentVal=simulate(st,times,"everything",false,0,false)
            Continue_list+=(currentVal[3])
            if bigger && currentVal[2]>=wanted
                break
            elseif bigger==False && currentVal[1]<=wanted
                break
            else
                pass
            end
        end
            
    else
        for n in range(1,0,times)
            singleTry=guesser(st)
			push!(trials_results,singleTry)
			trials_sum+=singleTry	
        end 
    end
    #Outputs
    if Continue
        CMin_Val=min(Continue_list)
        CMax_Val=max(Continue_list)
        if  cmp(Output,"avg")==0
            Continue_avg= sum(Continue_list)/length(Continue_list)
            return Continue_avg
        elseif O cmp(Output,"B-W")==0
            return CMin_Val,CMax_Val
        elseif Output=="all"
            return Continue_list
        elseif cmp(Output, "everything")==0
            Continue_avg= sum(Continue_list)/length(Continue_list)
            return Continue_avg,CMin_Val,CMax_Val,loop
        end
    else
        Min_Val=minimum(trials_results)
        Max_Val=maximum(trials_results)
        if cmp(Output,"avg")==0
            trials_sum=sum(trials_results)/length(trials_results)
            return trials_sum
        elseif   cmp(Output,"B-W")==0

            return Min_Val,Max_Val
        elseif cmp(Output,"all")==0
            return trials_results
        elseif  cmp(Output, "everything")==0
            trials_sum=sum(trials_results)/length(trials_results)
            return trials_sum,Min_Val,Max_Val,trials_results
        end
    end
end
    

#f=simulate("All work aNd no play make jack a dull boy",10000,"avg",false,0,false)
#print(f)
main()