'''
https://www.acmicpc.net/problem/1340
연도 진행바 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	524	199	162	40.299%
문제
문빙이는 새해를 좋아한다. 하지만, 이제 새해는 너무 많이 남았다. 그래도 문빙이는 새해를 기다릴 것이다.

어느 날 문빙이는 잠에서 깨면서 스스로에게 물었다. “잠깐, 새해가 얼마나 남은거지?”

이 문제에 답하기 위해서 문빙이는 간단한 어플리케이션을 만들기로 했다. 연도 진행바라는 것인데, 이번 해가 얼마나 지났는지를 보여주는 것이다.

오늘 날짜가 주어진다. 이번 해가 몇%지났는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 Month DD, YYYY HH:MM과 같이 주어진다. Month는 현재 월이고, YYYY는 현재 연도이다. 
숫자 네자리이다. DD, HH, MM은 모두 2자리 숫자이고, 현재 일, 시, 분이다.

Month는 January, February, March, April, May, June, July, August, September, October, November, December 중의 하나이고, 
연도는 1800보다 크거나 같고, 2600보다 작거나 같다. 항상 올바른 날짜와 시간만 입력으로 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

예제 입력 1 
May 10, 1981 00:31
예제 출력 1 
35.348363774733635
힌트
평년일 때, 각 달은 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이 있다. 윤년에는 2월이 29일이다. 
윤년은 그 해가 400으로 나누어 떨어지는 해 이거나, 4로 나누어 떨어지면서, 100으로 나누어 떨어지지 않는 해 일때이다. 
지역에 따른 서머타임은 고려하지 않는다.
'''

import sys
input = sys.stdin.readline

M, D, Y, T = input().rstrip().split()
month = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}
Y = int(Y)
D = int(D[:2])
M = month[M]
if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
    leap = True

else:
    leap = False

set_1 = set([1, 3, 5, 7, 8, 10, 12])
set_0 = set([4, 6, 9, 11])

for i in range(1, M):
    if i in set_0:
        D += 30
    
    elif i in set_1:
        D += 31
    
    elif leap:
        D += 29
    
    else:
        D += 28
D -= 1
h, m = map(int, T.split(':'))

m += h * 60
m += D * 24 * 60
m *= 100
if leap:
    total = 366 * 24 * 60

else:
    total = 365 * 24 * 60

print(m/total)