class Node:
  def __init__(self, n, next):
    self.value = n
    self.nextNode = next
  def setNext(self, next):
    self.nextNode = next
  def setVal(self, val):
    self.value = val
  def getNext(self):
    return self.nextNode
  def getVal(self):
    return self.value

class LinkedList:
  def __init__(self):
    self.firstNode = None
    self.lastNode = None
    self.len = 0
    
  def append(self, int):
    n = Node(int, None)
    if self.lastNode is None:
      self.firstNode = n
    else:
      self.lastNode.setNext(n)
    self.lastNode = n
    self.len+=1
    
  def prepend(self, int):
    n = Node(int, self.firstNode)
    if self.firstNode is None:
      self.lastNode = n
    self.firstNode = n
    self.len+=1
    
  
  def deleteFirst(self):
    if self.firstNode is not None:
      first = self.firstNode
      self.firstNode = first.nextNode
      self.len-=1
      if self.firstNode is None:
        self.lastNode = None
    else:
      print(" Error 1: No items in linked list cannot delete items")

  
  def printContents(self):
    n = self.firstNode
    print('[\n')
    while n is not None:
      print(str(n.value)+",\n ")
      n = n.nextNode
    print(']')

  
  def printNthItem(self , n):
 
    if n<=self.len-1 and n>=0:
      node = self.firstNode
      i = 0
      while i is not n:
        assert node is not None
        node = node.nextNode
        i+=1
      assert node is not None
      print(node.value)
    else:
      print("Error 2: Nothing to delete")

  
  def deleteLast(self):
    if self.firstNode is None:
      print("Error 2: Nothing to delete")
    elif self.len == 1:
      self.firstNode=None
      self.lastNode=None
      self.len = 0
      pass
    else:
      node = self.firstNode
      i = 0
      while i is not self.len-2:
        assert node is not None
        node = node.nextNode
        i+=1
      assert node is not None
      node.setNext(None)
      node = self.lastNode
      self.len-=1
    
    

  def deleteNthItem(self, n):
    if n<=self.len-1 and n>=0:
      if n != 0 and n is not self.len-1:
        node = self.firstNode
        i = 0
        while i is not n-1:
          assert node is not None
          node = node.nextNode
          i+=1
        assert node is not None
        assert node.nextNode is not None
        node.nextNode = node.nextNode.nextNode
      elif n == 0:
        self.deleteFirst()
      else:
        self.deleteLast()
      self.len-=1
    else:
      print("Error 2: Nothing to delete")

  def insertItem(self, i, n):
    if i != 0 and i != self.len and self.len != 0:
      node = self.firstNode
      ind = 0
      while ind != i-1:
        assert node is not None
        node = node.nextNode
        ind+=1
      assert node is not None
      newNode = Node(n, node.nextNode)
      node.setNext(newNode)
    elif i == 0:
      self.prepend(n)
    elif i == self.len:
      self.append(n)
    else:
      node = Node(n,None)
      node = self.firstNode
      node = self.lastNode
    self.len+=1

  def switchValues(self, i1, i2):
    pass
  def reverse(self):
    pass
    
myList = LinkedList()
myList.append(5)
myList.prepend(3)
myList.append(0)
myList.append(5)
myList.printContents()
myList.insertItem(0,7)
myList.printContents()



    