
# ******************************
# Make your Code
# ******************************
# sarah Castorena
# SID 2028049

numbers = []
num2 = []
for i in range(5):
    numbers.append(int(input('Enter a number: ')))   
avg = int(sum(numbers)/len(numbers))
for i in range(len(numbers)):
    if numbers[i] > avg:
       num2.append(numbers[i])  
for i in range(len(num2)):
   print(num2[i], end = ' ')