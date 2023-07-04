Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Stack:
...     def __init__(self):
...         self.stack = []
... 
...     def push(self, item):
...         self.stack.append(item)
... 
...     def pop(self):
...         if not self.is_empty():
...             return self.stack.pop()
...         else:
...             print("Stack is empty")
... 
...     def peek(self):
...         if not self.is_empty():
...             return self.stack[-1]
...         else:
...             print("Stack is empty")
... 
...     def is_empty(self):
...         return len(self.stack) == 0
... 
...     def size(self):
...         return len(self.stack)
... 
... 
... # Example usage:
... my_stack = Stack()
... 
... my_stack.push(5)
... my_stack.push(10)
... my_stack.push(15)
... 
... print("Current stack size:", my_stack.size())
... print("Top element:", my_stack.peek())
... 
... popped_item = my_stack.pop()
print("Popped item:", popped_item)

print("Current stack size:", my_stack.size())
print("Is stack empty?", my_stack.is_empty())
