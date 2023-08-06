#if 문의 중첩
#만 나이 구하기

print("="*50)

now_year = int(input("현재년은? "))
now_month = int(input("현재달은? "))
now_day = int(input("현재일은?"))

birth_year = int(input("당신이 태어난 해는? "))
birth_month = int(input("당신이 태어난 달은? "))
birth_day = int(input("당신이 태어난 날은? "))

if birth_year > now_year :
    result = "수치를 잘못 입력하셨습니다.람쥐"
if birth_month < now_month:
    age = now_year - birth_year
elif birth_month == now_month:
    if birth_day < now_day:
        age = now_year - birth_year
    else:
        age = now_year - birth_year
else:
    age = now_year - birth_year - 1

print("="*50)
print("오늘 날짜 : %d년 %d월 %d일"%(now_year, now_month, now_day))
print("생년월일 : %d년 %d월 %d일"%(birth_year, birth_month, birth_day))
print("-"*50)
print("만 나이 : %d세"%age)
print("="*50)