#직각삼각형의 한변의 길이를 구하기.(**거듭제곱)

num1 = int(input('가로의 길이를 입력하시오'));
num2 = int(input('세로의 길이를 입력하시오'));

if (num1 < 0 and num2 <0):
    exit(0);

print(((num1**2)+(num2**2))**0.5);

