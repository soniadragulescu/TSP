from City import City


class Repository:
    def __init__(self, filename):
        self.__cities = []
        self.__filename = filename
        self.__no_of_cities=-1
        self.__start=-1
        self.__stop=-1
        self.loadFromFile()

    def loadFromFile(self):
        try:
            f = open("data/" + self.__filename, "r")
        except IOError:
            print("Nu s-a putut deschide fisierul!")

        self.__no_of_cities = int(f.readline())
        i = 0
        for j in range(1,self.__no_of_cities+1):
            line=f.readline()
            city = City(0, [0, 0])
            line = line.strip()
            vector = line.split(",")
            distances = []
            for x in vector:
                distances.append(int(x))
            index = i
            city.setId(index)
            city.setDistances(distances)
            self.__cities.append(city)
            i += 1
        start=int(f.readline())
        stop=int(f.readline())
        self.__start=start
        self.__stop=stop
        for c in self.__cities:
            print(str(c.getId())+" "+str(c.getDistances()))
        print(self.__start)
        print(self.__stop)

    def getAll(self):
        return self.__cities[:]
    def getNoOfCities(self):
        return self.__no_of_cities
    def getDistForCity(self,id):
        for city in self.__cities:
            if city.getId()==id:
                return city.getDistances()
    def getStart(self):
        return self.__start
    def getStop(self):
        return self.__stop