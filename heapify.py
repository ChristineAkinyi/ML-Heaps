def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    # check if left child exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # check if right child exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root again.
        heapify(arr, n, largest)