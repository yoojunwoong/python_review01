# for을 이용하여 1~12사이 홀수값 출력하기
for i in range(1,13):
    if i%2 == 1:
        print(i);

# while loop를 사용하여 1~12까지의 짝수값 출력하기.
s = 1;
while s < 13:
    if s%2 == 0:
        print(s);
    s += 1

# 1~100까지의 숫자 중 홀수 이면서 3의 배수들의 합과 평균을 구하시오.
sum = 0;
cnt = 0;
for a in range(1,101):
    if (a%3 == 0 and a%2 == 1):
        sum += a;
        cnt += 1;

print(sum);
print(sum/cnt);

# while
b = 1;
sum = 0;
cnt = 0;
while b < 101:
   if (b % 3 == 0 and b % 2 == 1):
        sum += b;
        cnt += 1;
   b += 1; #while loop 끝나고나면, 다시 실행시키기 위한 b+=1 값

print(b-1);
print(cnt);
print(sum);
print(sum/cnt);








