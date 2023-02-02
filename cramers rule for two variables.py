ch='yes'
while(ch=='yes'):
    
    T='ENTER THE COEFFIENT OR THREE EQUATIONS XY '
    print(T.center(80,'#'),'\n')
    X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
    Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
    x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
    y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
    D1=int(input('ENTER THE CONSTANT OF D1:\t'))
    D2=int(input('ENTER THE CONSTANT OF D2:\t'))
    T2='TO FIND THE SOLUTION WE PROCIDE THE INSTRUCTION BY CRAMERS RULE'
    print(T2.center(80,'#'),'\n')
    A1=X*y-x*Y
    print('A=','\t',list([X,Y]))
    print('\t',list([x,y]),'\n')
    print('\tTHE CONSTANT VALUES D ARE=','\t',list([D1]),'\n','\t\t\t\t\t',list([D2]),'\n')
    print('DEL |A|=',X,'*',y,'-',x,'*',Y,'\n')
    print('THEREFORE DEL |A|=',A1,'\n')
    T3="TO FIND THE XYZ VARIABLE BY THE CRAMERS RULE BY ONE BY ONE FOR ALL THREE a,b"
    print(T3.center(80,'#'),'\n')
    print('a=','\t',list([D1,Y]))
    print('\t',list([D2,y]),'\n')
    a=D1*y-D2*Y
    print('|a|=',D1,'*',y,'-',D2,'*',Y,'\n')
    print('THE DETERMINATION OF THE a is=\t',a,'\n')
    print('a=','\t',list([X,D1]))
    print('\t',list([x,D2]),'\n')
    b=X*D2-x*D1
    print('|b|=',X,'*',D2,'-',x,'*',D1,'\n')
    print('THE DETERMINATION OF THE b is=\t',b,'\n')
    print('b=','\t',list([X,Y,D1]))
    print('\t',list([x,y,D2]))
    print("THE VALUE OF THE VARIABLE X=\t",round(a/A1),'\n')
    print("THE VALUE OF THE VARIABLE Y=\t",round(b/A1),'\n')
    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')
