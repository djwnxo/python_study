#영문 소문자 자음/모음 판별하기

char = input("영문 소문자 하나를 입력하세요 : ")

if char == "a" or char == "e" or char == "i" or char =="o" or char =="u":
    print("%s은(는) 모음이다. "%char)
else:
    print("%s은(는) 자음이다."% char)