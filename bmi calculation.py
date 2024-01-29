height = float(input("Enter Your Height: "))
weight = int(input("Enter Your Weight: "))

bmi = weight/pow(height/100,2)

if bmi <= 18.4:
        print('Your BMI is', bmi,'underweight')
        
elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'Normal')

elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'Overweight')

elif bmi > 30:
        print('Your BMI is', bmi,'You have to go to the gym')
else:
    print("Wrong input")


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(numbers_list)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_sum = 0
for num in numbers_list:
    if num % 2 == 0:
        even_sum += num

# Print the result
print("Sum of even numbers:", even_sum)
