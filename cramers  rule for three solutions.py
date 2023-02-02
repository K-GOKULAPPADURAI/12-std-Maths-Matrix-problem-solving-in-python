ch='yes'
while(ch=='yes'):
    
    T='ENTER THE COEFFIENT OR THREE EQUATIONS XYZ '
    print(T.center(80,'#'),'\n')
    X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
    Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
    Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
    x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
    y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
    z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
    j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
    k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
    l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
    D1=int(input('ENTER THE CONSTANT OF D1:\t'))
    D2=int(input('ENTER THE CONSTANT OF D2:\t'))
    D3=int(input('ENTER THE CONSTANT OF D3:\t'))
    T2='TO FIND THE SOLUTION WE PROCIDE THE INSTRUCTION BY CRAMERS RULE'
    print(T2.center(80,'#'),'\n')
    A1=X*(y*l-k*z)-Y*(x*l-j*z)+Z*(x*k-j*y)
    print('A=','\t',list([X,Y,Z]))
    print('\t',list([x,y,z]))
    print('\t',list([j,k,l]),'\n','THE CONSTANT VALUES D ARE=','\t',list([D1]),'\n','\t\t\t\t',list([D2]),'\n','\t\t\t\t',list([D3]),'\n')
    print('DEL |A|=',X,'*','(',y,'*',l,'-',k,'*',z,')','-',Y,'*','(',x,'*',l,'-',j,'*',z,')','+',Z,'*','(',x,'*',k,'-',j,'*',y,')','\n')
    print('THEREFORE DEL |A|=',A1,'\n')
    T3="TO FIND THE XYZ VARIABLE BY THE CRAMERS RULE BY ONE BY ONE FOR ALL THREE a,b,c"
    print(T3.center(80,'#'),'\n')
    print('a=','\t',list([D1,Y,Z]))
    print('\t',list([D2,y,z]))
    print('\t',list([D3,k,l]),'\n')
    a=D1*(y*l-k*z)-Y*(D2*l-D3*z)+Z*(D2*k-D3*y)
    print('|a|=',D1,'*','(',y,'*',l,'-',k,'*',z,')','-',Y,'*','(',D2,'*',l,'-',D3,'*',z,')','+',Z,'*','(',D2,'*',k,'-',D3,'*',y,')','\n')
    print('THE DETERMINATION OF THE a is=\t',a,'\n')
    print('b=','\t',list([X,D1,Z]))
    print('\t',list([x,D2,z]))
    print('\t',list([j,D3,l]),'\n')
    b=X*(D2*l-D3*z)-D1*(x*l-j*z)+Z*(x*D3-j*D2)
    print('|b|=',X,'*','(',D2,'*',l,'-',D3,'*',z,')','-',D1,'*','(',x,'*',l,'-',j,'*',z,')','+',Z,'*','(',x,'*',D3,'-',j,'*',D2,')','\n')
    print('THE DETERMINATION OF THE b is=\t',b,'\n')
    print('c=','\t',list([X,Y,D1]))
    print('\t',list([x,y,D2]))
    print('\t',list([j,k,D3]),'\n')
    c=X*(y*D3-k*D2)-Y*(x*D3-j*D2)+D1*(x*k-j*y)
    print('|c|=',X,'*','(',y,'*',D3,'-',k,'*',D2,')','-',Y,'*','(',x,'*',D3,'-',j,'*',D2,')','+',D1,'*','(',x,'*',k,'-',j,'*',y,')','\n')
    print('THE DETERMINATION OF THE c is=\t',c,'\n')
    print("THE VALUE OF THE VARIABLE X=\t",round(a/A1),'\n')
    print("THE VALUE OF THE VARIABLE Y=\t",round(b/A1),'\n')
    print("THE VALUE OF THE VARIABLE Z=\t",round(c/A1),'\n')



    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')
