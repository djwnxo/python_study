word = input("영어 문장을 입력하세요 : ")

for x in word:
    print(x)

phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요 : ")

for y in phone:
    if y!= "-":
        print("%s"%y , end = "")

#for 루프에서 변수 y는 입력된 전화번호의 각 문자 값을 가진다.
#if 문의 조건식 y != "-"는 변수 y의 값이 '-'이 아닐 대에만 실행 결과에서와 같이 해당 문자가 출력된다