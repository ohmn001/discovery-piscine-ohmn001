num = int(input('please number is less than 25 '))
print(num)
if num < 25:
    for i in range(num , 26):
        print(f'Inside the loop, my vairable is {i}')
else:
    print('Error')


