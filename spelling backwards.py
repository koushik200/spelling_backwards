def spell(txt):
    #your code goes here

    if txt=="":

        return txt
    else:            
     print(txt[len(txt)-1])      
     spell(txt[0:len(txt)-1])  
                       
txt = input()
spell(txt)
