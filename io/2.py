'''
a = 333 / 111
print("%.1f"%a)
print(a)
'''

#2.2.2
'''
print(-26.35 + 8.7 * (-21.0))
'''
'''
#문자열
a = "abc"
print(type(a))
#정수형
b = 123
print(type(b))
#실수형
c = 123.45
print(type(c))
#%는 나눗셈의 나머지 출력
print(10%3)
#//는 소숫점자리 삭제
print(10//3)
#문자열의 추출
s = "안녕하세요. 반갑습니다."
print(s[0])
print(s[3:10])
#문자열 연결 연산자
name = "정종혁"
hello = "ㅎㅇ"
print(name + "님" + hello)
#문자열 반복 연산자
x = "정지티비 구독과 좋아요 " * 3
print(x)
#문자열 길이 구하기
y = "대머리는 머리 끝까지 화가 나지만, 일반인은 머리카락 끝까지 화가 난다."
z = len(y)
print("문자열의 길이 : " + str(z))
#문자열 포맷팅 (%s는 문자열 대치, %d 정수형 변수 대치, %f 실수형 숫자 대치)
jhr = "동시에 네 명"
zx = "정하람은 %s을 좋아합니다."%jhr
print(zx)
jhrd = 4
zy = "정하람이 좋아하는 사람의 수 : %d"%jhrd
print(zy)
kor = 100
eng = 100
math = 100
sum = kor + eng + math
avg = sum/3
print("합계 : %d, 평균 : %.2f"%(sum, avg))
#키보드 입력
person = input("이름을 입력하세요 : ")
print(person + "님 안녕하세요.")

a = input("첫 번째 정수를 입력하세요 : ")
b = input("두 번째 정수를 입력하세요 : ")
c = a + b
print(c)
# --> 25
c = int(a) + int(b)
print(c)
# --> 7
#int()는 실수나 문자열을 정수형 숫자로 변환한다.
#float()은 정수나 문자열을 실수형 숫자로 변환하는 데 사용된다.
#str()은 정수형이나 실수형 숫자를 문자열로 변환하는 데 사용된다.
'''
'''
#콤마로 구분하여 출력하기
name2 = "정종혁"
print(name2)
a = 10
b= 20
print(a,b,a - b,100)
#2.5.2 키워드 sep으로 출력하기
year = 2023
month = 8
day = 5
print(year,month,day,sep="/")
hp1 = '010'
hp2 = '1234'
hp3 = '5678'
print(hp1,hp2,hp3,sep="-")
price =1000
print(price, "원")
print(price,"원",sep="")
#2.5.3 문자열 포맷 코드로 출력하기
x = 25
y = 3.3
animal = "고양이"
print("%d %f %s"%(x,y,animal))
print("%.1f"%y)
#포맷코드 %.1f 실수에서 소수점 첫재 자리(둘째 자리에서 반올림)까지 구함
#이스케이프 코드 출력
'''
'''
\n 줄바꿈
\t 탭
\\ 역슬래쉬 출력
\' 단 따옴표(') 출력
\" 쌍 따옴표(") 출력
'''
'''
#탄생년을 입력받아 나이 계산하기
name = input("당신의 이름은?")
birth = int(input("당신이 태어난 해는?"))

age = 2023 - birth + 1
print("%s님의 나이는 %d세 입니다."%(name, age))

#비교 연산자와 논리 연산자

비교연산자 : >, <, ==, !=, <=, >=
논리연산자 : and, or, not
'''
#3.3.3 영어 단어 퀴즈 만들기
ans1 = "땡! 틀림"
if ans1 == "lion":
