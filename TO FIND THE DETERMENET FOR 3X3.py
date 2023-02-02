ch='yes'
while ch=='yes':

    M11=int(input('ENTER A NUMBER OF THE ELEMENT M11:''\t'))
    M12=int(input('ENTER A NUMBER OF THE ELEMENT M12:''\t'))
    M13=int(input('ENTER A NUMBER OF THE ELEMENT M13:''\t'))
    M21=int(input('ENTER A NUMBER OF THE ELEMENT M21:''\t'))
    M22=int(input('ENTER A NUMBER OF THE ELEMENT M22:''\t'))
    M23=int(input('ENTER A NUMBER OF THE ELEMENT M23:''\t'))
    M31=int(input('ENTER A NUMBER OF THE ELEMENT M31:''\t'))
    M32=int(input('ENTER A NUMBER OF THE ELEMENT M32:''\t'))
    M33=int(input('ENTER A NUMBER OF THE ELEMENT M33:''\t'))

    t="THE DETERMINENT OF GIVEN MATRIX IS ABOVE"
    print(t.center(80,'#'),'\n')
    print('A=','\t',list([M11,M12,M13]))
    print('\t',list([M21,M22,M23]))
    print('\t',list([M31,M32,M33]),'\n')
    print('|A|=',M11,'*','(',M22,'*',M33,'-',M32,'*',M23,')','-',M12,'*','(',M21,'*',M33,'-',M31,'*',M23,')','+',M13,'*','(',M21,'*',M32,'-',M31,'*',M22,')','\n')
    A1=M11*(M22*M33-M32*M23)-M12*(M21*M33-M31*M23)+M13*(M21*M32-M31*M22)
    print('|A|=',A1)
    ch='yes'
    ch=input("ENTER YOUR CHOICE")
else:
    print("thankyou")
