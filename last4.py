import math
print ("x^1 \t x^2 \t x^3")
print ("----------------------")
for num in range(1,6):
    for power1 in range(1,2):
        for power2 in range(2,3):
            for power3 in range(3,4):
                result1 = math.pow(num, power1)
                result2 = math.pow(num, power2)
                result3 = math.pow(num, power3)
                print(result1, "\t", result2, "\t", result3)
 
