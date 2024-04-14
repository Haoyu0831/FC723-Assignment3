class EuclideanAlgorithm:
    def euclidean_algorithm(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def get_input(self):
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        return self.euclidean_algorithm(a,b)


    
euclidean = EuclideanAlgorithm()
print(euclidean.get_input())
