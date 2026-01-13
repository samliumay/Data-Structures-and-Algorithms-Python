
class cookie:
    def __init__(self, flavor, shape, size):
        self.flavor = flavor
        self.shape = shape
        self.size = size

    def describe(self):
        print(
            f"This cookie is {self.size} sized, {self.shape} shaped and has a {self.flavor} flavor."
        )
    
    def setFlavor(self, flavor):
        self.flavor = flavor
    
    def setShape(self, shape):
        self.shape = shape

    def setSize(self, size):
        self.size = size

    def getFlavor(self):   
        return self.flavor
    def getShape(self):
        return self.shape
    def getSize(self):
        return self.size