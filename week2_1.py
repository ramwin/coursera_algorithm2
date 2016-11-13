#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-05 17:09:33

import heapq


class Node(object):
    " number 从 0 到 499 "

    def __init__(self, number):
        self.number = number
        self.edges = []
        self.parent = None
        self.depth = 0

    @property
    def ancestor(self):
        if self.parent is None:
            return self
        else:
            return self.parent.ancestor


class Edge(object):

    def __init__(self, number, node1, node2, weight):
        self.number = number  # 链接的id
        self.node1 = node1
        self.node2 = node2
        self.weight = weight  # 链接的长度

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight


class Clustering(object):

    def __init__(self):
        self.input = open('data/clustering1.txt', 'r')
        # self.input = open('data/test.txt', 'r')
        self.node_cnt = int(self.input.readline())
        self.nodes = []
        self.edges = []
        self.edge_cnt = 0
        self.block = self.node_cnt
        for node_number in range(self.node_cnt):
            node = Node(number=node_number)
            self.nodes.append(node)
        edge_number = 0
        for line in self.input.readlines():
            node1_number, node2_number, edge_length = map(int, line.split(' '))
            node1 = self.nodes[node1_number-1]
            node2 = self.nodes[node2_number-1]
            edge = Edge(number=edge_number, node1=node1, node2=node2, weight=edge_length)
            node1.edges.append(edge)
            node2.edges.append(edge)
            heapq.heappush(self.edges, edge)

    def get_shortest_edge(self):
        edge = heapq.heappop(self.edges)
        return edge

    def merge(self):
        """ 合并最靠近的2个block """
        edge = self.get_shortest_edge()
        if edge.node1.ancestor == edge.node2.ancestor:
            self.merge()
        else:
            if edge.node1.ancestor.depth > edge.node2.ancestor.depth:
                edge.node2.ancestor.parent = edge.node1.ancestor
            else:
                edge.node1.ancestor.parent = edge.node2.ancestor
            self.block -= 1

    def get_space(self):
        """ 获取当前最靠近的block的距离 """
        edge = self.edges[0]
        if edge.node1.ancestor == edge.node2.ancestor:
            heapq.heappop(self.edges)
            return self.get_space()
        else:
            return edge.weight


if __name__ == '__main__':
    answer = Clustering()
    while answer.block > 4:
        answer.merge()
    print(answer.get_space())
