
from tkinter import Listbox


class ArrayList :
    def __init__(self) :
        self.items=[]
    def insert(self,pos,elem) :
        self.items.insert(pos,elem)
    def delete(self,pos) :
        self.items.pop(pos)
    def isEmpty(self) :
        return self.size() == 0
    def size(self) :
        return len(self.items)
    def getEntry(self, pos) :
        return self.items[pos]
    def clear(self) :
        self.items = []
    def replace(self,pos,elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def display(self,msg = 'ArrayList:') :
        print(msg,self.size(),self.items)
    def merge(self,lst) : 
        self.items.extend(lst)
    def findMaxMin(self) :
        min = self.items[0]
        max = self.items[0]
        for i in range(1, self.size()) :
            if min > self.items[i]: 
                min = self.items[i]
            if max < self.items[i] : 
                max = self.items[i]
        return (min,max)
    def isEqual(self, list):
        for i in range(len(self.items)):
            for j in range(len(list.items)):
                if list.items[j] == self.items[i] : return True
        return False  
    def union(self, listB):
        C = ArrayList()
        C = self.items + listB.items
        return C

A = ArrayList()
B = ArrayList()
A.insert(0,20)
A.insert(1,10)
A.insert(2,30)
A.display()
B.insert(0,35)
B.insert(1,50)
B.insert(2,40)
B.display()
print(A.union(B))
print(A.isEqual(B))
