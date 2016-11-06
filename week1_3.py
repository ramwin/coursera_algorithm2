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
node_dict = {}  # 所有的node

for i in range(1, 1+node_cnt):
    node_dict[i] = Node(i)

X_dict = {}
edges = []

for _ in range(edge_cnt):
    edge = Edge.create_from_line(file_obj.readline())
    edges.append(edge)
    node_dict[edge.node1].edges.append(edge)
    node_dict[edge.node2].edges.append(edge)

def get_min_edge():
    if not X_dict:
        min_edge = edges[0]
        for edge in edges:
            if edge.cost < min_edge.cost:
                min_edge = edge
    elif X_dict:
        min_edge = None
        for edge in edges:
            if (edge.node1 in X_dict) != (edge.node2 in X_dict):
                if min_edge is None:
                    min_edge = edge
                else:
                    if edge.cost < min_edge.cost:
                        min_edge = edge
    return min_edge


total_cost = 0
for i in range(node_cnt - 1):
    min_edge = get_min_edge()
    total_cost += min_edge.cost
    X_dict[min_edge.node1] = True
    X_dict[min_edge.node2] = True
print(total_cost)
