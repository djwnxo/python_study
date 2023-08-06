#5.4.1 리스트 병합하기
'''
person1 = ["jung",16,"jksimmons@twitch.com"]
person2 = ["jong",16,"jks1mmons@insta.com"]

person = person1 + person2 #두 리스트의 항목을 person이라는 한 리스트에 넣음
print(person)

#5.4.2 리스트 합계 구하기

scores = [80,90,85,95,100]

sm = sum(scores) #scores 리스트 내에 있는 요소들의 합계를 구하는 데 사용된다
avg = sm/len(scores) # 합계 sm을 리스트의 길이로 나누면 평균 avg값이 나온다

print("합계 : ",sm)
print("평균 : ",avg)

#5.4.3 리스트 순서 반대로 하기

data = [10,20,30,40,50]
print(data)

data.reverse()
print(data)

#5.4.4 리스트 복사하기

fruits = ["apple", "banana", "orange"]
print(fruits)

x = fruits.copy()
print(x)

#5.4.5
data = [12,8,15,32,-3,-20,15,34,6]
print(data)

data.sort() #data.sort()는 리스트 data내의 요소들을 오름차순으로 정렬한다
print(data)

data.sort(reverse=True) #reverse=True는 요소들을 내림차순으로 정렬한다
print(data)
'''
#5.5 문자열과 리스트
#5.5.1  문자열 찾기
'''
string1 = "Python is fun!"
print(string1)

x = string1.find("fun")
print(x) #실행결과 10은 fun이 제일 먼저 나오는 위치, 즉 인덱스 번호 값을 가진다.


#5.5.2 문자열 치환하기

string1 = "망고는 맛있디. 나는 망고를 제일 좋아한다."
print(string1)

x = string1.replace("망고","망고빙수")
print(x)
'''
#5.5.3 문자열 쪼개기
'''
hello = "have a nice day"
print(hello)

list1 = hello.split(" ") #공백을 기준으로 나눔
print(list1)
print(type(list1))

for i in range(0,len(list1)): #0부터 list1의 길이 - 1 만큼 반복 = 총 4번 반복
    print("list1[%d] : %s"%(i,list1[i]))

#5.5.4 리스트 문자열로 변환하기
names = ["정", "종", "혁"]
print(names)

x = "/".join(names) #리스트 names 요소들 사이에 /를 넣어서 하나의 문자열로 만든다
print(x)

phone1 = ["010", "1234", "5678"]
print(phone1)

phone2 = "-".join(phone1)
print(phone2)
'''
#5.5.5 리스트 문자열에서 하이픈 삭제하기
'''
phone_list1 = ["010-1234-5678", "010-9876-5432", "010-1928-4857"]
print(phone_list1)

phone_list2 = []
for number in phone_list1:
    x = number.replace("-","")

    phone_list2.append(x)

print(phone_list2)
'''
#5.5.6 리스트에서 문자열로 치환하기

sentences = ["Love me, love my cat." , "No news is good news.", "Blood is thicker than water"]

for sentence in sentences:
    x = sentence.replace(" ", "_")
    print(x)


#문자열 메소드
'''
find() : 문자열에서 특정 문자열을 찾앙 위치(인덱스 번호)를 구함
replace() : 문자열에서 특정 문자열을 다른 문자열로 치환함
split() : 특정 문자열을 기준으로 문자열을 조개서 리스트에 저장함
join() : 리스트의 요소를 하나로 묶어서 문자열로 변환함
'''