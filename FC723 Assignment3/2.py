class EuclideanAlgorithm:

    def euclidean_algorithm(self, a, b):
        # the function takes two integers, a and b, and find their greatest common divisor

        # while loop continues as long as b is not zero
        while b != 0:
            a, b = b, a % b

        # when b is zero, the current value is the greatest commmon divisor of a and b
        return a
    



    
euclidean = EuclideanAlgorithm()
print(euclidean.euclidean_algorithm(1785,546))