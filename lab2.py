from Repository import Repository
from Service import Service

#print("Fisier input:")
filename="easy.txt"
repo=Repository(filename)
filename_output="hard_01_tsp_solution.txt"
service=Service(repo)
f=open(filename_output,'w')
f.write(str(repo.getNoOfCities())+'\n')
path,dist=service.shortestPath(service.stillVisit)
i=0
for x in path:
    f.write(str(x))
    i+=1
    if i<len(path):
        f.write(',')
f.write('\n')
f.write(str(dist)+'\n')
path2,dist2=service.shortestPath(service.notReached)
i=0
f.write(str(len(path2)))
f.write('\n')
for x in path2:
    f.write(str(x))
    i+=1
    if i<len(path2):
        f.write(',')
f.write('\n')
f.write(str(dist2))
f.close()