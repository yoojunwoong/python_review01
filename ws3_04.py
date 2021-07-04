# workshop
# 10행 10열의 정방 행렬 구조에 지형이 있다.
# 각 셀의 길이는 1미터 이다.
# 대각선의 길이를 구하시오.

for i in range(1,11):
    for j in range(1,11):
        print(i,'-',j);
        print('대각선의 길이:',(i**2+j**2)**0.5)