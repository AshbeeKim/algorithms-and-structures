#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Plus Minus
def plusMinus(arr):
    # Write your code here
    plus = list(filter(lambda x: x > 0, arr))
    minus = list(filter(lambda x: x < 0, arr))
    zero = list(filter(lambda x: x == 0, arr))
    print(len(plus) / len(arr))
    print(len(minus) / len(arr))
    print(len(zero) / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# Mini-Max Sum
def miniMaxSum(arr):
    # Write your code here
    sums = []
    for i in range(len(arr)):
    #     sums.append(sum(list(filter(lambda x: x!=arr[i], arr)))) ## 한 케이스에서 Wrong Answer 발생 >> drop
        left = [] if i == 0 else arr[:i]
        right = [] if i == len(arr) - 1 else arr[i+1:]
        sums.append(sum(left + right))

    print(min(sums), max(sums), sep=" ")
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# Time Conversion
def timeConversion(s):
    # Write your code here
    s, comp = s[:-2], s[-2:]
    times = list(map(str, s.split(':')))
    if (comp == "AM")&(times[0] == "12"):
        return ":".join(["00", times[1], times[2]])
    elif ((comp == "PM")&(times[0] == "12"))|(comp == "AM"):
        return ":".join(times)
    else:
        return ":".join([str(int(times[0])+12), times[1], times[2]])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


# Sparse Arrays
def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for _ in queries:
        result.append(strings.count(_))
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


# Lonely Integer
def lonelyinteger(a):
    c = Counter(a)
    c = sorted(c.items(), key=lambda x: x[1])
    return c[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()


# Flipping bits
def flippingBits(n):
    b = format(n, 'b')
    if len(b) < 32:
        b = '0'*(32 - len(b)) + b
    b = b.replace('0', '*')
    b = b.replace('1', '0')
    b = b.replace('*', '1')
    return int('0b' + b, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')
    fptr.close()


# Diagonal Difference
def diagonalDifference(arr):
    rl = [arr[i][j] for i, j in zip(range(len(arr)), range(len(arr)-1, -1, -1))]
    lr = [arr[i][j] for i, j in zip(range(len(arr)), range(len(arr)))]
    return abs(sum(lr) - sum(rl))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Counting Sort 1
def countingSort(arr):
    c = Counter(arr)
    m = {i:0 for i in range(100)}
    return list(map(lambda x: c.get(x[0]) if x[0] in list(c.keys()) else x[1], m.items()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    

# Pangrams
def pangrams(s):
    # Write your code here
    temp = Counter(s.lower())
    comp = {S:0 for S in list("abcdefghijklmnopqrstuvwxyz")}
    comp = dict(map(lambda x: (x[0], temp.get(x[0])) if x[0] in temp.keys() else (x[0], x[1]), list(comp.items())))
    if  list(filter(lambda x: x==0, comp.values())):
        return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()


# Permuting Two Arrays
def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    arr = [a + b for a, b in zip(A, B)]
    arr = list(map(lambda x: x >= k, arr))
    return "NO" if False in arr else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()


# Subarray Division 1
def birthday(s, d, m) -> int:
    # Write your code here
    arr = []
    for i in range(len(s)):
        arr.append(s[i : i + m])
        if i + 2 == len(arr):
            break
    return len(list(filter(lambda x: x==d, list(map(sum, arr)))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())    # len(s)

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split() # d, m,, 왜 이렇게 불러온 것인지 이해하려 하지 말 것

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()


# XOR Strings 2
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
## 와 4줄의 공백


# Mock Test

