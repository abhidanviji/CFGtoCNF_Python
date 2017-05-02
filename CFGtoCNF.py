#CS 635 Programming Project - Abhinaya Dhandapani
#User input of the CFG
str =  input('Enter Rule: ')#A -> aBcdE
#var_list to maintain the RHS and arr_list to record LHS
var_list={}
arr_list={}
count=0
i=0
#Split strings for processing
s = str.split( )
left=s[0]
right=s[2]
first=right[0]
rest=right[1:]
arr_list[count]=left
count=count+1

#Recursive function for CFG to CNF conversion
def cnf(f,c):
    app=''
    #RHS is returned if it is a single lower case letter
    if len(f)==1 and not f.isupper():
        return f
    #Checks lower case to produce CNF string
    if not f[0].isupper():
        app=app+'<'+f[0]+'>'
        arr_list[c] = '<'+f[0]+'>'
        #Counter to maintain the arr_list sequence for LHS
        c = c + 1
        var_list['<'+f[0]+'>']=cnf(f[0],c)
    #Upper case just appends the RHS string
    else:
        app=app+f[0]
    #Condition to check for the rest of the string for string length greater than 1
    if len(f[1:])>1:
        app=app+'<'+f[1:]+'>'
        arr_list[c] = '<' + f[1:] + '>'
        # Counter to maintain the arr_list sequence for LHS
        c = c + 1
        var_list['<'+f[1:]+'>']=cnf(f[1:],c)
    # Condition to check for the rest of the string for uppercase string of length lesser than 1
    else:
        if f[1:].isupper():
            app=app+f[1:]
    #RHS value of CNF returned
    return app

#Recursive function call
var_list[s[0]]=cnf(first+rest,count)

#Final CNF Display
while (i<len(arr_list)):
    out=arr_list[i]+" -> "+var_list[arr_list[i]]
    print(out)
    i=i+1