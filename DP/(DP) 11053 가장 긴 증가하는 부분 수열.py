'''
https://www.acmicpc.net/problem/11053
가장 긴 증가하는 부분 수열
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	76175	29452	19383	36.937%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
'''

import sys
input = sys.stdin.readline

N = int(input())

A = tuple(map(int,input().split()))

dp = [1 for _ in range(N + 1)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max((dp[j] + 1, dp[i]))

print(max(dp))


'''
N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]

print(dp)
for i in range(1,N):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        j = len(dp)-1
        while j > 0:
            if dp[j-1] < li[i]:
                break
            j -= 1
        dp[j] = li[i]
        print('now')
    print(dp)
print(len(dp))


13
80 70 60 60 30 50 40 10 40 20 30 25 15  
'''