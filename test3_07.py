# while True를 사용하여 무한 loop 돌리기, break사용시 멈춤

print('start......');

while True:
    cmd = input('input command...');
    if cmd == 'q':
        print('bye');
        break;
    print('input cmd....');
    print(cmd);

print('end.....');

