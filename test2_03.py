# if문을 사용하여 사칙연산하기
num1 = int(input('input num1...?'))
num2 = int(input('input num2...?'))
op = input('input op(+ - / *)...?');
result = 0; #op가 해당하는 값이 없을시 출력되는 값
# if와 elif 사용중, if의 경우 모든조건고려, elif의 경우 위에서 걸러진것을 재사용x
# 따라서 elif를 사용하는경우, 프로그램의 속도에 더 유리함
if op == '+':
    result = num1 + num2;
if op == '-':
    result = num1 - num2;
if op == '/':
    result = num1 / num2;
if op == '*':
    result = num1 * num2;
print(result);





