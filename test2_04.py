#생각해보기
#두 개의 숫자를 입력 받아 두수의 합을 구하고, 홀수 인지 짝수인지를 출력하시오.
# if esle 문과 %연산자를 이용하여 값을 짝수 여부 확인
num1 =input('input num1...?');
num2 =input('input num2...?');
sum = int(num1) + int(num2);
print(sum);

if sum % 2 == 0 :
    print('짝수');
else:
    print('홀수');


