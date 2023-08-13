#C8-1 예제 8-6의 출력 포맷을 바꾸어라!
'''
def square_sum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i*i*i)
        print("%d*%d*%d"%(i,i,i),end=" ")

        if i == n:
            print("= ", end = "")
        else:
            print("+ ", end="")
    print(sm)

N = int(input("N의 값을 입력하세요 : "))
square_sum(N)
'''
#C8-2 1~N 홀수의 세제곱 합을 구하라!
'''
def square_sum(n):
    sm = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            sm = sm + (i*i*i)
            print("%d*%d*%d"%(i,i,i),end =" ")

            if i == n or i == (n-1):
                print("= ", end="")
            else:
                print("+ ", end="")
    print(sm)

N = int(input("N의 값을 입력하세요 : "))
square_sum(N)
'''
#C8-3 키보드로 입력받은 단어가 회문인지 판별하라잉!
'''
def is_palindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    
    return True

string = input("단어를 입력하세요 : ")

if is_palindrome(string):
    print("'%s'은(는) 회문이다!"%string)
else:
    print("'%s'은(는) 회문이 아니다!"%string)
'''
#C8-4 문장의 단어 개수를 카(운)트(하)라!이더
'''
def count_word(s):
    arr = s.split(" ")

    return len(arr)

string = input("문장을 입력하세요 : ")

num_word = count_word(string)
print("단어의 개수 :", num_word)
'''
#C8-5 문장에서 특정 단어를 삭제하랑!
'''
def del_word(s, w)':
    arr = s.split(" ")
    arr.remove(w)
    result = " ".join(arr)

    return result

string = "Don't cry before you are the hurt."
word = "the"

new_str = del_word(string, word)
word = "the"

new_str = del_word(string, word)
print("원래 문자열 :", string)
print("삭제 단어 :", word)
print("변경된 문자열 :", new_str)
'''
#C8-6 선형 탐색으로 최솟값을 찾아리랑!
'''
def find_min(n):
    smallest = n[0]
    for i in range(1,len(n)):
        if n[i] < smallest:
            smallest = n[i]

    return smallest

data = [6,3,-2,12,5,-3,17,9,13]
print(data)

min_value = find_min(data)
print('최솟값 :',min_value)
'''
#C8-7 이진 탐색으로 내림차순에서 특정 값을 찾아라푼젤!

def binary_search(n,x):
    start = 0
    end = len(n) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == n[mid]:
            return mid
        elif x > n[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

data = [93,91,89,87,80,61,55,43,41,38,32,30,25,20,8,2]
print(data)

search_num = 89
index = binary_search(data, search_num)
print('%d의 인덱스 번호 : %d'%(search_num, index))