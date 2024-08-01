# ML-Heaps
This repository contains code for the following questions:
 
# A Python3 program to convert min Heap to max Heap

1. Define the function MaxHeapify that maintains the max-heap property for the subtree rooted at index i in an array of size N.
2. Compute the index l of the left child of the node at index i.
3. Compute the index r of the right child of the node at index i.
4. Initialize largest to i, assuming the root node has the largest value.
5.  Verify if the left child exists (l < N) and is greater than the root node (arr[i]). If so, update largest to l.
6. Verify if the right child exists (r < N) and is greater than the current largest value (arr[largest]). If so, update largest to r.
7. If the largest value is not at the root (i), swap the root with the largest child.
8. Recursively call MaxHeapify on the subtree rooted at the index largest to ensure the subtree maintains the max-heap property.
9. Define the function convertMaxHeap that transforms an arbitrary array into a max-heap.
10. Iterate from the last internal node (int((N - 2) / 2)) up to the root (0), applying MaxHeapify to ensure each subtree satisfies the max-heap property.
11. Define a helper function printArray that prints all elements of an array.

# Function to create a min heap from an array
Create an array arr representing a min-heap: [3, 5, 9, 6, 8, 20, 10, 12, 18, 9].
Determine the length of the array: N = len(arr).
Execution:

Print the original min-heap array using printArray.
Convert the min-heap to a max-heap by calling convertMaxHeap(arr, N).
Print the converted max-heap array using printArray.

##Question 2: Heapify an array
1. Define the function heapify that adjusts the subtree rooted at index i to maintain the heap property in an array of size n.
2. Initialize largest to i. Assume the root of the subtree (arr[i]) is the largest.
3. Calculate the index l of the left child of the root (arr[i]).
4. Calculate the index r of the right child of the root (arr[i]).
5. Check if the left child exists (l < n) and if it is greater than the root. If true, update largest to l.
6. Check if the right child exists (r < n) and if it is greater than the current largest. If true, update largest to r.
7. If largest is not the root (i), swap the root with the largest child.
8. Call heapify on the subtree rooted at largest to ensure the subtree maintains the heap property.

# Function to check if the given list represents min-heap or not
1. Define the function checkMinHeap which takes a list A and an index i as parameters.
2. Check if i is a leaf node by verifying if 2*i + 2 (the index of the right child) is greater than or equal to the length of the list A.
3. Return True if i is a leaf node since a leaf node trivially satisfies the min-heap property.
4. Check if the left child (at index 2*i + 1) is a valid heap:
-Ensure A[i] (the value at the current node) is less than or equal to A[2*i + 1] (the value of the left child).
-Recursively call checkMinHeap function on the left child to ensure it is also a min-heap.
-Assign the result to "left"
5. Check if the right child (at index 2*i + 2) is a valid heap:
-If 2*i + 2 is exactly at the end of the list (len(A)), then the right child does not exist, which is valid.
-Otherwise, ensure A[i] is less than or equal to A[2*i + 2] (the value of the right child).
-Recursively call checkMinHeap on the right child to ensure it is also a min-heap.
-Assign the result to right.
6. Return True if both the left and right subtrees (children) are min-heaps; otherwise, return False.

# Function for heap sort algorithm
1. Calculate and return the index of the left child of the node at index i. The left child is at position 2*i + 1.
2. Calculate and return the index of the right child of the node at index i. The right child is at position 2*i + 2.
3. Define a utility function swap to exchange the elements at indices i and j in the list A. Use a temporary variable temp to facilitate the swap.
4. Define the heapify function to maintain the heap property starting from index i.
Compute the indices of the left and right children using LEFT(i) and RIGHT(i).
Initialize largest to i.
5. Check if the left child exists (left < size) and is greater than the current node (A[i]). If so, update largest to left.
6. Check if the right child exists (right < size) and is greater than the current largest value (A[largest]). If so, update largest to right.
7. If the largest value is not at the current index i, swap the values at indices i and largest.
Recursively call heapify on the subtree rooted at largest to ensure the heap property is maintained.
8. Define the pop function to remove and return the root of the heap. If the heap is empty (size <= 0), return -1.
9. Store the root value (A[0]) in top.
Replace the root with the last element in the heap (A[size - 1]).
Call heapify on the root node to maintain the heap property after the removal.
Return the original root value (top).
10. Define the heapsort function to sort a list A. Compute the length of the list n.
11. Build the heap by calling heapify starting from the last internal node ((n - 2) // 2) up to the root node (0).
12. Sort the list by repeatedly popping the root (maximum element) and placing it at the end of the list. Decrease the size of the heap (n - 1) each time.

# Find the kth largest element in a heap
1. Define the function kLargest that takes a list arr and an integer k as parameters.
2. Sort the list arr in descending order using sort(reverse=True). This means the largest elements will come first.
3. Iterate through the first k elements of the sorted list using a for loop with range k
4. Print each of these k largest elements, separated by a space (end=" " ensures that the elements are printed on the same line).
5. Initialize a list arr with some example values.
6. Set the value of k to 3, meaning we want to find the 3 largest elements from the list.
7. Call the kLargest function with arr and k as arguments to print the 3 largest elements from the list.

