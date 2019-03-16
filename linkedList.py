# linkedList.py
# Author : Phyo Htut
from node import *

class LinkedList:
  
  def __init__(self, n0 = None):
    self.length = 0
    self.head = Node('__head__')
    self.tail = Node('__tail__')
    if n0 != None:
      self.head.nex = n0
      n0.pre = self.head
      n0.nex = self.tail
      self.tail.pre = n0
      
      self.length = self.length + 1
    else:
      self.head.nex = self.tail
      self.tail.pre = self.head
  
  def add_front(self, n0):
    if self.length == 0:
      self.head.nex = n0
      n0.pre = self.head
      n0.nex = self.tail
      self.tail.pre = n0
    else:
      tmp = self.head.nex
      # order of operation here is really important
      tmp.pre = n0
      n0.nex = tmp
      n0.pre = self.head
      self.head.nex = n0
      
    self.length = self.length + 1
    
  def add_back(self, n0):
    if self.length == 0:
      self.head.nex = n0
      n0.pre = self.head
      n0.nex = self.tail
      self.tail.pre = n0
    else:
      tmp = self.tail.pre
      # order of operation here is really important
      tmp.nex = n0
      n0.pre = tmp
      n0.nex = self.tail
      self.tail.pre = n0
    
    self.length = self.length + 1
    
  def get_first(self):
    return self.head.nex
  
  def get_last(self):
    return self.tail.pre
    
  def get_length(self):
    return self.length
  
  def pop_first(self):
    if self.length == 0:
      return 'LinkedList is empty!'
    else:
      self.length = self.length - 1
      
      pop = self.head.nex
      new_first = self.head.nex.nex
      
      self.head.nex = new_first
      new_first.pre = self.head
      
      pop.nex = None
      pop.pre = None
      
      return pop.data
    
  
  def pop_last(self):
    if self.length == 0:
      return 'This LinkedList is empty!'
    else:
      self.length = self.length - 1
      
      pop = self.tail.pre
      new_last = self.tail.pre.pre
      
      self.tail.pre = new_last
      new_last.nex = self.tail
      
      pop.pre = None
      pop.nex = None
      
      return pop.data
      
  def del_data(self, d):
    if d == '__head__' or d == '__tail__':
      print 'You may not delete the reference node!'
      return False
    else:
      tmp = self.head.nex
      data_found = False
      while str(tmp.data) != '__tail__':
        if str(tmp.data) == d:
          data_found = True
          break
        tmp = tmp.nex
      if data_found == True:
        self.length = self.length - 1
        
        prev_node = tmp.pre
        next_node = tmp.nex
        
        prev_node.nex = next_node
        next_node.pre = prev_node
        
        tmp.pre = None
        tmp.nex = None
        
        return True
      else:
        return False
      
    
  def printout(self):
    print '\nLength of this LinkedList is: ' + str(self.length) + '\n'
    
    print 'Data in this LinkedList are as follow: '
    tmp = self.head.nex
    while str(tmp.data) != '__tail__':
      print tmp.data
      tmp = tmp.nex
      
  
