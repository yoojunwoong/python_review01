# workshop

#Number guess 게임 구현
#1) 게임 진행 카운트를 출력 한다.
#2) 5회가 되면 게임 Fail !
#3) 입력한 숫자가 큰지 작은지 출력
#4) 게임이 종료 되면(Collect, incollect 이건 다시 게임을 시작 할 수 있게 한다.)

import random
print('start..............');
num = random.randint(1, 10);
cnt = 1;
while True:
    cmd = input('Input Number(q:exit): ');
    if cmd == 'q':
        print('bye');
        break;
    else:
        int_num = int(cmd);
        if int_num == num:
            print(cnt,'Collect');
            print('bye')
            break;
        else:
            if cnt < 5:
                print(cnt,'Fail');
                if int_num > num:
                    print('input Num > random Num ');
                else:
                    print('input Num < random Num ');
                cnt += 1;
            else:
                print(cnt,'Incorrect');
                if int_num > num:
                    print('big');
                else:
                    print('small');
                cont = input('regame? (yes/no)');
                if cont == 'yes':
                    cnt = 1;
                else:
                    print('bye');
                    break;