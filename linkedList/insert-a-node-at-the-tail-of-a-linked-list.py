def Insert(head, data):
  if not head:
    head = Node(data)
    return head
  
  current_node = head
  while current_node.next:
    current_node = current_node.next
    
  current_node.next = Node(data)
  return head