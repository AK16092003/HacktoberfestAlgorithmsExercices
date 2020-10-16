from exercicies.linked_list import ItemList, LinkedList, insertFirst, mergeList, sortList


def test_sorted_list():
    unsortedList = [1,5,3,7,8,23,2,42,16,1]
    my_list = LinkedList()
    for i in unsortedList:
        insertFirst(my_list, i)

    sortedList = unsortedList.sort()
    my_sorted_list = LinkedList()
    for i in sortedList:
        insertFirst(my_sorted_list, i)

    assert my_sorted_list == sortList(my_list), "Different LinkedLists (sort)"


def test_merged_list():
    
    my_list1 = LinkedList()
    for i in range(5,10):
        insertFirst(my_list1, i)

    my_list2 = LinkedList()
    for i in range(5):
        insertFirst(my_list2, i)

    mergedList = LinkedList()
    for i in range(10):
        insertFirst(mergedList, i)

    assert mergedList == mergeList(my_list1,my_list2), "Different LinkedLists (merge)"