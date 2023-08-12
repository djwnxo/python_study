#7.3 함수 값의 변환
# 정의된 함수에서 얻은 값을 return문을 이용하여 호출한 함수 측에 반환할 수 있다. 이것을 함수 값의 반환이라고 한다.

def func(n):
    x = n + 5
    return x #x를 함수 값으로 반환

a = func(10) #func(10)은 함수 정의에서 반환된 x 값을 가짐
print(a)
b = func(20) #func(20)은 함수 정의에서 반환된 x 값을 가짐
print(b) 