ch='yes'
while(ch=='yes'):
    M11=int(input('ENTER A NUMBER OF THE ELEMENT M11:''\t'))
    M12=int(input('ENTER A NUMBER OF THE ELEMENT M12:''\t'))
    M13=int(input('ENTER A NUMBER OF THE ELEMENT M13:''\t'))
    M21=int(input('ENTER A NUMBER OF THE ELEMENT M21:''\t'))
    M22=int(input('ENTER A NUMBER OF THE ELEMENT M22:''\t'))
    M23=int(input('ENTER A NUMBER OF THE ELEMENT M23:''\t'))
    M31=int(input('ENTER A NUMBER OF THE ELEMENT M31:''\t'))
    M32=int(input('ENTER A NUMBER OF THE ELEMENT M32:''\t'))
    M33=int(input('ENTER A NUMBER OF THE ELEMENT M33:''\t'))
    A=(M22*M33-M32*M23)
    B=(M23*M31-M33*M21)
    C=(M21*M32-M31*M22)
    D=(M32*M13-M12*M33)
    E=(M33*M11-M13*M31)
    F=(M31*M12-M11*M32)
    G=(M12*M23-M22*M13)
    H=(M13*M21-M23*M11)
    I=(M11*M22-M21*M12)
    T="THE ADJOINT OF THE GIVEN MATRIX ELEMENTS ARE"
    print(T.center(80,'#'),'\n')
    X=print('\t\t\t\t',list([A,D,G]))
    Y=print('\t\t\t\t',list([B,E,H]))
    Z=print('\t\t\t\t',list([C,F,I]))
    ch=input("DO YOU WANT TO CONTINUE THE PROGRAM")
else:
    print("ok thanks")
