ch='yes' 
while(ch=='yes'):
    p=input("ENTER THE FUNTION TO BE DIFFERENTIATE:\t")
    wrt=input("ENTER THE FUNTION WITH RESPECT TO :\t")
    c=int(input("ENTER THE COEFFITIANTE OF X:\t"))
    n=int(input("ENTER THE POWER OF THE FUNTION:\t")) 
    ab=input("DO YOU WANT TO ADD OR SUBRACT ANYTHING ")
    if(ab=='yes'):
        B=input("ENTER THE BINARY OPERATER TO BE USE")
        n1=int(input("ENTER THE POWER OF THE FUNTION:\t"))
        c1=int(input("ENTER THE COEFFITIANTE OF X:\t"))
        C=input("ENTER THE CONSTANT VALUE FOR THE EQUATION")
    if(ab=='yes'):
        print("\n\tTHE GIVEN EQUATION IS:\t",c,'*',p,'^',n,B,c1,'*',p,'^',n1,B,C)
    else:
        print('THE GIVEN EQUATION IS:\t',c,'*',p,'^',n)
        
    if(wrt==p and ab!='yes'):
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'*','[','d',p,'/','d',wrt,'=',1,']')
    elif(wrt==p and ab=='yes'):
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'*','[','d',p,'/','d',wrt,'=',1,']',B,n1*c1,'*',p,'^',n1-1,'*','[','d',p,'/','d',wrt,'=',1,']')
    if(wrt!=p and ab!='yes'):
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'d',p,'/','d',wrt)    
    elif(wrt!=p and ab=='yes'):
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'d',p,'/','d',wrt,B,n1*c1,'*',p,'^',n1-1,'d',p,'/','d',wrt)    

    o=input("IF YOU WANT TO FIND F''(X)..........")    
    if(o=='yes'):
        x1=n*c  
        x2=n-1
        x3=n-2
        if(ab=='yes'):
            a1=n1*c1
            a2=n1-1
            a3=n1-2
        if(wrt==p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']')
        elif(wrt==p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']',B,a1*a2,'*',p,'^',a3,'*','[','d',p,'/','d',wrt,'=',1,']')
        if(wrt!=p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt)    
        elif(wrt!=p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,B,a1*a2,'*',p,'^',a3,'d',p,'/','d',wrt)    
    else:
        x1=n*c 
        x2=n-1
        x3=n-2
        if(ab=='yes'): 
            a1=n1*c1
            a2=n1-1
            a3=n1-2
        print("THANKING YOU FOR FOUND F''(X)")
    o1=input("IF YOU WANT TO FIND F'''(X).........")
    if(o1=='yes'):
        x1=x1*x2
        x2=n-2
        x3=n-3
        if(ab=='yes'):
            a1=a1*a2
            a2=n1-2
            a3=n1-3
        if(wrt==p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']')
        elif(wrt==p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']',B,a1*a2,'*',p,'^',a3,'*','[','d',p,'/','d',wrt,'=',1,']')
        if(wrt!=p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt)    
        elif(wrt!=p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,B,a1*a2,'*',p,'^',a3,'d',p,'/','d',wrt)        
    else:
        x1=x1*x2 
        x2=n-2
        x3=n-3
        if(ab=='yes'): 
            a1=a1*a2
            a2=n1-2
            a3=n1-3
            print("THANKING YOU FOR FOUND F'''(X)")
    o2=input("IF YOU WANT TO FIND F'4(X)..........")
    if(o2=='yes'):
        x1=x1*x2
        x2=n-3
        x3=n-4
        if(ab=='yes'):
            a1=a1*a2
            a2=n1-3
            a3=n1-4
        if(wrt==p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']')
        elif(wrt==p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']',B,a1*a2,'*',p,'^',a3,'*','[','d',p,'/','d',wrt,'=',1,']')
        if(wrt!=p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt)    
        elif(wrt!=p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,B,a1*a2,'*',p,'^',a3,'d',p,'/','d',wrt)    
    else:
        x1=x1*x2
        x2=n-3
        x3=n-4
        if(ab=='yes'): 
            a1=a1*a2
            a2=n1-3
            a3=n1-4
            print("THANKING YOU FOR FOUND F'4(X)")
    o3=input("IF YOU WANT TO FIND F'5(X)..........")
    if(o3=='yes'):
        x1=x1*x2
        x2=n-4
        x3=n-5
        if(ab=='yes'):
            a1=a1*a2
            a2=n1-4
            a3=n1-5
        if(wrt==p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']')
        elif(wrt==p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']',B,a1*a2,'*',p,'^',a3,'*','[','d',p,'/','d',wrt,'=',1,']')
        if(wrt!=p and ab!='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt)    
        elif(wrt!=p and ab=='yes'):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,B,a1*a2,'*',p,'^',a3,'d',p,'/','d',wrt)    
    else:
       print("THANKING YOU FOR FOUND F'5(X)")
    ch=input("DO YOU WANT TO FIND THE SOLUTION AGAIN..........")  
else:
 print('THANKING YOU FOR FINDING ALL SOLUTIONS')


