# -*- coding: utf-8 -*-

#1
print('Hello World!')

#2
print('강한친구 대한육군')
print('강한친구 대한육군')

#3
print('''\\    /\\
 )  ( ')
(  /  )
 \\(__)|''')

print('\\    /\\')
print(") )  ( ')")
print('(  /  )')
print(' \\(__)|')

#4
print('''|\\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')

#5
a, b = map(int, input().split())
print(a+b)

#6
a, b = map(int, input().split())
print(a-b)

#7
a, b = map(int, input().split())
print(a*b)

#8
a, b = map(int, input().split())
print(a/b)

#9
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, end='\n')

#10
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, end='\n')

#11
a, b = map(int, input().split())
print(a*int(str(b)[-1:]), a*int(str(b)[1:2]), a*int(str(b)[:1]), a*b, end='\n')
# a, b = map(int, str, input().split())
# print(a*int(b[-1:]), a*int(b[1:2]), a*int(b[:1]), a*int(b), end='\n')

######################################################## changed ########################################################

# 10
id = input().lower()  # 따로 길이에 따른 예외처리는 하지 않음
print(id + "??!")

# 11
year = int(input())
print(year-543)

# 13
A = int(input())
B = int(input())
print(A*int(str(B)[-1]))
print(A*int(str(B)[-2]))
print(A*int(str(B)[-3]))
print(A*B)
