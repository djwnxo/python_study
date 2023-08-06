#딕셔너리란
'''
파이썬의 딕셔너리는 자료를 찾는 인덱스를 의미하는 키(key)와 자료의 내용인 값(Value)을 이용하여 데이터를 관리한다. 딕셔너리에서는 다음과 같이 요소들을 중괄호 {}로 감사게 된다
'''
#6.2.1 딕셔너리 생성하기

member = {"name": "정종혁", "age":"16","email":"kinjeok@gmail.com"}
print(member)

score = dict([("국어",80),("영어",90),("수학",100)])
print(score)

#6.2.2 딕셔너리 요소 추출하기
user = {"id":"kinjeok","name":"정종혁","level":"99","point":9999999999999}
print(user) #딕셔너리 전체 출력
print(user["id"]) #id의 키값 출력
print(user["name"]) #name의 키값 출력
print(user["point"]) #point의 키값 출력