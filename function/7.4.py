#7.4 지역 변수와 전역 변수
#7.4.1 지역변수
#지역 변수는 정의된 함수 내에서 사용되는 변수를 말한다
'''
def func():
    x = 100 #지역변수 x
    print(x)

func()
# print(x) #x가 정의되지 않음

#7.4.2 전역 변수
#전역 변수는 메인 루틴의 제일 앞에 정의된 변수를 말한다.

def func():
    print(x) # x-->전역 변수

x = 100 #전역 변수 x
func()
print(x)
'''
#7.4.3 키워드 global
#func() 내에서 전역 변수를 정의하고 싶은 경우에는 다음의 예에서와 같이 키워드 global을 사용하면 된다.

def func():
    global x #여기서 x는 메인 루틴의 전역 변수임
    x = 200 # x --> 전역 변수
    print(x)

x = 100
print(x)
func()
print(x)

def cir_area():
    global r
    result = r * r * 3.14
    return result

def cir_length():
    global r
    result = 2 * 3.14 * r
    return(result)

r = float(input("반지름을 입력하세요 : "))
area = cir_area()
length = cir_length()
print("원의 면적 : %.1f, 원주의 길이 :%.1f"%(area, length))

#매개변수를 이용한 원의 면적과 둘레 구하기

import math

def cir_area(r):
    result = r*r*math.pi
    return result

def cir_length(r):
    result = 2 * math.pi *r
    return result

r = float(input("반지름을 입력하세요 : "))
area = cir_area(r)
length = cir_length(r)
print("원의 면적 : %.1f, 원주의 길이 :%.1f"%(area, length))
#2313123123123123122312313