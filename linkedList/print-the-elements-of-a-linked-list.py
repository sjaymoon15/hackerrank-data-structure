def print_list(head):
  current_node = head
  while current_node:
    print(current_node.data)
    current_node = current_node.next