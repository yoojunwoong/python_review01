# while True와 if,elif를 사용하여, 선택옵션 구현하기

print('start......');

while True:
    cmd = input('input command...(q,i,d,u,s)');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        print('Insert date...');
    elif cmd == 'd':
        print('Delect date...');
    elif cmd == 'u':
        print('Update date...');
    elif cmd == 's':
        y = input('Input year');
        print(y, 'Select date...');
    else:
        print('Invalid cmd.. Try again..');
print('end.....');

