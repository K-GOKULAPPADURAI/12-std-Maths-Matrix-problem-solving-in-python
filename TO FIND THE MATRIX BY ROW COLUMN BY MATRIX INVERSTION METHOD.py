ch='yes'
while(ch=='yes'):
    T1="TO FIND THE VARIABLES X,Y&Z BY MATRIX INVERSION METHOD"
    print(T1.center(100,'#'),'\n')
    M11=int(input('ENTER A NUMBER OF THE ELEMENT M11:''\t'))
    M12=int(input('ENTER A NUMBER OF THE ELEMENT M12:''\t'))
    M13=int(input('ENTER A NUMBER OF THE ELEMENT M13:''\t'))
    M21=int(input('ENTER A NUMBER OF THE ELEMENT M21:''\t'))
    M22=int(input('ENTER A NUMBER OF THE ELEMENT M22:''\t'))
    M23=int(input('ENTER A NUMBER OF THE ELEMENT M23:''\t'))
    M31=int(input('ENTER A NUMBER OF THE ELEMENT M31:''\t'))
    M32=int(input('ENTER A NUMBER OF THE ELEMENT M32:''\t'))
    M33=int(input('ENTER A NUMBER OF THE ELEMENT M33:''\t'))
    c1=int(input('ENTER THE CONSTANT OF C1:\t'))
    c2=int(input('ENTER THE CONSTANT OF C2:\t'))
    c3=int(input('ENTER THE CONSTANT OF C3:\t'))
    T2='STEP1:\tTHE EXPRESSION TO SOLVE THE EQUATIONS BY MATRIX INVERSTION METHOD'
    print(T2.center(100,'#'),'\n')
    print('XA=B\nX=A^-1*B\nWE WANT TO FIND FIRST A^1\nWE KNOW THAT A^1=1/|A|*ADJ(A)')
    print('A=','\t',list([M11,M12,M13]))
    print('\t',list([M21,M22,M23]))
    print('\t',list([M21,M22,M23]),'\n')
    print('|A|=',M11,'*','(',M22,'*',M33,'-',M32,'*',M23,')','-',M12,'*','(',M21,'*',M33,'-',M31,'*',M23,')','+',M13,'*','(',M21,'*',M32,'-',M31,'*',M22,')','\n')
    A1=M11*(M22*M33-M32*M23)-M12*(M21*M33-M31*M23)+M13*(M21*M32-M31*M22)
    print('THEREFORE |A|=',A1)
    if (A1!=0):
            print('|A| IS !=0 THEREFORE A^-1 IS EXIST')
            A=(M22*M33-M32*M23)
            B=(M23*M31-M33*M21)
            C=(M21*M32-M31*M22)
            D=(M32*M13-M12*M33)
            E=(M33*M11-M13*M31)
            F=(M31*M12-M11*M32)
            G=(M12*M23-M22*M13)
            H=(M13*M21-M23*M11)
            I=(M11*M22-M21*M12)
            T="TO FIND THE XYZ VARIABLE MULTIPLE THE A^-1*B BY THE EXPRESSION XA=B "
            print(T.center(80,'#'),'\n')
            X=print('A^-1*B=\t\t\t\t','=','1/',A1,list([A,D,G]),'*',list([c1]))
            Y=print('\t\t\t\t','=','1/',A1,list([B,E,H]),'*',list([c2]))
            Z=print('\t\t\t\t','=','1/',A1,list([C,F,I]),'*',list([c3]),'\n')
            M=A*c1+D*c2+G*c3
            N=B*c1+E*c2+H*c3
            O=C*c1+F*c2+I*c3
            print('\t\t\t\t','=','1/',A1,'*',list([M]))
            print('\t\t\t\t','=','1/',A1,'*',list([N]))
            print('\t\t\t\t','=','1/',A1,'*',list([O]),'\n')            
            print('\t\t\t\t','=',list([round(M/A1)]))
            print('\t\t\t\t','=',list([round(N/A1)]))   
            print('\t\t\t\t','=',list([round(O/A1)]),'\n')
            print('THE VALUE OF THE VARIABLE X IS:',round(M/A1))
            print('THE VALUE OF THE VARIABLE Y IS:',round(N/A1))
            print('THE VALUE OF THE VARIABLE Z IS:',round(O/A1))
    else:
        print('A1 IS =0 SO THE A^-1 IS NOT EXISTS')
    ch=input('DO YOU WANT TO FIND ANOTHER SOLUTION:\t')
else:
    print('OK THANHS FOR YOUR WORKING')

