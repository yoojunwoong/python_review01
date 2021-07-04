# workshop
# 1~100 까지의 숫자 중 3의 배수의 합과 7의배수의 합의 차를 구하시오.
a = 0;
sum1 = 0;
sum2 = 0;
for a in range(1,101):
    if a%3 == 0:
       sum1 += a;

for a in range(1, 101):
    if a%7 == 0:
       sum2 += a;

print('3의 배수의 합:',sum1);
print('7의 배수의 합:',sum2);
print('두합의 차이:',sum1-sum2);



