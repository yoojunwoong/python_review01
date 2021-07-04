# 월급을 이용하여, 세후금액과,연봉 직급 구하기 (if,elif조건문)

salary = int(input('input salary..?'));
month = salary - (salary * 0.038) - (salary * 0.102);
year = 12 * month;
print(month, year);
if year <= 3000:
    print('사원');
elif year <= 5000:
    print('대리');
else:
    print('과장');