#2차원 리스트
#5.6.1 2차원 리스트의 구조
'''
numbers = [[10,20,30],[40,50,60,70,80]]

print(numbers[0][0]) #numbers[0][0] 에서 첫 번째 [0]은 [10,20,30],[40,50,60,70,80] 이 두 리스트 중 첫 번째를 의미하고, 두 번째 [0]은 첫 번째 [0]에서 골라진 리스트 중 요소들의 순서를 의미한다
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

#5.6.2 2차원 리스트와 이중 for문

data = [[10,20],[30,40],[50,60],[70,80]]

for i in range(4): #아래 명령어를 4번 반복한다
    for j in range(2): #아래 명령어를 두 번 반복한다
        print("data[%d][%d] = %d"%(i,j,data[i][j]))

#5.6.3 2차원 리스트로 합계와 평균 구하기

scores = [[75,83,90,90,14],[86,86,73],[76,95,83,77],[89,96,69],[89,76,93]]

for i in range(len(scores)): #리스트 scores의 길이 만큼 반복
    sum = 0
    for j in range(len(scores[i])): #리스트 scores의 i번째의 리스트 안의 요소의 길이만큼 반복
        sum = sum + scores[i][j]

    avg = sum/len(scores[i])

    print("%d번째 학생의 합계 : %d, 평균 : %.2f" %(i+1,sum,avg))

'''
#5.6.4 2차원 리스트로 문자열 다루기
strings = [["원두커피", "라떼", "콜라"],["우동","국수","피자","파스타"]]

for i in range(len(strings)): #strings 리스트 의 길이 만큼 반복
    for j in range(len(strings[i])): #리스트 strings의 i 번째 리스트 안의 요소의 길이만큼 반복
        print(strings[i][j])