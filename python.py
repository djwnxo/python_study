# a, b = map(int, input().split())
# c = input()

# if c == "+":
#     print(a + b)
# if c == "*":
#     print(a * b)

# ========================
# def plus(a, b):
#     return a + b

# def mult(a, b):
#     return a * b

# a, b = map(int, input().split())
# c = input()

# if c == "+":
#     print(plus(a, b))
# if c == "*":
#     print(mult(a, b))

# ========================

def calc(a, b, c):
    if c == "+":
        print(a + b)
    if c == "*":
        print(a * b)

a, b = map(int, input().split())
c = input()
calc(a, b, c)



