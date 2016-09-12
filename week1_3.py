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
for i in range(1, 1+node_cnt):
    node = Node(i)
    nodes.append(node)

min_edge = None
for i in range(edge_cnt):
    node1_number, node2_number, cost = map(int, file_obj.readline().strip().split())
    node1 = nodes[node1_number-1]
    node2 = nodes[node2_number-1]
    edge = Edge(node1, node2, cost)
    if not min_edge:
        min_edge = edge
    else:
        if edge.cost < min_edge.cost:
            min_edge = edge
    node1.edges.append(edge)
    node2.edges.append(edge)

X = {}  # 已经处理过的节点
cost_total = 0
X[min_edge.node1.number] = True
X[min_edge.node2.number] = True
cost_total += min_edge.cost
cross_edges = []
for edge in min_edge.node1.edges:
    has_node1 = edge.node1.number in X
    has_node2 = edge.node2.number in X
    if has_node1 != has_node2:
        cross_edges.append(edge)

for i in range(node_cnt - 2):
    min_edge = None
    for edge in cross_edges:
        if not min_edge:
            min_edge = edge
        else:
            if min_edge.cost > edge.cost:
                min_edge = edge
    X[min_edge.node1.number] = True
    X[min_edge.node2.number] = True
    cross_edges += min_edge.node1.edges
    cross_edges += min_edge.node2.edges
    cost_total += min_edge.cost
    index = 0
    for edge in cross_edges:
        has_node1 = edge.node1.number in X
        has_node2 = edge.node1.number in X
        if has_node1 and has_node2:
            cross_edges.pop(index)
        else:
            pass
        index += 1    
    print(X)
print(X)
print(cost_total)
