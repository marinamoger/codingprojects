# Name: Marina Moger
# OSU Email: mogerm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 - Dynamic Arrays
# Due Date: 2/3/25
# Description: Contains the implementation of a Bag Abstract Data Type (ADT), which
# uses the DynamicArray class as storage. It includes methods like add(), remove(),
# count(), clear(), and iterator functions to manipulate elements in the Bag.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the Bag
        """
        # append the new value to the DynamicArray
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes the first occurrence of the specified element from the Bag.
        """
        # search for the value in the DynamicArray
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                # remove the element by shifting elements to the left
                self._da.remove_at_index(i)
                return True

        # if the element was not found, return False
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of occurrences of the specified element in the Bag.
        """

        # initialize counter
        count = 0

        # iterate through the DynamicArray using a loop and get_at_index()
        for i in range(self._da.length()):
            element = self._da.get_at_index(i)
            if element == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Removes all elements from the Bag by resetting the DynamicArray.
        """
        # reset the DynamicArray to a new empty DynamicArray
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares the current bag with another bag to check if they are equal.
        Two bags are equal if they contain the same elements with the same frequencies.
        """
        # check if both bags have the same size
        if self._da.length() != second_bag._da.length():
            return False # if they are not the same length, they cannot be equal

        # compare the frequency of each element in the current bag to the second bag
        for i in range(self._da.length()):
            element = self._da.get_at_index(i)  # access element using get()

            # count occurrences of the element in both bags
            count_self = self.count(element)
            count_second = second_bag.count(element)

            # if the counts don't match, the bags are not equal
            if count_self != count_second:
                return False

        return True

    def __iter__(self):
        """
        Initializes the bag iterator.
        Returns the iterator object (self).
        """
        self._current_index = 0  # initialize the iterator index
        return self

    def __next__(self):
        """
        Returns the next element in the bag during iteration.
        """
        if self._current_index >= self._da.length():
            raise StopIteration

            # get the current element and advance the index
        element = self._da.get_at_index(self._current_index)
        self._current_index += 1
        return element


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
