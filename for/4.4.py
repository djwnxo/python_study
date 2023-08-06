#4.4.1 while 문의 기본 구조
'''
sum = 0
i = 1 #i를 1로 초기화

while i <= 10:
    sum = sum + i #누적합계 구함
    print("i의 값 : %2d = > 합계 : %d"%(i, sum))

    i = i + 1
'''
#4.4.2 while문으로 5의 배수 합계 구하기
'''
sum = 0
i = 500

while i <= 600:
    if i % 5 == 0:
        sum = sum + i
    
    i = i + 1

print("5의 배수 합계 : %d"%sum)
'''
#4.4.3 while문으로 영어 모음 개수 구하기

s = "Python is widely used by a number of big companies"

i = 0
count = 0

print("모음 : ",end="")

while i <= len(s) - 1:
    if (s[i] == "a" or s[i] == "A" or s[i] == "e" or s[i] == "E" or s[i] == "i" or s[i] == "I" or s[i] == "o" or s[i] == "O" or s[i] == "u" or s[i] == "U"):
        count = count + 1
        print(s[i], end = " ")

    i = i + 1

print()
print("모음 개수 : %d"%count)