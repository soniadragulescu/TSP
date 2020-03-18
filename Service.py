class Service:
    def __init__(self, repository):
        self.__repository = repository

    def stillVisit(self, start, stop, visited):
        if (visited.count(0)) > 0:
            return True
        return False

    def notReached(self, start, stop, visited):
        if start == stop:
            return False
        return True

    def shortestPath(self, functie):
        visited = [0] * self.__repository.getNoOfCities()
        start = self.__repository.getStart() - 1
        now = start
        stop = self.__repository.getStop() - 1
        sumOfDistances=0
        if functie==self.stillVisit:
            start=0
            now=0
        visited[start] = 1
        path = []
        path.append(start + 1)
        while functie(now, stop, visited):
            startDistances = self.__repository.getDistForCity(now)
            min = 999999
            id = -1
            for i in range(0, len(startDistances)):
                next = self.__repository.getDistForCity(i)[stop]
                if functie == self.stillVisit:
                    next = 0
                if startDistances[i]+next < min and startDistances[i] != 0 and visited[i] != 1 :
                    id = i
                    min = startDistances[i]+next
            path.append(id + 1)
            sumOfDistances+=startDistances[id]
            visited[id] = 1
            now = id
        if functie==self.stillVisit:
            sumOfDistances+=self.__repository.getDistForCity(now)[start]
        return path,sumOfDistances
