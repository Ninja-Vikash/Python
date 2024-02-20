# WAP for calculating Average of two number without using addition operation
Num1 = float(input("Enter your 1st number : "))
Num2 = float(input("Enter your 2nd number : "))

# Explained Code
def Calculate_avg(Num1, Num2):
    if (Num1 > Num2):
        diff = (Num1 - Num2)
        half = diff/2
        avg = Num1 - half
        return avg
    
    elif (Num2 > Num1):
        avg = Num1 - (Num1 - Num2)/2
        diff = (Num2 - Num1)
        half = diff/2
        avg = Num2 - half
        return avg
    
# Short Code
def Calculate_avg(Num1, Num2):
    if (Num1 > Num2):
        avg = Num1 - (Num1 - Num2)/2
        return avg
    
    elif (Num2 > Num1):
        avg = Num2 - (Num2 - Num1)/2
        return avg
    
Avg = Calculate_avg(Num1, Num2)

print("Average =", Avg)