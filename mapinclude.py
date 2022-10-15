def load_map(mapname):
    with open(mapname, 'r') as mapfile:
        startpos = list(map(float, mapfile.readline().split()))
        filemap = mapfile.readlines()
        gamemap = []
        for line in filemap:
            line = line.split()
            gamemap.append(line)
        return startpos, gamemap


def load_maplist():
    with open("maplist.cfg", 'r') as maplist:
        return maplist.readline().split()
