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
    

f=guesser("All work aNd no play make jack a dull boy")
print(f)