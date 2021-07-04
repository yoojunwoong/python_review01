# 1~100 까지의 숫자 중 홀수의 합과 평균, 짝수의 합과 평균을 구하시오.

sum1 = 0;
sum2 = 0;
cnt1 = 0;
cnt2 = 0;
for a in range(1,101):
    if a%2 == 1:  #홀수
       a += 1;
       cnt1 += 1;
       sum1 += a;
    else:
        a +=1;
        cnt2 += 1;
        sum2 += a;

print(a-1); #최종값에서 1을 더하기 때문에 빼주기 ex) a값의 최종값은 100+1 이기때문에 빼주기
print(sum1);
print(sum1/cnt1);
print(sum2);
print(sum2/cnt2);
print('-------------');

sum3 = 0;
sum4 = 0;
sum5 = 0;
cnt3 = 0;
cnt4 = 0;
cnt5 = 0;

for b in range(1,1001):
    if b%2 == 0:
        b += 1;
        cnt3 += 1;
        sum3 += b;

print(b-1);
print(sum3);
print(sum3/cnt3);

for c in range(1,1001):
    if c%3 == 0:
        c += 1;
        cnt4 += 1;
        sum4 += c;

print(c-1);
print(sum4);
print(sum4/cnt4);

for d in range(1,1001):
    if d%5 == 0:
        d += 1;
        cnt3 += 1;
        sum3 += d;

print(d-1);
print(sum3);
print(sum3/cnt3);








