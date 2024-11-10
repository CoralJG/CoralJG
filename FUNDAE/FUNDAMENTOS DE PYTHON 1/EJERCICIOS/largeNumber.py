num1 = int(input("Primer num:"))
num2 = int(input("Primer num:"))
num3 = int(input("Primer num:"))

large_num = num1

if num2 > large_num:
   large_num = num2
    
if num3 > large_num:
   large_num = num3
    
print("El número más grande es: ",large_num)
