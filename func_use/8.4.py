#이진 탐색
#이진 탐색(Binary search)에서는 요소들이 오름차순 또는 내림차순으로 정렬되어 있어야 한다. 만약 리스트가 정렬되어 있지 않다면 이진 탐색을 적용하기 전에 리스트를 사전에 정렬해 놓아야 한다. 이진 탐색에서는 지속적으로 탐색 범위를 1/2 씩 줄여가면서 해당값을 찾는다
#특정 값 인덱스 찾기(while 문)

def binary_search(n,x):
    start = 0
    end = len(n)-1

    while start <= end:
        mid = (start + end)//2
        if x == n[mid]:
            return mid
        elif x>n[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1

data = [7,16,23,35,40,52,68,78,82]
print(data)

search_num = 52
index = binary_search(data, search_num)
print("%d의 위치 : %d"%(search_num, index))