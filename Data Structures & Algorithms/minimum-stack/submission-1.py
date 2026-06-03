class MinStack:

    def __init__(self):
        self.dq=collections.deque()

    def push(self, val: int) -> None:
        self.dq.append(val)

    def pop(self) -> None:
        return self.dq.pop()

    def top(self) -> int:
        return self.dq[-1]

    def getMin(self) -> int:
        return min(self.dq)
