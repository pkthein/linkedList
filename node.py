# node.py
# Author : Phyo Htut
class Node:
  
  def __init__(self, d = 0, n = None, p = None):
    self.data = d
    self.nex = n
    self.pre = p
    
  def set_data(self, d):
    self.data = d
  
  def set_next(self, n):
    self.nex = n
    
  def set_pre(self, p):
    self.pre = p
    
  def get_data(self):
    return self.data
    
  def get_next(self):
    return self.nex
    
  def get_prev(self):
    return self.pre
