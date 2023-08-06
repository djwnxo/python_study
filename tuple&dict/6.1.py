#6.1 튜플이란
'''
파이썬에서 튜플은 리스트와 많은 부분이 유사하고 사용법도 거의 같다. 튜플과 리스트의 차이점은 다음 두 가지로 볼 수 있다.
튜플에서는 대괄호 대신에 소괄호를 사용한다
튜플에서는 리스트와 달리 요소의 수정과 추가가 불가능하다
'''
'''
#6.1.1 튜플 생성하기
animals = ("토끼","거북이","사자","여우") #튜플 animals 생성
print(animals)

numbers = tuple(range(10)) # tuple()을 사용한 튜플 생성
print(numbers)
'''
#6.1.2 튜플 요소 추출하기
n = tuple(range(10,21)) #10부터 20까지의 수를 n이라는 튜플로 만듦
print(n)

print("n[0] =",n[0]) # 첫 번째 숫자 출력
print("n[2:5] =", n[2:5]) # 세 번째에서 여섯 번째 숫자까지 출력
print("n[2:]=",n[2:]) #세 번째 숫자에서 끝까지 출력
print("n[:5]",n[:5]) # 처음부터 네 번째 숫자까지 출력
print("n[-2] =",n[-2])
print("n[::-1] =", n[::-1]) #n[::-1]을 이용하면 튜플 n의 순서가 반대로 된 튜플을 얻을 수 있다.

tup1 = (10,20,30,40,50)

for i in range(len(tup1)): #tup1의 길이만큼 반복
    print(tup1[i])

#6.1.4 튜플 병합하기

tup1 = (10,20,30)
tup2 = (40,50,60)
tup3 =tup1 + tup2
print(tup3)

#6.1.5 튜플에 관리자 정보 저장하기

admin_info = ("admin", "12345", "webmaster@naver.com")

print("관리자 정보")
print("아이디 : "+ admin_info[0])
print("비밀번호 : "+ admin_info[1])
print("이메일 : " + admin_info[2])