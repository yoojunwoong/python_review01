#생각해보기
#4과목 성적을 입력 받는다.
#4과목 평균이 90점 이상이면 "A학점"
#4과목 평균이 80점 이상이면 "B학점"
#4과목 평균이 70점 이상이면 "C학점"
#4과목 평균이 60점 이상이면 "D학점"
#4과목 평균이 60점 미만이면 "F학점"

num1 = int(input('국어성적을 입력하시오'))
num2 = int(input('수학성적을 입력하시오'))
num3 = int(input('영어성적을 입력하시오'))
num4 = int(input('과학성적을 입력하시오'))
result = 0;
result = (num1+num2+num3+num4)/4 # 4과목의 평균

if result >=90:
    print('A학점');
if 90> result >=80:
    print('B학점');
if 80> result >=70:
    print('C학점');
if 70> result >=60:
    print('D학점');
if 60> result:
    print('F학점');

print('---------------------');

#91~95 : A 96~100: A+
#81~85 : B 86~90: B+
#71~75 : C 76~80: C+
#61~65 : D 66~70: D+
#60 이하는 F

if 100>= result >=96:
    print('A+');
elif 95>= result >=91:
    print('A');
elif 90>= result >=86:
    print('B+');
elif 85>= result >=81:
    print('B');
elif 80>= result >=76:
    print('C+');
elif 75>= result >=71:
    print('C');
elif 70>= result >=66:
    print('D+');
elif 65>= result >=60:
    print('D');
else :
    print('F');








