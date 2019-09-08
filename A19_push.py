# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minstack or node<=self.minstack[-1]:
            self.minstack.append(node)
        else:
            self.minstack.append(self.minstack[-1])   #很好解决当最小值出栈的问题!!!!!
    def pop(self):
        # write code here
        if not self.stack:
            self.stack.pop()
        self.minstack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]