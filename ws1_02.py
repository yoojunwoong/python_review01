# 2번째 workshop

num1 = int(input('첫번째 숫자를 입력하세요'));
num2 = int(input('두번째 숫자를 입력하세요'));
op = input('연산자를 입력하세요');
result1 = (num1+num2);
result2 = (num1-num2);
result3 = (num1*num2);
result4 = (num1/num2);

if op == '+':
    print(result1);
elif op == '-':
    print(result2);
elif op == '*':
    print(result3);
elif op == '/':
    print(result4);
# elif를 사용하여 여러 조건주기