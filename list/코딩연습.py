#C5-1 1~20의 양의 정수 리스트를 생성하라!
'''
data = list(range(1,21))

for i in range(0, len(data)):
    print("%d"%data[i], end = " ")
'''
#C5-2 C5-1에서 짝수 번째 요소를 출력하라!
'''
data = list(range(1,21))

for i in range(0, len(data)):
    if i % 2 == 1:
        print("%d"%data[i], end = " ")
        '''
#C5-3 C5-2에서 홀수 번째 요소를 출력하라!
'''
data = list(range(1,21))
i = 0
while i<=20:
    if i % 2 == 1:
        print("%d"%i, end = " ")
    i = i + 1
        '''

#C5-4 빈 리스트에 요소를 추가하라!

data = []
for x in range(10,21):
    data.append(x)

print(data)