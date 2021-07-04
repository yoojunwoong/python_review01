# 숫자를 입력받아 최댓값,최솟값, 최댓값-최솟값 구하기.

# 3개의 숫자를 입력 받아서
# 단, 숫자는 두자리 숫자를 입력 받아야 하며 양수를 입력 받아야 한다.
# 이외의 숫자가 입력 될때는 프로그램 종료 한다.
# 최대값과 최소값을 출력 하고
# 최대값과 최소값의 차이를 출력 하시오

num1 = int(input('첫번째 숫자를 입력하시오'));
num2 = int(input('두번째 숫자를 입력하시오'));
num3 = int(input('세번째 숫자를 입력하시오'));

if not(10>num1//10>=1) and (10>num2//10>=1) and (10>num3//10>=1):
    print('값 오류')
    exit(0);

if (num1 > num2 and num3):
        max = num1;
elif(num2 > num1 and num3):
        max = num2;
elif(num3 > num1 and num2):
        max = num3;

if (num1 < num2 and num3):
        min = num1;
elif (num2 < num1 and num3):
        min = num2;
elif (num3 < num1 and num2):
        min = num3;

print(max); #최댓값
print(min); #최솟값
print(max-min); #최댓값 -최솟값


