# %와 //, and와 or을 사용하여 조건 맞추기

# 한개의 숫자를 입력 받아
# 3의 배수이고 짝수이고 양수이면 출력,그렇지 않으면 FAIL을 출력하시오.
num = int(input('input Num.....'));
if num > 0 and num%3 == 0 and num%2 ==0:
    print('OK');
else:
    print('FAIL');

# 두자리 숫자만 입력을 받는다.
# 단 두개의 숫자는 모두 한자리로 입력되어야 한다.
# 한자리가 아니고 음수이면 프로그램을 종료시킨다.
# exit(0); __ 프로그램 종료
num1 = int(input('input Num1.....'))
num2 = int(input('input Num2.....'))
if not(((num1 // 10) < 1 and (num2 // 10)<1) or (num1 < 0 and num2 < 0)):
   print('not in range Num');
   exit(0);


