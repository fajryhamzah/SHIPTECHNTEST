class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next


def get_mid_node(input_len, head):
	if input_len < 1 or head is None:
		return None
		
	if input_len%2 == 0:
		mid = (input_len//2)+1
	else:
		mid = -(-input_len//2)
	i = 1

	while i != mid:
		head = head.next
		i += 1

	return head.value 

def generate_linklist(input_list):
	head = None
	prev = None
	for i in input_list:
		node = Node(i,None)

		if not head:
			head = node

		if prev:
			prev.next = node

		prev = node

	return head


if __name__ == '__main__':
	input_len = int(input())
	input_list = input().split(' ')
	
	if input_len != len(input_list):
		raise Exception('Input overflow')

	head = generate_linklist(input_list)

	print(get_mid_node(input_len,head))