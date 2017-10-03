import sys

def oddEven():
    for i in range(1, 2001):
        sys.stdout.write("Number is " + str(i) + ". ")
        if i % 2:
            print "This is an odd number"
        else:
            print "This is an even number"

def multiply(arr, m):
    arr2 = []
    for i in arr:
        arr2.append(i * m)
    return arr2

def hackerChallenge(arr):
    arr2 = []
    for i in range(0, len(arr)):
        arr2.append([])
        for j in range(0, arr[i]):
            arr2[i].append(1)
    return arr2

oddEven()
print multiply([2,4,10,16], 5)
print hackerChallenge(multiply([2,4,5], 3))
