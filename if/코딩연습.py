#C3-1 특정 범위에 있는 수인지 판정하라!
'''
start = int(input("시작 수는?\n"))
end = int(input("끝 수는?\n"))
num = int(input("정수를 입력하세요 : "))

result = "%d은(는) %d~%d 사이에 있다." %(num, start, end)

if num > start and num < end:
    result = "%d은(는) %d~%d 사이에 있다."%(num, start, end)

print(result)
'''
#C3-2 월을 입력받아 계절을 판별하라!
'''
month = input("월을 숫자로 입력하세요 : ")

if month == "3" or month =="4" or month =="5":
    print("%s월은 봄입니다."%month)
if month == "6" or month =="7" or month =="8":
    print("%s월은 여름입니다."%month)
if month == "9" or month =="10" or month =="11":
    print("%s월은 가을입니다."%month)
if month == "12" or month =="1" or month =="2":
    print("%s월은 겨울입니다."%month)
'''
#C3-3 주민번호로 남/여를 판정하라!
'''
a = input("주민번호 뒷자리 첫 번째 숫자를 입력해 주세요 : ")

if a == "1" or a == "3":
    print("남성입니다!")
if a == "2" or a == "4":
    print("여성입니다!")
'''
#C3-5 다이어트 필요성을 판정하라!
'''
height = int(input("키는?"))
weight = int(input("몸무게는?"))

s = (height - 100) * 0.9

print("="*50)
print("키 :",height)
print("몸무게 :",weight)

if weight > s:
    print("건강을 위해 다이어트가 필요합니다!")
else:
    print("표준 또는 마른 체형입니다!")
'''
#C3-6 아르바이트 급여를 계산하라!
'''
print("아르바이트 급여 계산 프로그램")
print("# 시급")
print("- 주간 근무 : 9500원")
print("- 야간 근무 : 주간 시급 * 1.5")
print()

hour_pay = 9500

a = int(input("1(주간 근무) 또는 2(야간 근무)를 입력해주세요 : "))
work_time = int(input("근무 시간을 입력해주세요 : "))

if a == 1:
    day_night = "주간"
    pay = hour_pay * work_time
else:
    day_night = "야간"
    pay = hour_pay * work_time * 1.5

print("%d시간 동안 일한 %s 급여는 %d원 입니다."%(work_time, day_night, pay))
'''
#C3-7 할인율에 따라 지불 금액을 계산하라!
'''
spend = int(input("구매 금액은? "))

if spend >= 10000 and spend < 50000:
    rate = 5.0
elif spend >= 50000 and spend < 300000:
    rate = 7.5
elif spend >= 300000:
    rate = 10.0
else:
    rate = 0

discount = spend * rate / 100
pay = spend - discount

print("구매금액 : %.0f"%spend)
print("할인율 : %.1f"%rate)
print("할인 금액 :: %.0f"%discount)
print("지불금액 : %.0f"%pay)
'''
#C3-8 서비스 만족도에 따라 팁을 계산하라!
'''
print("서비스 만족도 : ")
print(" 1: 매우만족")
print(" 2: 만족")
print(" 3: 불만족")
a = input("서비스 만족도는?(1/2/3)")
price = int(input("음식 값은?"))

if a == "3":
    tip = int(price * 0.2)
    service = "매우 만족"
elif a == "2":
    tip = int(price*0.1)
    service = "만족"
else:
    tip = 0
    service = "불만족"
print()
print("서비스 만족도 : %s, 팁 : %d원"%(service,tip))
'''
#C3-9 세 정수 중 가장 큰 수를 찾아라!!!!!!!!!!!!!
'''
num1 = int(input("첫 번째 정수는? "))
num2 = int(input("두 번째 정수는? "))
num3 = int(input("세 번째 정수는? "))

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print("%d, %d, %d 중에서 가장 큰 수는 %d 입니다."%(num1, num2, num3, largest))
'''
#C3-10 웹 사이트 콘텐츠 이용 가능 여불를 판단하라이더!
'''
userid = input("아이디는? ")

if userid == "admin":
    print("콘텐츠 이용이 가능합니다!")
else:
    level = int(input("회원 등급은?(1~9) "))
    
    if level >= 1 and level <= 3:
        print("콘텐츠 이용이 가능합니다!")
    else:
        print("콘텐츠를 이용하실 수 없습니다!")
'''
#C3-11 온도에 따라 물의 상태를 판별의 커비!
unit = input("단위를 입력해 주세요(1 : 섭씨, 2 : 화씨) : ")
temp = int(input("온도를 입력해 주세요 : "))

if unit == "2":
    temp = (temp-32) * 5 / 9

if temp <= 0:
    state = "고체"
elif temp < 100:
    state = "액체"
else:
    state = "기체"

print("물의 섭씨 온도 : %.1f도, 상태 : %s"%(temp, state))