'''
https://www.acmicpc.net/problem/11507
카드셋트 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	32 MB	857	504	447	63.494%
문제
최근에 진솔이는 로봇 공학을 하기 시작했다. 그래서 포커 카드가 완전한 세트인지 확인하는 로봇을 만들기로 결심했다.

그는 프로그램을 작성하는 일을 분담했다. 그 프로그램은 카드의 모양(스페이드(♠), 하트(♡), 다이아몬드(♢), 클럽(♣))을 인식하는 것이다. 문제를 간단하게 하기 위해서 모든 카드는 하나의 모양과 하나의 숫자를 가진다고 가정한다.

여기서 그 모양은 실제 그림 대신 문자로 대체한다. P,K,H,T에 해당한다. 그리고 숫자는 1~13에 해당하는 정수이다. 로봇은 각각의 카드를 TXY의 형태로 '카드 이름'을 정하는데 T는 모양에 해당하고 XY는 숫자에 해당한다. 만약 만약 숫자가 1자리 숫자이면 X=0에 해당한다. ex) 01.

만약에 모양이 P이고 숫자가 9이면 P09이다.

완벽한 카드 한 세트는 52개로 이루어져 있다. (4 (모양)x 13(숫자))

로봇은 모든 카드의 '카드이름'을 읽고 문자열 S로 결합한다.

이제 진솔이가 프로그래밍 하는 것을 도와주자.  문자열을 읽어 얼마나 많은 카드를 잃어버렸는지 세면 된다.

만약에 2개의 같은 카드가 존재한다면 GRESKA이라고 출력하면 된다.

입력
오직 1줄만 문자열 S(1 ≤ |S| ≤ 1000)가 들어온다. 이것은 현재 가지고 있는 카드 이름에 해당한다.

출력
만약 똑같은 카드가 존재한다면 GRESKA을 출력한다.

그렇지 않으면 4개의 정수를 공백 문자로 구분하여 출력한다. 각각 P, K, H, T에 해당한다.

예제 입력 1 
P01K02H03H04
예제 출력 1 
12 12 11 13
예제 입력 2 
H02H10P11H02
예제 출력 2 
GRESKA
예제 입력 3 
P10K10H10T01
예제 출력 3 
12 12 12 12
힌트
예제1 : 12 12 11 13은 잃어버린 P카드 :  12개, K : 12개, H : 11개, T : 13라는 뜻이다.

예제2 : 같은 카드(H02)가 존재하므로 GRESKA을 출력하였다.

출처
Contest > Croatian Open Competition in Informatics > COCI 2015/2016 > Contest #1 1번

문제를 번역한 사람: infoefficiency
'''

import sys
input = sys.stdin.readline

a = input().rstrip()
pats = 'PKHT'
card = {i : 13 for i in pats}

cnt = len(a) // 3

card_dic = {i : set() for i in pats}

GRESKA = False

for i in range(cnt):
    i *= 3
    pat = a[i]
    num = a[i + 1 : i + 3]
    if num in card_dic[pat]:
        GRESKA = True
        print('GRESKA')
        break

    card_dic[pat].add(num)
    card[pat] -= 1

if not GRESKA:
    for i in pats:
        print(card[i], end = ' ')