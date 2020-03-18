
class City:
    def __init__(self,id,distances):
        self.__id=id
        self.__distances=distances

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def setDistances(self,distances):
        self.__distances=distances

    def getDistances(self):
        return self.__distances[:]
