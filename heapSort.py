def heapify(numbers, n, i):

    maxNumIdx = i
    leftIdx = 2*i + 1
    rightIdx = 2*i + 2

    print("[HEAPIFY] numbers:{} | n:{} | i:{} | maxNumIdx: {} | leftIdx:{} | rightIdx:{}"
          .format(numbers, n, i, maxNumIdx, leftIdx, rightIdx))

    if leftIdx < n and numbers[i] < numbers[leftIdx]:
        print("[maxNumIdx:{} >> Left Index:{}]".format(maxNumIdx, leftIdx))
        maxNumIdx = leftIdx

    if rightIdx < n and numbers[maxNumIdx] < numbers[rightIdx]:
        print("[maxNumIdx:{} >> Right Index:{}]".format(maxNumIdx, rightIdx))
        maxNumIdx = rightIdx

    # Swap The Elements to Build the Max Heap
    # Root Element shall be Swapped with largest
    # From there onwards we continue heapify :)
    if maxNumIdx != i:
        print("[maxNumIdx:{} != i:{}]".format(maxNumIdx, i))
        numbers[i], numbers[maxNumIdx] = numbers[maxNumIdx], numbers[i]

        # Recursion
        print("[Recursion From Heapify]: heapify numbers:{} | n:{} | maxNumIdx:{}"
              .format(numbers, n, maxNumIdx))
        heapify(numbers, n, maxNumIdx)

def heapSort(numbers):

    print("[HEAP SORT]:", numbers)

    n = len(numbers)

    # Building Max Heap for numbers:
    for i in range(n-1, 0, -1):
        heapify(numbers, n, i)

    # Swapping the Element with Root
    for i in range(n-1, 0, -1):
        print("SWAP: {}->{} with {}->{} in numbers:{}"
              .format(i, numbers[i], 0, numbers[0], numbers))
        # HeapSort: Swap the 0th i.e. Root
        numbers[i], numbers[0] = numbers[0], numbers[i]

        print("SWAP: new numbers:{}".format(numbers))

        # Heapifying the Root Element
        # Recursion
        print("[Recursion From Heapify]: heapify numbers:{} | i:{} | Root:{}"
              .format(numbers, i, 0))
        heapify(numbers, i, 0)


numbers = [91, 76, 22, 11, 21, 34, 66]

print("Original Numbers:", numbers)
heapSort(numbers)
print("Sorted Numbers:", numbers)