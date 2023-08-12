#C3-1 특정 범위에 있는 수인지 판정하라!
start = int(input("시작 수는?\n"))
end = int(input("끝 수는?\n"))
num = int(input("정수를 입력하세요 : "))

result = "%d은(는) %d~%d 사이에 있다." %(num, start, end)

if num > start and num < end:
    result = "%d은(는) %d~%d 사이에 있다."%(num, start, end)

print(result)