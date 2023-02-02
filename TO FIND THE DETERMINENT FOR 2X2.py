M11=int(input('enter the value of m11'))
M12=int(input('enter the value of m12'))
M21=int(input('enter the value of m13'))
M22=int(input('enter the value of m14')) 
def cofactor(a,b,c,d):
    a=M11*M22
    b=-(M21*M12)
    print(a+b)
cofactor(M11,M12,M21,M22)
'''
2 3 4
5 6 7
8 9 2
#cofact of m11
m22 m23
m32 m33
#cofact of m22
m11 m13
m31 m33
#cofact of m33
m11 m12
m21 m22
'''
