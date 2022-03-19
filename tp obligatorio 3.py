def diagonal(X,fila,col):
    t=0
    i=10
    j=0
    for i in range(fila):
        if col>=i:
            t=t+X[i][i]
    return t

X=[[1,3],[4,5]]
fila=2
col=2
t=diagonal(X,fila,col)
print(t)