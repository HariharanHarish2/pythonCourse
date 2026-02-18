class Math:
    def add(self, a, b, c=0):
        return a + b + c

obj = Math()
print(obj.add(2, 3))      # Output: 5
print(obj.add(2, 3, 4))   # Output: 9
