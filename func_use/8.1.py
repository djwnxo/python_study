#파이썬의 내장 함수
'''
파이썬의 내장 함수는 파이썬에 기본적으로 내장되어 있는 함수이다.
파이썬에서 자주 사용 되는 내장 함수를 표로 정리하면 다음과 같다.
print()     데이터나 변수를 화면에 출력함
input()     키보드로 데이터 입력을 받음
type()      변수의 데이터 형을 구함
int()       실수나 문자열을 정수로 변환함
float()     정수나 문자열을 실수로 변환함
str()       정수나 실수를 문자열로 변환함
sum()       리스트나 튜플 요소들의 합을 구함
len()       문자열, 리스트, 튜플, 딕셔너리의 길이를 구함
range()     10진 정수를 2진수로 변환함
list()      새로운 리스트를 생성함
tuple()     새로운 튜플을 생성함
dict()      새로운 딕셔너리를 생성함
ord()       문자의 아스키 코드 값을 구함
bin()       10진 정수를 2진수로 변환함
hex()       10진 정수를 16진수로 변환함
round()     반올림 값을 구함
max()       리스트나 튜플의 최댓값을 구함
min()       리스트나 튜플의 최솟값을 구함
'''

#8.1.1 아스키 코드 구하기 - ord()
#2장에서 키보드로 입력 받는 모든 데이터(숫자,문자,특수문자 등)는 문자열로 처리된다고 설명하였다. 이 문자열을 저장하는 데 사용되는 컴퓨터 코드(0과 1의 조합)가 아스키 코드이다. 아스키는 영문 알파벳, 숫자, 특수문자 등에 사용되는 대표적인 문자 인코딩 방식이다.

x = "1" #x는 문자열
print("아스키코드 :", ord(x)) #ord(x)는 x의 아스키 코드 값

#8.1.2 16진수/2진수 변환하기 - hex(), bin()

x = "a"
code = ord(x)

print("아스키 코드(10진수) : %d"%code)
print("아스키 코드(16진수) : %s"%hex(code)) #hex() : 16진수
print("아스키 코드(2진수) : %s"%bin(code)) #bin() : 2진수

#8.1.3 반올림 값 구하기 - round()

x = round(7.65676) #소수점 첫째 자리 반올림
print(x)

y = round(7.65676, 2) #소수점 셋째 자리 반올림
print(y)

#8.1.4 최댓값/최솟값 구하기 - max(), min()
# max()함수는 주어진 수들 중 또는 리스트(또는 튜플) 의 요소들 중에서 최댓값을 구할 때 사용된다.

x = max(3,5,2) #3,5,2 중 최댓값
print(x)

data = [3,7,2,12,423]
y = max(data) #리스트 요소 중 최댓값
print(y)