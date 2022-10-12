
# ******************************
# Make your Code
# ******************************
# sarah Castorena
# SID 2028049

numbers = []
for i in range(5):
    numbers.append(int(input('Enter a number: ')))
avg = sum(numbers)/len(numbers)
numbers  = [i for i in range(len(numbers)) if numbers[i] > avg]    
print(*numbers, sep = ' ')