# When you want an attribute of a class to remain the same
# i.e. not allowing reassignment, declare the attribute as a 'property' (a method)

class Dogs:
    def __init__(self, breed):
        self.breed = breed

    @property
    def isCute(self):
        return True


bruno = Dogs('lab')

print(bruno.isCute)
#try to say bruno is not cute
bruno.isCute = False # will give you AttributeError: can't set attribute

