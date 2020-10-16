# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:35:06 2020
@author: João Victor Ribeiro
"""

class ItemList:

    def __init__(self, data=0, next_item=None):
        self.data = data
        self.next = next_item

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)
    
    
class LinkedList:

    def __init__(self):
        self.begin = None

    def __repr__(self):
        return "[" + str(self.begin) + "]"
    
    def __len__(self):
        length = 0
        current = self.begin
        while current.next:
            length += 1
        return length
            

def insertFirst(my_list, new_data):
    new_item = ItemList(new_data)
    new_item.next = my_list.begin
    my_list.begin = new_item
    
    
def insertAfter(my_list, previous_item, new_data):
    assert previous_item, "Previous item need to exists in the list."
    new_item = ItemList(new_data)
    new_item.next = previous_item.next
    previous_item.next = new_item

    
def search(my_list, value):
    current = my_list.begin
    while current and current.data != value:
        current = current.next
    return current
    

def remove(my_list, value):
    assert my_list.begin, "Impossible to remove the value of a empty list."

    if my_list.begin.data == value:
        my_list.begin = my_list.begin.next
    else:
        previous_item = None
        current = my_list.begin
        while current and current.data != value:
            previous_item = current
            current = current.next
        if current:
            previous_item.next = current.next
        else:
            previous_item.next = None
    

def mergeList(list1, list2):
    # your code here
    return False # return the merged list
    

def sortList(my_list):
    # your code here
    return False # return the sorted list
