from collections import deque
class graph:
    def __init__(self,edges):
        self.edges = edges
        self.dic = {}
        self.q = deque()
        for start,end in self.edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start] = [end]

    def get_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dic:
            return []

        paths = []
        for place in self.dic[start]:
            if place not in path:
                new_paths = self.get_path(place,end,path)
                for i in new_paths:
                    paths.append(i)
        return paths

    def bfs(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if not self.q:
            self.q.append(start)

        while self.q:
            node =self.q.popleft()
            if node not in path:



if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    eg = graph(routes)
    print(eg.get_path('Mumbai', 'New York'))
    print(eg.bfs('Mumbai', 'New York'))


