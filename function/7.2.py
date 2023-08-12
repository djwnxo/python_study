#7.2 매개변수

#앞에서 배운 함수 정의의 형식은 'def 함수명()' 이다. 경우에 따라서는 함수 정의 시에 다음과 같은 매개변수(Parameter)가 사용된다

#7.2.1 매개변수란
#매개변수는 호출 함수에서 전달하고자 하는 값이나 변수를 전달받기 위해 함수 정의에서 사용되는 변수를 말한다.
'''
def say_hello(name):
    print("%s님 안녕하세요!"%name)

say_hello("정종혁")
say_hello("ㅋ")

#7.2.2 매개변수와 인수

def print_name(first_name, last_name):
    name = first_name + last_name
    print("이름 : ",name)

print_name("정","종혁")
'''
#7.2.3 매개변수의 유효 범위
#정의 함수에서 사용되는 매개 변수는 정의된 함수 내에서만 유효하다.
'''
def even_odd(n):
    if n % 2 == 0:
        print("%d은(는) 짝수이다."%n)
    else:
        print("%d은(는) 홀수이다."%n)

x = int(input("양의 정수를 입력하세요 : "))
even_odd(x)

#7.2.4 매개변수 *args
#일반적인 함수 정의에서는 매개변수의 개수가 고정된다. 그러나 하나의 함수에서 매개변수의 개수를 고정하지 않고 호출 함수에서 전달하는 인수의 개수에 따라 매개변수를 가변적으로 하고 싶은 경우에 사용하는 것이 매개변수 *args이다.

def average(*args): #args는 튜플 데이터 형
    num_args = len(args)
    sum = 0
    for i in range(num_args):
        sum = sum + args[i]

    avg = sum/num_args
    print("%d과목 평균 : %.1f"%(num_args, avg))

average(85,96,87)
average(77,93,85,97,72)

#7.2.5 매개변수에 리스트 전달하기

def func(food): #food는 fruits가 저장된 메모리 주소를 전달받음
    for x in food:
        print(x)

fruits =  ["사과","오렌지","바나나"]
'''
func(fruits)

def func(food): 
    food.append("딸기") #요소추가
    food.append("수박") #요소추가

fruits =  ["사과","오렌지","바나나"]

print(fruits) #3개 요소 출력됨
func(fruits)
print(fruits) #5개 요소 출력됨