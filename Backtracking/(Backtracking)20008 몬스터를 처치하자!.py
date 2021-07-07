'''
https://www.acmicpc.net/problem/20008
몬스터를 처치하자! 출처
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	87	42	32	47.059%
문제
가장 빠른 시간 내에 몬스터를 처치하려고 한다. 사용할 수 있는 스킬은 N개 있으며, 각 스킬은 사용하는 데 1초가 들고, 사용을 시작한 지 1초 후 몬스터에게 일정 대미지를 입힌다. 여러 개의 스킬을 동시에 사용할 수는 없다.

각 스킬에는 저마다의 대기 시간과 대미지가 있다. 대기 시간은 스킬을 사용하기 시작한 순간부터 차기 시작한다.

예를 들어, 현재 시각이 t = 0이고, 대기 시간이 10초이고 대미지가 10인 스킬을 체력이 100인 몬스터에게 사용했다고 하자. 그러면 t = 1일 때 몬스터의 체력이 90으로 줄어들고, 같은 스킬은 t = 10일 때부터 다시 사용할 수 있다.

입력
첫 번째 줄에는 스킬 개수 N(1 ≤ N ≤ 5)과 몬스터의 체력(HP)을 나타내는 정수(1 ≤ HP ≤ 100000)가 주어진다.

두 번째 줄부터는 줄마다 스킬의 대기 시간을 초 단위로 나타내는 정수 C(1 ≤ C ≤ 10)와 스킬의 대미지를 나타내는 정수 D(HP/10 ≤ D ≤ HP)가 공백을 두고 주어진다. 모든 스킬의 대기 시간은 다르며, 모든 D의 합은 HP보다 작다.

출력
몬스터를 처치하는 데 걸리는 최소 시간을 출력한다.

예제 입력 1 
2 70000
3 10000
5 10001

예제 출력 1 
12
 
| 시간 | 0초 | 1초 | 2초 | 3초 | 4초 | 5초 | 6초 | 7초 | 8초 | 9초 | 10초 | 11초 | 12초 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mob hp | 70000 | 59999 | 49999 | 49999 | 49999 | 39999 | 29998 | 29998 | 19998 | 19998 | 19998 | 9997 | -3 |
| 1번스킬 남은 대기시간 | 0 | 0->3 | 2 | 1 | 0->3 | 2 | 1 | 0->3 | 2 | 1 | 0 | 0->3 | 2 |
| 2번 스킬 남은 대기시간 | 0->5	4 | 3 | 2 | 1 | 0->5 | 4 | 3 | 2 | 1 | 0->5 | 0 | 0 |

예제 입력 2 
2 70000
3 10001
5 10000

예제 출력 2 
12

| 시간 | 0초 | 1초 | 2초 | 3초 | 4초 | 5초 | 6초 | 7초 | 8초 | 9초 | 10초 | 11초 | 12초 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mob hp | 70000 | 60000 | 49999 | 49999 | 49999 | 39998 | 29998 | 29998 | 19997 | 19997 | 19997 | 9996 | -4 |
| 1번 스킬 남은 대기시간 | 0 | 0->3 | 2 | 1 | 0->3 | 2 | 1 | 0->3 | 2 | 1 | 0->3 | 0 | 1 |
| 2번 스킬 남은 대기시간 | 0->5 | 4 | 3 | 2 | 1 | 0->5 | 4 | 3 | 2 | 1 | 0 | 0->5 | 4 |

예제 입력 3 
3 2831
7 1138
6 507
9 870

예제 출력 3 
7

출처
University > 충남대학교 > 제4회 생각하는 프로그래밍 대회 H번

문제를 다시 작성한 사람: jh05013
문제를 만든 사람: potion

2021. 03. 09.(목) 기준 파이썬 1위!!!
| 등수 | 제출 번호 | 시도 | 아이디 | 메모리 | 시간 | 언어 | 코드 길이 | 제출한 시간 |
|---|---|---|---|---|---|---|---|---|
| 1 | 30774870 | 1 | cjhoon96 | 29200 | 168 | Python 3 / 수정 | 945 | 1분 전 |
| 2 | 23150128 | 1 | happiness96 | 31824 | 492 | Python 3 | 1743 | 8달 전 |
| 3 | 22895381 | 1 | scvhero | 109156 | 2636 | Python 3 | 302 | 9달 전 |

'''

N, HP = map(int,input().split())

skill = []
cooling = [0 for _ in range(N)]
for _ in range(N):
    skill.append(tuple(map(int,input().split())))

min_time = 1e9

def bfs(skill, cooling, HP, time):
    global min_time
    time += 1
    if min_time <= time:
        return
    check = []
    for i in range(N):
        if not cooling[i]:
            check.append(i)
        else:
            cooling[i] -= 1
            if not cooling[i]:
                check.append(i)
    if  len(check) == 0:
        bfs(skill, cooling, HP, time)

    else:
        for idx in check:
            next_cool = cooling.copy()
            now_skill = skill[idx]
            next_HP = HP - now_skill[1]

            if next_HP <= 0:
                if min_time > time:
                    min_time = time
                print('last deal: ', time, next_cool, next_HP)
                return

            next_cool[idx] = skill[idx][0]
            bfs(skill, next_cool, next_HP, time)
            print(time, next_cool, next_HP, check)

bfs(skill, cooling, HP, 0)
print(min_time)

