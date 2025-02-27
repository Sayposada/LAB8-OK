class Monticulo:
    def __init__(self, array=None):
        if array is None:
            self.A = []
            self.heap_size = 0
        else:
            self.A = array
            self.heap_size = len(array)
            self.construir_monticulo()

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def construir_monticulo(self):
        n = self.heap_size // 2
        for i in range(n, -1, -1):
            self.max_heapify(i)

class Colaprioritaria(Monticulo):
    def max_heap_insert(self, k):
        self.heap_size += 1
        self.A.append(k)
        i = self.heap_size - 1
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            self.A[self.parent(i)], self.A[i] = self.A[i], self.A[self.parent(i)]
            i = self.parent(i)

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise ValueError("heap underflow")
        max_val = self.A[0]
        self.A[0] = self