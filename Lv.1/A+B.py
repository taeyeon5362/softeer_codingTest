import sys

T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    sum = 0
    for i in a :
        sum += i
    
    print('Case #{}: {}'.format(test_case, sum))


/*
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

제약조건
두 정수 A와 B는 1이상 9이하의 정수이다.

입력형식
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.

출력형식
각 테스트 케이스마다 "Case #(테스트 케이스 번호): "를 출력한 다음, A+B를 출력한다.
테스트 케이스 번호는 1부터 시작한다.

입력예제1
5
1 1
2 3
3 4
9 8
5 2
출력예제1
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
*/
