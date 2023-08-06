#딕셔너리 요소 변환
#6.3.1 딕셔너리에 요소 추가하기

scores = {"kor":90, "eng": 89, "math":98}
print(scores)

scores["music"]=100 #딕셔너리 마지막에 'music' : 100 추가
print(scores)

#6.3.2 딕셔너리 요소 수정하기

words = {"door":"문","chair":"의자","table":"책상","house":"집"}
print(words)

words["table"] = "테이블" #"table" 키의 값을 "테이블"로 변경
print(words)

words["house"] = "하우스"
print(words)

#6.3.3 딕셔너리 요소 삭제하기

car = {"brand":"nexon", "model":"paragon","start":"2015","year":2023}
print(car)

x=car.pop("start") #"start" 요소 추출과 동시에 해당 요소 삭제
print(x)

print(car)

car = {"brand":"nexon", "model":"paragon","start":"2015","year":2023}
print(car)
car.clear()
print(car)