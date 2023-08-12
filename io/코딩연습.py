#C2-1 연월일 사이에 '.'을 삽입하라!
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
