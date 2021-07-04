# !과 ' ' (공백)의 bool의 여부판단, or연산자 사용
a = 10;
b = 20;
print(a!= b);

if a!=b:
    print('다른 값이다.');
else:
    print('같은 값이다.');

a =' ';
if a:
   print('True');
else:
   print('False');

b = 10;
c = 5;

if (b > 5) or (c < 5):
    print('ok');


