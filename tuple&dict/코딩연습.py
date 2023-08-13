#C7-1 함수와 매개변수로 두 수의 합을 구하라!
'''
def add(a,b):
    c = a + b
    print("%d + %d = %d"%(a,b,c))

add(12,15)
add(245,300)
add(-38,-12)
'''
#C7-2 함수와 매개변수로 정수 합계를 구하라!
'''
def sum_int(start,end):
    total = 0
    for i in range(start,end+1):
        total = total + i
    print("%d ~ %d 정수 합계 : %d"%(start,end,total))

sum_int(20,50)
sum_int(600,800)
'''
#C7-3 매개변수 *args를 활용하는 프로그램을 작성하라!
'''
def member_join(*args):
    result = ""
    for arg in args:
        result = result + arg + " "

    print("가입 회원 :",result)

member_join("김정연","안서영")
member_join("황선형","김철영","이창연")
member_join("정수진","김보람","정수연","함소영")
'''
#C7-4 함수에서 리스트를 활용하는 프로그램을 작성하라!
'''
def multiply(num,x):
    i = 0
    while i < len(num):
        num[i] = num[i] * x

        i = i + 1

numbers = [10,20,30,40,50]

multiply(numbers, 10)
print(numbers)

multiply(numbers,10)
print(numbers)
'''
#C7-5 함수로 삼각형의 면적을 계산하라!
'''
def tri_area(w,h):
    result = w*h*0.5
    return result

width = int(input("너비를 입력하세요: "))
height = int(input("높이를 입력하세요: "))

print("- 삼각형의 너비 :",width)
print("- 삼각형의 높이 :",height)
print("- 삼각형의 면적 :",tri_area(width,height))
'''
#C7-6 함수로 배수의 합계를 구하라!
'''
def sum_besu(n):
    sum = 0
    for i in range(1, 101):
        if i%n == 0:
            sum = sum + i

    return sum

besu = int(input("구하고자 하는 배수를 입력하세요: "))

total = sum_besu(besu)

print("1~100 사이 %d의 배수의 합계 : %d"%(besu, total))
'''
#C7-7 함수로 문장에 포함된 공백을 카운트하라!
'''
def count_space(a):
    count = 0

    for x in a:
        if x ==" ":
            count = count + 1

    return count

sentence = "Python is easy and powerful"

print(sentence)
num_space = count_space(sentence)
print("- 공백의 개수 :", num_space)
'''
#C7-8 함수로 딕셔너리에서 게임 아이템을 가져오라!

def get_item(userid):
    game_items = {"kim":"총","lee":"대포","choi":"전투기","hwang":"병사"}

    for key in game_items:
        if userid == key:
            item = game_items[key]

    return item

user1 = "kim"
user2 = "hwang"

print("%s의 게임 아이템 : %s"%(user1, get_item(user1)))
print("%s의 게임 아이템 : %s"%(user2, get_item(user2)))