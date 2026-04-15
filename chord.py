import hashlib

def sha1_id(key, m):
    return int(hashlib.sha1(key.encode()).hexdigest(),16)%(2**m)

class Node:
    def __init__(self,id,m):
        self.id=id
        self.m=m
        self.successor=self
        self.predecessor=None
        self.finger=[self]*m

    def in_interval(self,target,start,end,inclusive=False):
        if start<end:
            return start<target<=end if inclusive else start<target<end
        return target>start or target<end

    def find_successor(self,key):
        node=self
        visited=set()

        while True:
            if node.id in visited:
                return node
            visited.add(node.id)

            if node.in_interval(key,node.id,node.successor.id,True):
                return node.successor

            nxt=node.closest_preceding_node(key)
            if nxt==node:
                return node.successor
            node=nxt

    def closest_preceding_node(self,key):
        for i in reversed(range(self.m)):
            f=self.finger[i]
            if f and self.in_interval(f.id,self.id,key):
                return f
        return self

    def fix_fingers(self):
        for i in range(self.m):
            start=(self.id+2**i)%(2**self.m)
            self.finger[i]=self.find_successor(start)

class ChordRing:
    def __init__(self,m=6):
        self.m=m
        self.nodes={}

    def add_node(self,id):
        node=Node(id,self.m)

        if not self.nodes:
            node.successor=node
            node.predecessor=node
            self.nodes[id]=node
            return

        any_node=next(iter(self.nodes.values()))
        succ=any_node.find_successor(id)

        node.successor=succ
        node.predecessor=succ.predecessor

        succ.predecessor.successor=node
        succ.predecessor=node

        self.nodes[id]=node

        for n in self.nodes.values():
            n.fix_fingers()

    def get_nodes(self):
        return sorted(self.nodes.keys())