# for 문 2번 사용하기...
for i in range(1,6):
    for j in range(1,6):
        print(i,'-',j);

print('--------------');

# while loop 2번 사용하기
a = 1;
while a < 6:
    a2 = 1;
    while a2 < 6:
        print(a,'-',a2);
        a2 += 1;
    a += 1;
