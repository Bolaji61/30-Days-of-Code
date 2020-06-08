import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

allSwapCount = 0
for i in range(n):
    #Track number of elements swapped in array
    numSwaps = 0
    for j in range(n-1):
        #Swap array elements as appropriate
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps+=1
    allSwapCount += numSwaps
print("Array is sorted in %d swaps." % (allSwapCount))
print("First Element: %d" % (a[0]))
print("Last Element: %d" % (a[-1]))
