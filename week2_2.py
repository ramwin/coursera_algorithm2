#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-12 21:42:30

import pdb


class Node(object):
    " 每个节点 "

    def __init__(self, code, length):
        self.code = code
        self.length = length
        self.parent = None
        self.depth = 0

    @property
    def ancestor(self):
        if self.parent is None:
            return self
        else:
            return self.parent.ancestor

    def set_parent(self, node):
        if self.code == node.code:
            raise ValueError("不要把node的parent设置成自己")
        if self.parent:
            raise ValueError("不要设置已经有了parent的node")
        else:
            self.parent = node

    def __str__(self):
        return self.code


class Clustering(object):

    def __init__(self):
        self.input = open("data/clustering_big.txt", "r")
        # self.input = open("data/test.txt", "r")
        self.node_cnt, self.node_length = map(int, self.input.readline().split(" "))
        self.node_set = set()  # 用来存储是否出现过节点
        self.nodes = {}
        self.group = set()
        index = 0
        for line in self.input.readlines():
            index += 1
            if index % 10000 == 0:
                print("已经处理了%d条数据" % index)
                print(len(self.group))
            new_group = True
            code = line.replace(" ", "").strip()
            if code in self.node_set:
                new_group = False
                continue
            node = Node(code, int(self.node_length))
            for i in range(self.node_length):
                close_node = code[0:i] + ("1" if code[i] == "0" else "0") + \
                             code[i+1:self.node_length]
                if close_node in self.node_set:
                    new_group = False
                    if not node.parent:  # 第一次找到组
                        node.set_parent(self.nodes[close_node].ancestor)
                    else:  # 第二次找到组
                        if self.nodes[close_node].ancestor == node.ancestor:
                            pass  # 如果还在一个组，就不要操作
                        else:  # 如果不在一个组，就把两个组进行合并
                            if node.ancestor.depth < self.nodes[close_node].ancestor.depth:
                                self.group.remove(node.ancestor)
                                node.ancestor.set_parent(self.nodes[close_node].ancestor)
                            elif node.ancestor.depth > self.nodes[close_node].ancestor.depth:
                                self.group.remove(self.nodes[close_node].ancestor)
                                self.nodes[close_node].ancestor.set_parent(node.ancestor)
                            else:
                                self.group.remove(node.ancestor)
                                node.ancestor.set_parent(self.nodes[close_node].ancestor)
                                node.ancestor.depth += 1
                for j in range(i+1, self.node_length):
                    close_node_2 = close_node[0:j] + \
                        ("1" if close_node[j] == "0" else "0") + \
                        close_node[j+1:self.node_length]
                    if close_node_2 in self.node_set:
                        new_group = False
                        if not node.parent:  # 第一次找到组
                            node.set_parent(self.nodes[close_node_2].ancestor)
                        else:  # 第二次找到组。需要把两个组合并
                            if self.nodes[close_node_2].ancestor == node.ancestor:
                                pass
                            else:
                                if node.ancestor.depth < self.nodes[close_node_2].ancestor.depth:
                                    self.group.remove(node.ancestor)
                                    node.ancestor.set_parent(self.nodes[close_node_2].ancestor)
                                elif node.ancestor.depth > self.nodes[close_node_2].ancestor.depth:
                                    self.group.remove(self.nodes[close_node_2].ancestor)
                                    self.nodes[close_node_2].ancestor.set_parent(node.ancestor)
                                else:
                                    self.group.remove(node.ancestor)
                                    node.ancestor.set_parent(self.nodes[close_node_2].ancestor)
                                    node.ancestor.depth += 1
            if new_group is True:
                self.group.add(node)
            self.node_set.add(code)
            self.nodes[code] = node


if __name__ == '__main__':
    answer = Clustering()
    print(len(answer.group))
