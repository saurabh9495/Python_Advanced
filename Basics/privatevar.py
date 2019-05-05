class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

    __geek = geek

class MapSubClass(Map):
    def geek(self, key, value):         
        for i in zip(keys, values): 
            self.list.append(i) 

___________________________________

def _get_errors(self):
    if self._errors is None:
        self.full_clean

errors = property(_get_errors)

___________________________________

def Geek:
    def _single_method(self):
        pass
    def __double_method(self):
        pass

class Pyth(Geek):
    def __double_method(self):
        pass

___________________________________

class Geek:
    def __init__(self,ab):
        self.ab = ab
    def __custom__(self):
        pass