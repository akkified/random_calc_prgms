# Calculating the mean absolute deviation from scratch
from statistics import mean

numbers = input("Enter numbers separated by a space:")
numbers = numbers.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
   
mean_value = mean(numbers)
mean_absolute_deviation = mean([abs(number-mean_value) for number in numbers])
print(mean_absolute_deviation)
