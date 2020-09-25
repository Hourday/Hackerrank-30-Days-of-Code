class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum=[]
        self.maximumDifference=0

    # Add your code here

    def computeDifference(self):
        for y in range(len(self.__elements)):
            for x in range(len(self.__elements)):
                b=self.__elements[y]-self.__elements[x]
                self.maximum.append(abs(b))
        self.maximumDifference=max(self.maximum)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)