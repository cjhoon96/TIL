# **BAEKJOON**

# 재귀함수
* ## 재귀함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미
* ## 단순한 형태의 재귀함수 예제
    * ## '재귀함수를 호출합니다.'라는 문자열을 무한히 출력합니다.
    * ## 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력됩니다.

```python
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()
recursive_function()
```

* ## 재귀함수를 문제 풀이에서 사용할때 종료조건을 반드시 명시!! (무한 호출 방지)
* ## 재귀함수를 활용하면 스택 구조처럼 스택 프레임에 입력값을 저장 하였다가 마지막에 호출된 함수부터 처음에 호출된 함수까지 실행

* ### 예시) 팩토리얼
```python
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(int(input())))
```
100
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


* ### 예시) 최대공약수 계산 (유클리드 호제법) 예제

    * ### 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.
    * ### 유클리드 호제법
        * ### 두 자연수 a,b에 대해 (a>b) a를 b로 나눈 나머지를 r이라고 하자
        * ### 이때 a와 b의 최대공약수는 b와 r의 최대 공약수와 같다.

### 재귀 함수로 구현
```python
def gcd(a,b):
    r = a%b
    if r == 0:
        return b
    else:
        return gcd(b,r)
    
a,b=map(int,input().split())

print(gcd(a,b))
```
 192 162
6

* ## 모든 재귀함수는 반복문으로 구현 가능
* ## 유리한 경우도 있고 그렇지 않은 경우도 있음
* ## 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
    * ## 그래서 스택을 사용해야 할때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많음
    
