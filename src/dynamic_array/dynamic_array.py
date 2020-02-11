class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # todo: increase size
            print("Error: Array is full")

        if index >= self.count:
            # Better error Handling
            print("Error out of bounds")

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i -1]

        self.storage[index] = value
        self.count += 1


    def append(self, value):
        if self.count == self.capacity:
            # todo: increase size
            print("Error: Array is full")
        
        self.storage[self.count] = value
        self.count += 1 

    def double_size(self):
        self.capacity #= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage

        self.storage = new_storage



        