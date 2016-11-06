#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-05 17:09:33


class Node(object):
    """ 节点对象 """

    def __init__(self, number):
        self.number = number
        self.edges = []
        self.parent = None


class Edge(object):
    """ 链接对象 """

    def __init__(self, number, node1, node2, weight):
        self.number = number  # 链接的id
        self.node1 = node1
        self.node2 = node2
        self.weight = weight  # 链接的长度


class Clustering(object):

    def __init__(self):
        self.input = open('data/clustering1.txt', 'r')
        self.node_cnt = int(self.input.readline())
        self.nodes = []
        self.edges = []
        self.edge_cnt = 0
        for line in self.input.readlines():
            node_cnt = int(
