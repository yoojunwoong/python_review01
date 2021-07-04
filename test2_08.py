# max함수의 초기화와 조건문을 사용하여 최댓값 구하기.

# 두개의 숫자를 입력 받는다
# 두수 중 최대 값을 출력하시오.
num1 = int(input('input num1..'));
num2 = int(input('input num2..'));
max = 0; # 두개의 숫자의 큰값을 max 값에 넣는다.

if (num1 > num2):
    max = num1;
elif(num1 == num2):
    max = num1
else:
    max = num2;
print('최댓값',':',max);





