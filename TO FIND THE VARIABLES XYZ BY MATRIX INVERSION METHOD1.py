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
    c1=int(input('ENTER THE CONSTANT OF C1:\t'))
    c2=int(input('ENTER THE CONSTANT OF C2:\t'))
    c3=int(input('ENTER THE CONSTANT OF C3:\t'))
#adj=j
#A1=determinent of matrix
    T2='TO FIND THE SOLUTION WE PROCIDE THE INSTRUCTION BY MATRIX INVERSION METHODE'
    print(T2.center(140,'#'),'\n')
#FIRST WE FIND THE A INVERSE TO USE THE EXPRESSION X=A^-1*B
    A1=X*(y*l-k*z)-Y*(x*l-j*z)+Z*(x*k-j*y)
    print('A=','\t',list([X,Y,Z]))
    print('\t',list([x,y,z]))
    print('\t',list([j,k,l]),'\n')
    print('|A|=',X,'*','(',y,'*',l,'-',k,'*',z,')','-',Y,'*','(',x,'*',l,'-',j,'*',z,')','+',Z,'*','(',x,'*',k,'-',j,'*',y,')','\n')
    print('THEREFORE |A|=',A1,'\n')
#HENCE WE FIND THE DETERMINENT OF A MATRIX
#WE USE IF CLAUSE TO CONTINUE OR DISCONTINUE THE PROGRAME
#IF THE GIVEN CONDITION IS TRUE WE CAN FIND THE VARIABLES XYZ
#ELSE THE CODE WILL BE DISCONTINUE THE PROCESS
    if (A1!=0):
            print('|A| IS !=0 THEREFORE A^-1 IS EXIST','\n')
            print('THE EXPRESSION TO FIND THE A^-1=1/|A|*B\n')
            print('THE DETERMINENT OF MATRIX IS=\t',A1,'\n')
            print('THE CONSTANT VALUES B ARE=','\t',list([c1]),'\n','\t\t\t\t',list([c2]),'\n','\t\t\t\t',list([c3]),'\n')
            A=(y*l-k*z)
            B=(z*j-l*x)
            C=(x*k-j*y)
            D=(k*Z-Y*l)
            E=(l*X-Z*j)
            F=(j*Y-X*k)
            G=(Y*z-y*Z)
            H=(Z*x-z*X)
            I=(X*y-x*Y)
            print('THEREFORE ADJ(A)=\t',list([A,D,G]),'\n','\t\t\t',list([B,E,H]),'\n','\t\t\t',list([C,F,I]),'\n')
            T3="TO FIND THE XYZ VARIABLE MULTIPLE THE A^-1*B BY THE EXPRESSION XA=B "
            X=print('A^-1*B=\t\t\t\t','=','1/',A1,list([A,D,G]),'*',list([c1]))
            Y=print('\t\t\t\t','=','1/',A1,list([B,E,H]),'*',list([c2]))
            Z=print('\t\t\t\t','=','1/',A1,list([C,F,I]),'*',list([c3]),'\n')
#WE MULTIPLE THE A^-1 AND B CONSTANT VALUES
            M=A*c1+D*c2+G*c3
            N=B*c1+E*c2+H*c3
            O=C*c1+F*c2+I*c3
            print('\t\t\t\t','=','1/',A1,'*',list([M]))
            print('\t\t\t\t','=','1/',A1,'*',list([N]))
            print('\t\t\t\t','=','1/',A1,'*',list([O]),'\n')
#WE DIVIDE THE ALL MULTIPLIED VALUES BY THE DETERMINENT A MATRIX
            print('\t\t\t\t','=',list([round(M/A1)]))
            print('\t\t\t\t','=',list([round(N/A1)]))
            print('\t\t\t\t','=',list([round(O/A1)]),'\n')
            print('THE VALUE OF THE VARIABLE X IS:',round(M/A1))
            print('THE VALUE OF THE VARIABLE Y IS:',round(N/A1))
            print('THE VALUE OF THE VARIABLE Z IS:',round(O/A1))
#HENCE WE FIND THE SOLUTION FOR THE GIVEN EQUATION
    else:
        print('A1 IS =0 SO THE A^-1 IS NOT EXISTS')

#OTHERWISE WE CAN'T FIND THE SOLUTION
    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')
