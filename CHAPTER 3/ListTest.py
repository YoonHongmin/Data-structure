items = []
def insert(pos,elem) :
    items.insert(pos,elem)
def delete(pos) :
    items.pop(pos)
def isEmpty() :
    return size() == 0
def size() :
    return len(items)
def getEntry(pos) :
    return items[pos]
def clear() :
    #global items
    items = []
def replace(pos,elem) :
    items[pos] = elem
def sort() :
    items.sort()
def display(msg = 'ArrayList:') :
    print(msg,size(),items)
def merge(lst) : items.extend(lst)

insert(0,10)
insert(1,20)
insert(0,30)
insert(2,40)
insert(size(),50)
insert(1,60)
replace(2,70)
delete(2)
print(items)