print('Welcome to your BMI calculator!!!')
height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

bmi = round(weight / (height * height))

if bmi < 18.5:
	print(f'Your BMI is {bmi}. You are underweight.')
elif bmi < 25:
	print(f'Your BMI is {bmi}. You are normal weight.')	
elif bmi < 30:
	print(f'Your BMI is {bmi}. You are overweight.')	
elif bmi < 35:
	print(f'Your BMI is {bmi}. You are obese')	
else:
	print(f'Your BMI is {bmi}. You are clinically obese.')

	
