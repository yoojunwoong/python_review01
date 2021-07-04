# random 패키지를 이용하여, 1~10사이의 값을 구하기.
import random
print('start......');
num = random.randint(1,10);

while True:
    cmd = input('input Number(q:exit)...');
    if cmd == 'q':
        print('bye');
        break;
    else:
        int_num = int(cmd);
        if int_num == num:
            print('ok');
        else:
            print('Fail');

print('end.....');

