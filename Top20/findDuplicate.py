import sys
import time

# Naive approach, brute force
# T:O(n^2) S:O(1)
def findDuplicate1(inp):
    n=len(inp)
    for i in range(n):
        for j in range(i+1,n):
            if(inp[i] == inp[j]):
                return inp[i]
    return sys.minvalue

# Adhoc Sort and Scan
# T:O(nlogn) S:O(1)
def findDuplicate2(inp):
    inp.sort()
    n=len(inp)
    for i in range(1, n):
        if(inp[i] == inp[i-1]):
            return inp[i]            
    return sys.minvalue

# Data Structure pattern, Lookup Array
# T:O(n) S:O(n)
def findDuplicate3(inp):
    n = len(inp)
    aux = [bool]*n
    for i in range(n):
        tmp = inp[i]
        if(aux[tmp] == True):
            return tmp
        aux[tmp] = True
    return sys.minvalue

# Adhoc Negation Trick (Input array should be mutable)
# T:O(n) S:O(1)
def findDuplicate4(inp):
    n = len(inp)
    for i in range(n):
        tmp = abs(inp[i])
        if(inp[tmp] < 0):
            return tmp
        inp[tmp] *= -1
    return sys.minvalue

# Set Data Structure
# T:O(n) S:O(n)
def findDuplicate5(inp):
        s=set()
        for i in range(len(inp)):
            if inp[i] in s:
                return inp[i]
            else:
                s.add(inp[i])

def testcase1(inp):
    n = len(inp)
    for i in range(n-1):
        inp[i] = i+1
    inp[n-1] = n-1

def main():
    n = int(sys.argv[1])
    inp = [int] * n
    testcase1(inp)

    start = time.time()
    print(findDuplicate1(inp))
    end = time.time()
    print("Time Taken for findDuplicate1: ", (end - start))
    # ------------------------------------
    start = time.time()
    print(findDuplicate2(inp))
    end = time.time()
    print("Time Taken for findDuplicate2: ", (end - start))
    # ------------------------------------
    start = time.time()
    print(findDuplicate3(inp))
    end = time.time()
    print("Time Taken for findDuplicate3: ", (end - start))
    # ------------------------------------
    start = time.time()
    print(findDuplicate4(inp))
    end = time.time()
    print("Time Taken for findDuplicate4: ", (end - start))
    # ------------------------------------
    testcase1(inp)
    start = time.time()
    print(findDuplicate5(inp))
    end = time.time()
    print("Time Taken for findDuplicate5: ", (end - start))
    # ------------------------------------

if __name__ == "__main__":
    main()