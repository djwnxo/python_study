#C2-1 연월일 사이에 '.'을 삽입하라!
a = '''
year = int(input("년은?"))
month = int(input("월은?"))
day = int(input("일은?"))
print(year,month,day,sep=".")

#C2-2 사각형의 둘레와 면적을 계산하라!
width = int(input("사각형의 밑변은?\n"))
height = int(input("사각형의 높이는?\n"))
round = (width + height) * 2
area = height * width
print("사각형의 밑변 : %dcm"%width)
print("사각형의 높이 : %dcm"%height)
print("사각형의 둘레 : %dcm"%round)
print("사각형이 넓이 : %dcm2"%area)
'''
'''
#C2-3 원의 둘레와 면적을 구하라!
r = float(input("반지름을 입력하세요옹\n"))

import math
length = 2*math.pi*r
area = r*r*math.pi
print("원의 둘레 : %.2f"%length)
print("원의 넓이 : %.2f"%area)
'''
#C2-4 인치를 센티미터로 환산하라!
'''
inch = float(input("인치는?\n"))
cm = inch * 2.54
print("%.1f inch => %.1f cm"%(inch, cm))
'''
#C2-5 온라인 서점의 책 결제 금액을 계산하라!
price = int(input("책 값은?"))
sale = int(input("할인률은?"))
kyochon = int(input("배송료는?"))
sum = price -(price*(sale/100)) +kyochon
print("책 값 : %d원"%price)
print("할인율 : %d"%sale)
print("배송료 : %d원"%kyochon)
print("결제 금액 : %d원"%sum)