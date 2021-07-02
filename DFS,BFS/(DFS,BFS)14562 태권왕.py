'''
https://www.acmicpc.net/problem/14562
태권왕 출처
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	373	186	157	51.645%
문제
태균이는 지금 태권도 겨루기 중이다. 지금은 상대에게 지고 있지만 지금부터 진심으로 경기하여 빠르게 역전을 노리려 한다.

태균이가 현재 할 수 있는 연속 발차기는 두가지가 있다.

A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
B는 1점을 얻는 연속 발차기이다.
현재 태균이의 점수 S와 상대의 점수 T가 주어질 때, S와 T가 같아지는 최소 연속 발차기 횟수를 구하는 프로그램을 만드시오.

입력
첫째 줄에 테스트 케이스의 수 C(1 ≤ C ≤ 100)이 주어진다. 둘째 줄부터 C줄에 걸쳐 테스트 케이스별로 현재 점수 S와 T가 공백을 사이에 두고 주어진다. (1 ≤ S < T ≤ 100)

출력
각 줄마다 S와 T가 같아지는 최소 연속 발차기 횟수를 출력한다.

예제 입력 1 
6
10 20
2 7
15 62
10 37
11 50
34 59
예제 출력 1 
3
3
4
4
5
25
'''
import sys
input=sys.stdin.readline
from collections import deque

def bfs(s,t):
    queue = deque()
    queue.append((s, t, 0))
    overlap = 0
    visit = set()

    while queue:
        s_score, t_score, node = queue.popleft()
        a_s, a_t, b_s = s_score * 2, t_score + 3, s_score + 1
        node += 1
        
        if a_s == a_t or b_s == t_score:
            print(node)
            return overlap

        if a_s < a_t:
            if (a_s, a_t, node) not in visit:
                visit.add((a_s, a_t, node))
            else:
                overlap += 1
            queue.append((a_s, a_t, node))

        if b_s < t_score:
            queue.append((b_s, t_score, node))



n = int(input())

for _ in range(n):
    s, t = map(int,input().split())
    
    print(bfs(s, t))
