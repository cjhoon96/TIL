'''
https://www.acmicpc.net/problem/10773
제로 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	25988	17340	14528	67.834%
문제
나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

출력
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.

예제 입력 1 
4
3
0
4
0
예제 출력 1 
0
예제 입력 2 
10
1
3
5
4
0
0
7
0
0
6
예제 출력 2 
7
힌트
예제 2의 경우를 시뮬레이션 해보면,

[1]
[1,3]
[1,3,5]
[1,3,5,4]
[1,3,5] (0을 불렀기 때문에 최근의 수를 지운다)
[1,3] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,3,7]
[1,3] (0을 불렀기 때문에 최근의 수를 지운다)
[1] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,6]
합은 7이다.

출처
Olympiad > Canadian Computing Competition & Olympiad > 2015 > CCC 2015 Senior Division 1번

문제의 오타를 찾은 사람: busyhuman
문제를 번역한 사람: koosaga

'''

import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    n = input().rstrip()
    
    n = int(n)

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))