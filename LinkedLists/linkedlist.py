class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None


class SLinkedList:
   def __init__(self):
      self.head = None  # First node in singly linked list.

   def listprint(self):
      node = self.head

      # Iterating through linked list till node.next is None.
      while node is not None:
         print (node.value)
         node = node.next


# Keep track of passed values with array(buffer), then delete node 
# if found before
def eliminate_duplicate_v1(sLinkedList):
   node = sLinkedList.head
   lastNode = None
   found = []

   while node is not None:
      if node.value in found:
         lastNode.next = node.next
      else:
         found.append(node.value)
         lastNode = node
         
      node = node.next

   sLinkedList.listprint()




if __name__ == "__main__":
    import random

    linkedlist = SLinkedList()
    linkedlist.head = Node(1)
   
    node = linkedlist.head

    # Populating linked list with 20 random value nodes. 
    for i in range(2,20):
      temp = Node(random.randint(1, 10))
      node.next = temp
      node = temp


    linkedlist.listprint()
    print("----")

    eliminate_duplicate_v1(linkedlist)
