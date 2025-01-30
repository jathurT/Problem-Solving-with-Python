from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        popped = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top = self.queue1.popleft()
        self.queue2.append(top)
        self.queue1, self.queue2 = self.queue2, self.queue1 # swap the queues
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()