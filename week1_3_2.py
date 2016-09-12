#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-12 19:56:17

import heapq
import pdb


file_path = "data/edges.txt"


class Node(object):
    def __init__(self, number):
        self.number = number
        self.edges = []

    def __str__(self):
        return self.number


class Edge(object):

    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

    @classmethod
    def create_from_line(cls, line):
        node1, node2, cost = map(int, line.strip().split())
        return cls(node1, node2, cost)


file_obj = open(file_path, 'r')
node_cnt, edge_cnt = map(int, file_obj.readline().strip().split())
nodes = []
edges = []
min_edge = None
for i in range(1, 1+node_cnt):
    node1_number, node2_number, cost = map(int, file_obj.readline().strip().split())
    edges.append(Edge(node1_number, node2_number, cost))
    if not min_edge:
        min_edge = Edge(node1_number, node2_number, cost)
    else:
        if min_edge.cost > cost:
            min_edge = Edge(node1_number, node2_number, cost)


X = {}
costs = 0

# 预处理
X[min_edge.node1] = True
X[min_edge.node2] = True
costs = min_edge.cost
min_edge = None
for i in range(node_cnt-2):
    for edge in edges:
        a = edge.node1 in X
        b = edge.node2 in X
        if a!=b:  # 属于交叉edge
            if min_edge is None:
                min_edge = edge
            else:
                if min_edge.cost > edge.cost:
                    min_edge = edge
    costs += min_edge.cost
    X[min_edge.node1] = True
    X[min_edge.node2] = True
    print(costs)
print(costs)
