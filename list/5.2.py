#5.2.1 for문에서 리스트 사용하기

colors = ["빨간색", "파란색", "노란색", "검은색", "초록색"]

for color in colors:
    print("나는 %s을 좋아한다"% color) # %s는 문자열

#다른 방법
colors = ["빨간색", "파란색", "노란색", "검은색", "초록색"]

n = len(colors) #len()함수 : 리스트의 길이
for i in range(0,n): # i의 값 : 0~4
    print("나는 %s를 좋아한다"%colors[i]) # i : colors의 인덱스


#5.2.2 while문에서 리스트 사용하기

animals = ["코끼리", "호랑이", "사슴", "펭귄", "여우"]

i = 0
while i < len(animals): #i가 animals 리스트의 길이 보다 작을 때
    print(animals[i]) #animals 리스트에 있는 i번재 항목을 출력한다

    i = i + 1

