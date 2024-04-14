class EuclideanAlgorithm:
    def euclidean_algorithm(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    



    
euclidean = EuclideanAlgorithm()
print(euclidean.euclidean_algorithm(1785,546))