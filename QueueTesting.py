from Queue import QueueImpl
class TestingQueue:
    q = QueueImpl(30)

    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.print()
    q.deQueue()
    q.deQueue()
    q.print()
    print(q.isFull())

