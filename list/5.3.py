'''
#5.3.1 리스트 요소 수정하기
flowers = ["목련", "벚꽃", "장미", "백일홍"]
print(flowers)

flowers[1] = "무궁화" #flowers 리스트의 두 번째 항목을 무궁화로 변경
print(flowers)

#5.3.2 리스트 요소 추가하기

arr = [5,3,12,9,2]
print(arr)

arr.append(10) #리스트 마지막에 10이라는 항목 추가
print(arr)


scores = []

while True:
    score = int(input("성적을 입력하세요(종료 : -1)."))

    if score == -1:
        break #입력된 score의 값이 -1이면 반복문 종료
    else : 
        scores.append(score) #입력된 score 값을 scores 리스트에 추가


    print(scores)
'''
#5.3.3 리스트 요소 삽입하기
'''
fruits = ["apple", "orange", "banana", "cherry"]
print(fruits)

fruits.insert(1, "melon") #두 번째 자리에 melon이라는 항목 추가
print(fruits)

fruits.insert(2,"strawberry") #세 번째 자리에 strawberry라는 항목 추가
print(fruits)

#5.3.4 리스트 요소 위치 찾기

number = [5,20,13,7,8,22,7,17]
print(number)

idx = number.index(7) #리스트에서 7이라는 항목의 순서 찾기
print(idx) #--> 3이 나옴
'''
#5.3.5 리스트 요소 삭제하기
'''
member = ["정종혁","16","서울시 광진구","yoongella@discord.com","010-1234-5678"]
print(member)
member.remove("16")
print(member)

data = [10,20,30,40,50,60,70,80]
print(data)

x = data.pop(2)
print(x)
print(data)

x = data.pop(3)
print(x)
print(data)
'''

data = [3,12,7,-3,-9]
print(data)

data.clear()
print(data)