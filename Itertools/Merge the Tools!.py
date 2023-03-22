def merge_the_tools(string, k):

    a = [] 
    for i in range(0,len(string),k):
        a.append(string[i:i+k])
    # print(a)
    for i in a:
        letters = set() 
        temp = ''
        for j in i:
            if not(j in letters):
                letters.add(j)
                temp += j 
        print(temp)
                
        

