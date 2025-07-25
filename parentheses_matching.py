# -*- coding: utf-8 -*-
"""Parentheses Matching.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uBUjkKMW3NHJ8qnUk0CH6umDaAwzZ5Vb
"""

def is_balanced(expr):
    stack = []
    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if not ((top == '(' and char == ')') or
                    (top == '[' and char == ']') or
                    (top == '{' and char == '}')):
                return False
    return len(stack) == 0

print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False