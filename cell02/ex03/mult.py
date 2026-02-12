first_num = int(input('Enter the first number '))
print(first_num)
second_num = int(input('Enter the second number '))
print(second_num)
Ans = first_num * second_num

print(f'{first_num} x {second_num} = {Ans}')
if Ans > 0:
    print('The result is Positive')
elif Ans < 0:
    print('The result is Negative')
else:
    print('The result is Positive and Negative')
#print(f'you Answer is {Ans}.')
