function guesser(st)
    tries=0
    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'",',','.']
    stlist=split(st,"")
    counter=0
    s=""
    while true
        if counter == length(stlist)
            break
        end

        i=rand(0,lenght(alph)-1)
        
        if islower(alph[i]) == islower(stlist[counter])
            if isupper(stlist[counter])
                s+=uppercase(alph[i])
            else
                s=alph[i]+s
            end
            counter+=1
            println(s)
        else
            println(s+alph[i])
        end
        tries+=1
        sleep(0.03)
    end
    return tries
end
    

guesser("all work and no play make jack a dull boy")

