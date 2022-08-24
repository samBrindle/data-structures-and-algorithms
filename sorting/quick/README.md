# Blog Notes: Quick Sort
Quick Sort is an algorithm that picks an element as a pivot and partitions the given list around the pivot element. The partition helper function starts at the leftmost element and keeps track of the index of smaller elements. If it finds a smaller element, we swap those elements with the current index at list[i] if its bigger, we ignore it.

## Pseudocode
* Create a function quick_sort that takes in a list, and a starting index(left), and an ending index(len(list-1))
  * if left is greater than right:
    * create a variable position and set it equal to a partition function call of with the parameters (list, left, right)
    * recursively call quick_sort on the parameters (list, left, position - 1)
    * recursively call quick_sort on the parameters (list, position + 1), right
  * return list
* Create a helper function called partition that takes in a list a starting position(left), and an ending position(right) as parameters
  * create a variable pivot that is equal to list at index right
  * create a low variable that is equal to left - 1
  * for loop for i in range of left to right
    * if list at index i is less than or equal to pivot
      * low equals low + 1
      * call swap helper function with parameters (list, i, low)
  * call swap helper function with parameteres (list, right, low + 1)
  * return low + 1
* Create second helper function called swap that takes a list, i, and low as parameters
  * create a temp variable set equal to list at index i
  * set list at index i equal to list at index low
  * set list at index low equal to temp

## Trace
Sample List: [8, 23, 4, 16]
* Pass 1:
  * left: 0, right: 3, list: [8, 23, 4, 16], position:2
  * Whats happening here is we are passing in the list, the beginning index and the ending index into quick_sort([8, 23, 4, 16], 0, len(list)-1)
  * When passing this info into partition we receive a 2 back.
  * This 2 is then used in the recursive call we do.
* Pass 2:
  * left: 0, right: 1, list: [8, 4, 16, 23], position:0
  * We now have left=0 still but right is now 1 while our list has been sorted with 16 and 23 being pushed to the end
  * When passing this info into partition we receive a position of 0 which tells us to swap 8 and 4
  * This 0 is used in our recursive call
* Pass 3:
  * left: 0, right: 1, list: [4, 8, 16, 23], position: 0
  * The final swapping happens here, and we have a fully sorted list.
