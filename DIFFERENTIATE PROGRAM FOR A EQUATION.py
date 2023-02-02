print('syntax for the input is: #ax^m+bx^n+c,#aax^m+bbx^n+c')
E=input("ENTER THE EQUATION FOR INPUT COEFFICIENNT IN ONE DIGIT:\t")
e=len(E)
if(e==11 or e==12):
    C=int(E[0])
    p=E[1]
    bp=E[2]
    n=int(E[3])
    ba=E[4]
    C1=int(E[5])
    p1=E[6]
    bp1=E[7] 
    n1=int(E[8])
    bpa1=E[9]
    c=E[10]
    print(C*n,p,bp,n-1,ba,C1*n1,p1,bp1,n1-1)#ax^m+bx^n+c    
else:
    E1=E
    C=int(E1[0])
    C1=int(E1[1])
    p=E1[2]
    bp=E1[3]
    n=int(E1[4])
    bo=E1[5]
    C2=int(E1[6])
    C3=int(E1[7])
    o=int(E1[6:8])
    p1=(E1[8])
    bp1=E1[9]
    n1=int(E1[10])
    bo1=E1[11]
    c=E1[12]
    o1=int(E1[:2])
    print(o1*n,p,bp,n-1,bo,o*n1,p1,bp1,n1-1)#aax^m+bbx^n+c


