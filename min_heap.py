# Name: Marina Moger
# OSU Email: mogerm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 - minheap
# Due Date: 3/3/25
# Description: This program implements a MinHeap data structure using a DynamicArray,
# includes heap operations such as insertion, deletion, heap construction,
# and heapsort.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new element to the MinHeap while maintaining the heap property.

        Time Complexity: Amortized O(log N)
        """
        # Append the new element at the end of the heap
        self._heap.append(node)

        # Percolate up
        child = self._heap.length() - 1
        parent = (child - 1) // 2  # Compute parent index

        while child > 0 and self._heap[child] < self._heap[parent]:
            # Swap if the child is smaller than the parent
            self._heap[child], self._heap[parent] = self._heap[parent], self._heap[child]
            child = parent  # Move up the heap
            parent = (child - 1) // 2  # Recompute parent index

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty; otherwise, returns False.

        Time Complexity: O(1)
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Returns the smallest element in the MinHeap without removing it.
        Raises a MinHeapException if the heap is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        return self._heap[0]  # The minimum element is always at index 0

    def remove_min(self) -> object:
        """
        Removes and returns the smallest element in the MinHeap.
        Raises a MinHeapException if the heap is empty.

        Time Complexity: Amortized O(log N)
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        # Store the minimum element
        min_value = self._heap[0]

        # Replace the root with the last element
        last_index = self._heap.length() - 1
        if last_index > 0:
            self._heap[0] = self._heap[last_index]

        # Remove the last element correctly using remove_at_index()
        self._heap.remove_at_index(last_index)

        # Restore heap property by percolating down
        if not self.is_empty():
            _percolate_down(self._heap, 0)

        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a MinHeap from an unordered DynamicArray.
        Overwrites any existing heap content.

        Time Complexity: O(N)
        """
        # Replace the current heap with the given DynamicArray
        self._heap = DynamicArray()
        for i in range(da.length()):
            self._heap.append(da[i])

        # Start percolating down from the last non-leaf node
        last_non_leaf = (self._heap.length() // 2) - 1
        for i in range(last_non_leaf, -1, -1):
            _percolate_down(self._heap, i)

    def size(self) -> int:
        """
        Returns the number of elements currently stored in the MinHeap.

        Time Complexity: O(1)
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the MinHeap, leaving it empty.

        Time Complexity: O(1)
        """
        self._heap = DynamicArray()  # Reinitialize the heap with a new empty DynamicArray


def heapsort(da: DynamicArray) -> None:
    """
    Sorts the given DynamicArray in non-ascending order using the Heapsort algorithm.
    Sorting is done in place without using extra data structures.

    Time Complexity: O(N log N)
    """
    # Build a MinHeap using the given array
    heap = MinHeap()
    heap.build_heap(da)

    # Extract the min element one by one and store it back in da in reverse order
    for i in range(da.length() - 1, -1, -1):
        da[i] = heap.remove_min()  # Place the smallest element at the end



# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(heap: DynamicArray, parent: int) -> None:
    """
    Moves the element at index 'parent' down the heap to restore the heap property.

    Time Complexity: O(log N)
    """
    heap_size = heap.length()
    while True:
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        smallest = parent

        # Check if left child exists and is smaller than the current smallest
        if left_child < heap_size and heap[left_child] < heap[smallest]:
            smallest = left_child # Update smallest to left child index

        # Check if right child exists and is smaller than the current smallest
        if right_child < heap_size and heap[right_child] < heap[smallest]:
            smallest = right_child # Update smallest to right child index

        # If the parent is already the smallest, heap property is restored, so stop
        if smallest == parent:
            break
        heap[parent], heap[smallest] = heap[smallest], heap[parent]
        parent = smallest


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
