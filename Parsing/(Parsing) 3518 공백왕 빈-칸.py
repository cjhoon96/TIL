'''
https://www.acmicpc.net/problem/3518
공백왕 빈-칸 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	178	48	39	32.500%
문제
보기도 좋은 떡이 먹기도 좋다고.. 예쁘게 정리되어 있는 글이 난잡하게 써져있는 글보다 읽기 좋을 것이다. 이번 문제는 글을 단어별로 끊어서, 예쁘게 출력하는 것이다.

여기서 예쁜 글이란, 글에 있는 모든 줄에 대해서 i번째 단어들의 시작 위치가 똑같다면 그 글은 예쁜 글이라고 본다. 예를 들어서

a bc z
de f zz
이런 글이 있다고 치자. 두 번째 단어인 bc 와 f의 시작위치가 다르기 때문에 이 글은 예쁜 글이 아니다. 이제 띄어쓰기를 적절히 넣어서 시작위치를 같게 만들어보면

a bc z
de f zz
각 줄의 첫 번째 단어인 a와 de의 시작위치가 똑같고, 두 번째 단어인 bc와 f의 시작문자의 위치가 똑같다. 위 글은 예쁜 글이 된다.

...시작위치가 다르게 보인다고? 그건 글씨체 문제이니, 위 문장을 복사해 메모장에서 보자

입력으로 글의 내용이 주어졌을 때, 띄어쓰기를 적절히 넣고 빼서 이 글을 예쁘게 만들어주자. 글에 들어있는 문자는 띄어쓰기와 줄바꿈, 그리고 ASCII 값이 33~126 사이에 있는 문자들만 주어진다

입력
문서의 내용이 여러불에 걸쳐 들어온다. 각 단어들은 띄어쓰기로 구분되며, 단어의 길이는 최대 80자이다. 각 줄에는 (공백을 포함해서) 최대 180자의 문자가 들어오며, 입력되는 문장은 최대 1000줄까지 들어올 수 있다.

출력
입력으로 주어진 문서를 예쁘게 출력한 결과물을 출력한다. 정답이 여러개인 경우 사전순으로 가장 앞서는 것을 출력한다.

단어를 구분할 때 쓰이는 공백 이외에 불필요한 공백은 출력하지 않도록 주의하자.

예제 입력 1 
  start:  integer;    // begins here
stop: integer; //  ends here  
 s:  string;   
c:   char; // temp 
예제 출력 1 
start: integer; // begins here
stop:  integer; // ends   here
s:     string;
c:     char;    // temp
출처
ICPC > Regionals > Northern Eurasia > Northern Eurasia Finals > NEERC 2010 A번

문제를 번역한 사람: pichulia
'''
import sys
input = sys.stdin.readline

str_lst = []

max_words = 0

while True:
    string = input().rstrip()
    if string == '':
        break

    string = list(string.split())
    words = len(string)
    str_lst.append(string)

    if words > max_words:
        max_words = words

lnth = [0] * max_words

for string in str_lst:
    for i in range(len(string)):
        l = len(string[i])
        maxi = lnth[i]
        if l > maxi:
            lnth[i] = l

for string in str_lst:
    sen = ''
    for i in range(len(string)):
        sen += string[i] + ' '*(lnth[i] - len(string[i])) + ' '
    print(sen.rstrip())
