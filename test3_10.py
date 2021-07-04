#for문과 stop(bool)문을 사용하여 값 제어하기.
for i in range(1,11):
    stop = False;
    for j in range(1,11):
        if i == 3 and j == 5:
            stop = True
            break;
        print(i,'-',j);
    print(i,'------------');
    if stop == True:
        break;
    print(i, '------------');
print(i,'------------');