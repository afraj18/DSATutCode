from collections import deque

queue = deque()

for i in range(0,10):
    queue.append(i)
    print(queue)

for i in range(len(queue)):
    queue.popleft()
    print(queue)