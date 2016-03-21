




def nearest_shoot_point(input1,input2,input3,input4):

    bullet = []
    for x in range(0,len(input4)):   
        temp = input4[x]
        temp = list(temp[:])
        temp = [x for x in temp if x != '#']
        temp = map(int, temp)
        bullet.append(temp)
        
    
    list_of_cells = []    
    N = input1[0] #Size of battlefield
    M = input1[1] 

    P = input3[0] #Target Position
    Q = input3[1]
    
        
    #Loops for all posible positions from where we can hit target
    
    for x in range(Q+1, M):    #East direction    
        cell = [P,x]
        if cell in bullet:
            list_of_cells.append(cell)
            break
        else:
            list_of_cells.append(cell)
        
            
    for x in range(P+1, N):    #North direction    
        cell = [x,Q]
        if cell in bullet:
            
            list_of_cells.append(cell)
            break
        else:
            
            list_of_cells.append(cell)
                 
    

    for x in range(P-1,-1,-1):    #South direction    
        cell = [x,Q]
        if cell in bullet:
            
            list_of_cells.append(cell)
            break
        else:
            
            list_of_cells.append(cell)
                
    


    for x in range(Q-1,-1,-1):    #West direction    
        cell = [P,x]
        if cell in bullet:
            
            list_of_cells.append(cell)
            break
        else:
            
            list_of_cells.append(cell)
                
          


    temp = Q
    for x in range(P+1, N): #North East direction    
        
        temp = temp+1
        cell = [x,temp]
        if temp==M:
            break
        else:
            if cell in bullet:
                
                list_of_cells.append(cell)
                break
            else:
                
                list_of_cells.append(cell)
                   
    

            
    temp = Q
    for x in range(P+1, N): #North West direction    
        
        temp = temp - 1
        
        cell = [x,temp]
        if temp==-1:
            break
        else:
            if cell in bullet:
                
                
                list_of_cells.append(cell)
                break
            else:
                
                list_of_cells.append(cell)
                  
    


    temp = Q
    for x in range(P-1,-1,-1): #South West direction    
        
        temp = temp - 1
        
        cell = [x,temp]
        if temp==-1:
            break
        else:
            if cell in bullet:
                
                
                list_of_cells.append(cell)
                break
            else:
                
                list_of_cells.append(cell)
                  
    


    temp = Q
    for x in range(P-1,-1,-1): #South East direction    
        
        temp = temp + 1
        
        cell = [x,temp]
        if temp==M:
            break
        else:
            if cell in bullet:
                
                
                list_of_cells.append(cell)
                break
            else:
                
                list_of_cells.append(cell)
                  
    

    distance = []
    #Loop fo minimum walking distance
    for x in range(0, len(list_of_cells)):
        d = (abs(list_of_cells[x][0]-input2[0]) +  abs(list_of_cells[x][1]-input2[1])) 
        distance.append(d)
        


    

    indices = [i for i, x in enumerate(distance) if x == min(distance)]
    


    closet_point = []

    for x in range(0,len(indices)):
        closet_point.append(list_of_cells[indices[x]])

    

    closet_point_str = []
    for x in range(0, len(closet_point)):
        string = str(closet_point[x][0]+1)+'#'+str(closet_point[x][1]+1)
        closet_point_str.append(string)
    print closet_point_str
        

        


input1 = [6,6]  #Size of battlefield
input2 = [2,4]  #Starting point of soldier
input3 = [4,3]  #Position of target
input4 = ['1#2','2#3','4#1','4#5']  #Position of bulletproof cells.

nearest_shoot_point(input1,input2,input3,input4)


