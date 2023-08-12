#사용자 함수 활용
#8.2.1 소수 여부 판별하기
'''
def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                prime = False
    
    return prime

number = int(input("수를 입력하세요 : "))

if is_prime(number):
    print("소수이다!")
else :
    print("소수가 아니다!")
'''

#8.2.2 세제곱 합계 구하기
'''
def square_sum(n):
    sm = 0
    for i in range(1, n+1): #i : 1~n
        sm = sm + (i*i*i) #누적합계 sm 구함

    return sm

N = int(input("N의 값을 입력하세요 : "))
print(square_sum(N))
'''
#8.2.3 회문인지 판별하기
#회문은 똑바로 읽으나 거꾸로 읽으나 똑같은 단어나 문자을 말한다.
'''
def is_palindrome(s):
    for i in range(0, int(len(s)/2)): #문자열의 좌측 절반 읽음
        if s[i] != s[len(s)-i-1]: #w\좌측과 우측 인덱스가 다른지 비교
            return False
        
    return True

string = "rotator"

if is_palindrome(string):
    print("%s은(는) 회문이다!"%string)
else:
    print("%s은(는) 회문이 아니다!"%string)
'''
#8.2.4 문장 단어 반대로 말하기
'''
def rvs_sentence(s):
    words = s.split(" ") #문자열 s를 쪼개서 리스트로 저장
    result = "" #result에 빈 문자열 저장
    for word in words:
        result = word + " " + result #result 앞 부분에 word 삽입

    return result

sentence = "Nice to meet you"
print(rvs_sentence(sentence))
'''
#8.2.5 문자열 존재 여부 판별하기
'''
def check_words(s, keyword):
    if (s.find(keyword) == -1): # 검색 후 반환된 인덱스가 -1인가
        print("'%s'은(는) 존재하지 않는다!"%keyword)

string = "A good book is a great friend."
word = "friend"

print("문장 :", string)
print("찾는 단어 :", word)

check_words(string,word)

#s.find(keyword)는 문자열 s내에 문자열 keyword가 존재하는지를 찾는다. 해당 문자열이 처음 나오는 위치, 즉 인덱스 값을 반환한다. 그러나 만약 해당 문자열(keyword)이 문자열(s)내에 존재하지 않는 경우에는 -1값을 반환한다.

#8.2.6 다수의 문자열 치환하기

def replace_word(string, word_list, word):
    arr = string.split(" ") #문자열 쪼개서 리스트 arr에 저장
    new_arr = [] # new_arr에 빈 리스트 저장
    for x in arr:
        if x in word_list:
            new_arr.append(word) #new_arr에 word 추가
        else:
            new_arr.append(x)#new_arr에 x추가

    result = " ".join(new_arr)#new_arr 붙여서 문자열로 만듦
    return result

string = "python java php apple orange banana"
word_list = ["apple", "orange", "banana"]#치환할 단어 목록
word = "fruits"#치환단어
print("문자열 :",string)
print("단어 리스트 :",word_list)
print("치환할 단어 :",word)

new_str = replace_word(string, word_list, word)
print("치환된 문자열 :",new_str)
'''
#8.2.7 문자열 위치 이동시키기

def string_shift(string, d, direction):
    if direction == "left": #왼쪽으로 이동
        left_part = string[d:] #left_part : 이동 후 문자열 왼쪽 부분
        right_part = string[0:d] #right_part : 이동 후 문자열 오른쪽 부분
    else:
        left_part = string[len(string)-d:]
        right_part = string[0:len(string)-d]

    result = left_part + right_part #왼쪽과 오른쪽 부분 서로 연결
    return result

string = "pythonprogramming"

str_left = string_shift(string, 2, "left") #문자열 string내의 문자들을 왼쪽으로 2칸
str_right = string_shift(string,3,"right")

print("원래 문자열 :",string)
print("좌측으로 2칸 이동 :", str_left)
print("우측으로 3칸 이동 :",str_right)