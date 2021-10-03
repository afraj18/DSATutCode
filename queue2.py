from queue import Queue
import time
import threading

q = Queue()


def place(food):
    for i in food:
        q.enqueue(i)
        print("Order Placed : ", i)
        time.sleep(0.5)


index = 0


def serve():
    time.sleep(1)
    while not q.isEmpty():
        print("Order Served : ", q.dequeue())
        time.sleep(2)


t = time.time()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

# place(orders)
# serve()

t1 = threading.Thread(target=place(orders))
t2 = threading.Thread(target=serve)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in : ", time.time() - t)
