import sys

T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    sum = 0
    for i in a :
        sum += i
    
    print('Case #{}: {}'.format(test_case, sum))
