from math import cos, pi

def som(a,b):
    s=a+b
    return s
#end of function som()

def somDiff(a,b):
    s=a+b
    d=a-b
    return(s,d)
#end of function somDiff()

def Sbstrct_one_frm_func(x,func):
    y=-1+func(x)
    return(y)
#end of function Sbtrct_one_frm_func()

def pow_of_three(u):
    return(u**3)
#end of function pow_of_three()

def invrs(u):
    return(1/u)
#end of function invrs()

#main program
print("      ******")
print("    ***************")
print("   ** **    ******")
print("   *  *     *********")
print("   * 0    0 ******   *")
print(" *******************")
print("     ***********    *")
x,y,z=eval(input("Input 3 messages separated by ',' and written between ' \" ': "))
if(x!="skip"):
     print("Message 1:",x
      ,"\nMessage 2:",y
      ,"\nMessage 3:",z)
     if(len(x)>len(y) and len(x)>len(y)): print("Message 1 is the longest!!!")
     elif(len(y)>len(x) and len(y)>len(z)): print("Message 2 is the longest!!!")
     elif(len(z)>len(x) and len(z)>len(y)): print("Message 3 is the longest!!!")
     else: print("Congratulations! All messages are of equal size, or you didn't input anything >:(")
else:    
     num1,num2,num3=eval(input("Input your numbers: "))
     print(num1,num2,num3)
     if(num1!="skip"):
          if(num1>num2 and num1>num2): print("Number 1 is the longest!!!")
          elif(num2>num3 and num2>num1): print("Number 2 is the longest!!!")
          elif(num3>num2 and num3>num1): print("Number 3 is the longest!!!")
     for i in range(0,10,1):
         if i==6: break
         num=i+1
         print(num)
print(somDiff(3,4))
print(som(5,8))
print("substract 1 from 3^3:",Sbstrct_one_frm_func(3,pow_of_three))
print("substract 1 from 1/8:",Sbstrct_one_frm_func(8,invrs))
print("cos(pi)=",cos(pi))
