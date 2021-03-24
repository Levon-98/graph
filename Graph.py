from typing import Union


class Edge:
    def __init__(self, vertex_1: int, vertex_2: int, weight: int = 0):
        self.edge = tuple(sorted([vertex_1, vertex_2]))

        self.weight = weight

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class Nodes:
    def __init__(self, vertex: int):
        self.vertex = vertex

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return f"Nodes({self.vertex})"


class Graph:
    def __init__(self, *nodes: Union[Nodes, Edge]):
        self.nodes = nodes
        self.Edge_dict = {}
        self.Vertex_dict = {}

        for i in nodes:
            if isinstance(i, Edge):
                self.Edge_dict[f"{i.edge}"] = i.weight
            elif isinstance(i, Nodes):
                self.Vertex_dict[i.vertex] = i
            else:
                raise TypeError(f"excepted type Node or Edge {type(i)} found")

        self.Neighbours_dict = self.__neighbours_dict_1()

    def __str__(self):
        return str(self.__dict__)

    def __contains__(self, item: object):
        if not isinstance(item, Graph):
            raise TypeError("item  is not Graph")

        if set(item.Vertex_dict).issubset(set(self.Vertex_dict)) and set(
            item.Edge_dict
        ).issubset(set(self.Edge_dict)):
            return True
        return False

    def __neighbours_dict_1(self):
        neighbor_dict = {vertex: [] for vertex in self.Vertex_dict}
        for edge in self.Edge_dict:
            edge = eval(edge)
            if edge[0] in neighbor_dict:
                neighbor_dict[edge[0]].append(edge[1])
            if edge[1] in neighbor_dict:
                neighbor_dict[edge[1]].append(edge[0])
        return neighbor_dict

    def add_vortex(self, i: int):
        i_node = Nodes(i)
        self.Vertex_dict[i_node.vertex] = i_node
        self.Neighbours_dict = self.__neighbours_dict_1()

    def add_edge(self, vertex_1: int, vertex_2: int, weight: int = 0):
        new_edge = Edge(vertex_1, vertex_2, weight)
        self.Edge_dict[f"{new_edge.edge}"] = new_edge.weight
        self.Neighbours_dict = self.__neighbours_dict_1()

    def delete_vertex(self, node: Nodes):
        del self.Vertex_dict[node.vertex]
        for i in self.nodes:
            if isinstance(i, Edge):
                if node.vertex in i.edge:
                    del self.Edge_dict[f"{i.edge}"]
            if isinstance(i, Nodes):
                if i.vertex != node.vertex:
                    self.Vertex_dict[i.vertex] = i

        self.Neighbours_dict = self.__neighbours_dict_1()


if __name__ == "__main__":
    pass
    edge = Edge(1, 2)
    edge_1 = Edge(1, 3, 1)
    k = Edge(2, 1)
    node = Nodes(1)
    node_1 = Nodes(2)
    node_3 = Nodes(3)
    node_4 = Nodes(4)
    graph = Graph(edge, edge_1, node, node_1, node_3, node_4, k)
    graph_1 = Graph(edge, edge_1, node, node_1, node_4)
    print(graph_1 in graph)
    print(graph.Edge_dict)
    print(graph.Vertex_dict)
    print(graph.Neighbours_dict)
    graph.delete_vertex(node_3)
    print(graph.Edge_dict)
    graph.add_vortex(5)
    graph.add_edge(2, 8, 14)
