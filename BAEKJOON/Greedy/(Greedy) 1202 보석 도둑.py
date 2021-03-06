'''
https://www.acmicpc.net/problem/1202
보석 도둑 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	24226	5600	3936	22.266%
문제
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

예제 입력 1 
2 1
5 10
100 100
11
예제 출력 1 
10
예제 입력 2 
3 2
1 65
5 23
2 99
10
2
예제 출력 2 
164
힌트
두 번째 예제의 경우 첫 번째 보석을 두 번째 가방에, 세 번째 보석을 첫 번째 가방에 넣으면 된다.

출처
Contest > Croatian Open Competition in Informatics > COCI 2013/2014 > Contest #1 4번

문제를 번역한 사람: baekjoon
잘못된 조건을 찾은 사람: eeight
알고리즘 분류
자료 구조
그리디 알고리즘
정렬
우선순위 큐
'''


import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

lst = []
for _ in range(N):
    m, v = map(int, input().split())
    lst.append((v,m))

lst.sort(reverse = True)

bags = []
for _ in range(K):
    bags.append(int(input()))

bags.sort()

total = 0
lst = deque(lst)

for w in bags:
    new_lst = deque()
    appended = False
    
    while lst:
        now = lst.popleft()
        if not appended and now[1] <= w:
            total += now[0]
            break
        
        else:
            new_lst.append(now)
    
    lst = new_lst + lst

print(total)