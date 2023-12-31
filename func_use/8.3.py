#8.3 선형 탐색
#선형 탐색(Linear search)은 다른 말로 순차 탐색(Sequential search)이라고도 한다. 선형 탐색에서는 찾고자 하는 요소와 리스트에 있는 요소들을 순차적으로 하나씩 비교해 나간다.
#선형 탐색을 이용하여 최댓값 구하기

def find_max(n):
    mx = n[0] #초기 최댓값(mx) : 첫 번째 요소
    for i in range(1, len(n)): # i : 1~4   
        if n[i] > mx: #요소 값이 mx보다 크면
            mx = n[i]#mx에 요소값 저장

    return mx

data = [5,-3,12,8,2]
print(data)
max_value = find_max(data)
print("최댓값 :", max_value)