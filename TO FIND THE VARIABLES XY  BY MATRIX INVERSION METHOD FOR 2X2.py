ch='yes'
while(ch=='yes'):
    
    T='ENTER THE COEFFIENT OR THREE EQUATIONS XYZ '
    print(T.center(80,'#'),'\n')
    X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
    Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
    x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
    y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
    c1=int(input('ENTER THE CONSTANT OF C1:\t'))
    c2=int(input('ENTER THE CONSTANT OF C2:\t'))
#adj=j
#A1=determinent of matrix
    T2='TO FIND THE SOLUTION WE PROCIDE THE INSTRUCTION BY MATRIX INVERSION METHODE'
    print(T2.center(140,'#'),'\n')
#FIRST WE FIND THE A INVERSE TO USE THE EXPRESSION X=A^-1*B
    A1=X*y-x*Y
    print('A=','\t',list([X,Y]))
    print('\t',list([x,y]),'\n')
    print('|A|=',X,'*',y,'-',x,'*',Y)
    print('THEREFORE |A|=',A1,'\n')
#HENCE WE FIND THE DETERMINENT OF A MATRIX
#WE USE IF CLAUSE TO CONTINUE OR DISCONTINUE THE PROGRAME
#IF THE GIVEN CONDITION IS TRUE WE CAN FIND THE VARIABLES XYZ
#ELSE THE CODE WILL BE DISCONTINUE THE PROCESS
    if (A1!=0):
            print('|A| IS !=0 THEREFORE A^-1 IS EXIST','\n')
            print('THE EXPRESSION TO FIND THE A^-1=1/|A|*B\n')
            print('THE DETERMINENT OF MATRIX IS=\t',A1,'\n')
            print('THE CONSTANT VALUES B ARE=','\t',list([c1]),'\n','\t\t\t\t',list([c2]),'\n')
            A=y
            B=-Y
            C=-x
            D=X
            print('THEREFORE ADJ(A)=\t',list([A,B]),'\n','\t\t\t',list([C,D]),'\n')
            M=A*c1+B*c2
            N=C*c1+D*c2
            print('\t\t\t\t','=','1/',A1,'*',list([M]))
            print('\t\t\t\t','=','1/',A1,'*',list([N]),'\n')
#WE DIVIDE THE ALL MULTIPLIED VALUES BY THE DETERMINENT A MATRIX
            print('\t\t\t\t','=',list([round(M/A1)]))
            print('\t\t\t\t','=',list([round(N/A1)]),'\n')
            print('THE VALUE OF THE VARIABLE X IS:',round(M/A1))
            print('THE VALUE OF THE VARIABLE Y IS:',round(N/A1))
#HENCE WE FIND THE SOLUTION FOR THE GIVEN EQUATION
    else:
        print('A1 IS =0 SO THE A^-1 IS NOT EXISTS')

#OTHERWISE WE CAN'T FIND THE SOLUTION
    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')



