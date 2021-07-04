# range, while을 시용하여 값의 합,평균을 구하기.

# 1 ~ 10 합을 구하시오.
sum = 0;
cnt = 0;

for i in range(1,11):
    sum += i;
    cnt += 1;

print(cnt);
print(sum);
print(sum/cnt);

#while
# 1~10합을 구하시오.

a = 1;
sum2 = 0;
while a < 11:
    sum2 += a;
    a += 1;

print(a-1); #카운트(cnt)
print(sum2);
print(sum2/(a-1));





