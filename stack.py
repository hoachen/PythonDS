
class Stack(object):
    """ 用列表实现基本的栈结构"""
    def __init__(self):
        self.items = []

    def push(self, obj):
        self.items.append(obj)

    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        size = self.size()
        return self.items[size -1]


class MyStack(object):
    """ 实现了一个特殊栈,能返回当前栈的最小元素 pop,push get_min 的时间复杂度是O(1)"""
    def __init__(self):
        self.data_stack = Stack()
        self.min_stack = Stack()

    def get_min(self):
        if self.min_stack.is_empty():
            raise Exception('stack is empty')
        return self.min_stack.peek()

    def push(self, obj):
        if self.min_stack.is_empty():
            self.min_stack.push(obj)
        elif obj <= self.get_min():
            self.min_stack.push(obj)
        else:
            self.min_stack.push(self.get_min())
        self.data_stack.push(obj)

    def pop(self):
        self.min_stack.pop()
        return self.data_stack.pop()

    def peek(self):
        return self.data_stack.peek()


class MyQueue(object):
    """ 使用两个栈实现队列的功能 """
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def enqueue(self, obj):
        self.push_stack.push(obj)

    def dequeue(self):
        if self.push_stack.is_empty() and self.pop_stack.is_empty():
            raise Exception('Queue is empty')
        elif self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        return self.pop_stack.peek()


if __name__ == '__main__':
    # s
    # s = MyStack()
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # s.push(1)
    # s.push(2)
    # s.push(1)
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    # print('s.pop:%s s.min: %s' % (s.peek(), s.get_min()))
    # s.pop()
    q = MyQueue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(1)
    print('en dequeue:%s' % (q.dequeue()))
    print('en dequeue:%s' % (q.dequeue()))
    print('en dequeue:%s' % (q.dequeue()))
    print('en dequeue:%s' % (q.dequeue()))
    print('en dequeue:%s' % (q.dequeue()))
    print('en dequeue:%s' % (q.dequeue()))






