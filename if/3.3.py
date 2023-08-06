#3.3 if 구문

age = int(input("나이"))
ticket = 2000 #기본 입장료

if age >= 65:
    ticket = 0

print("나이 : %d세"%age)
print("입장료 : %d원"%ticket)