def heapify(arr: list, length: int, index: int):
    max_index = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if (left_index < length and arr[left_index] > arr[max_index]):
        max_index = left_index
    if (right_index < length and arr[right_index] > arr[max_index]):
        max_index = right_index
    if (max_index != index):
        arr[max_index], arr[index] = arr[index], arr[max_index]
        heapify(arr, length, max_index)


def heap_sort(arr: list):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [64, 34, 25, 12, 22, 11, 90]

heap_sort(arr)

print(arr)
