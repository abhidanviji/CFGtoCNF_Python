str =  input('Enter Rule')#A -> ABceDFS
s = str.split( )
var_list={}
arr_list={}
count=0
i=0
left=s[0]
right=s[2]
first=right[0]
rest=right[1:]
arr_list[count]=left
count=count+1

def cnf(f,c):
    app=''
    if len(f)==1 and not f.isupper():
        return f
    if not f[0].isupper():
        app=app+'<'+f[0]+'>'
        arr_list[c] = '<'+f[0]+'>'
        c = c + 1
        var_list['<'+f[0]+'>']=cnf(f[0],c)
    else:
        app=app+f[0]
    if len(f[1:])>1:
        app=app+'<'+f[1:]+'>'
        arr_list[c] = '<' + f[1:] + '>'
        c = c + 1
        var_list['<'+f[1:]+'>']=cnf(f[1:],c)
    else:
        if f[1:].isupper():
            app=app+f[1:]
    return app

var_list[s[0]]=cnf(first+rest,count)

while (i<len(arr_list)):
    out=arr_list[i]+" -> "+var_list[arr_list[i]]
    print(out)
    i=i+1