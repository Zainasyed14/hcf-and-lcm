num1 = int(input("Enter your first value : "))
num2 = int(input("Enter your second value : "))
ognum1=num1
ognum2=num2
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
hcf=num1
print("hcf of num1 and num 2 is : " , hcf)
lcm=ognum1*ognum2/hcf
print("LCM of num1 and num2 is : " , lcm)