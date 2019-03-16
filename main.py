# main.py
# Author : Phyo Htut
from node import *
from linkedList import *

ll0 = LinkedList(Node('x0'))

ll0.add_back(Node('kappa'))

ll0.add_front(Node('1312'))

ll0.add_back(Node(12))

ll0.printout()

print ''
print ll0.pop_first()
print ''

ll0.printout()

print ''
print ll0.pop_last()
print ''

ll0.printout()

ll0.add_back(Node(132))

ll0.printout()

ll0.del_data('kappa')

ll0.printout()

ll0.add_back(Node('Dan'))
ll0.add_front(Node('Tin'))
ll0.add_back(Node(1.111))

ll0.printout()
