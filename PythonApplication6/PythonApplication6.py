from graphviz import Digraph
import time

white = True
red = False


class Node:
    def __init__(self, val):
        self.color = red
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class RWtree:
    def __init__(self, val):
        self.root = Node(val)
        self.root.color = white
        
    def insert(self, val):
        new = Node(val)
        parent = self.root
        while (val >= parent.val and parent.right) or (val < parent.val and parent.left):
            if val >= parent.val:
                parent = parent.right
            else:
                parent = parent.left
        new.parent = parent
        if val >= parent.val:
            parent.right = new
        else:
            parent.left = new
        if parent.color == white:
            return None
        else:
            while parent != self.root and parent.color != white:
            
                ded = parent.parent
                if ded.right and ded.left and ded.right.color == ded.left.color == red:
                    ded.color = red
                    ded.right.color = white
                    ded.left.color = white
                    if ded == self.root:
                        ded.color = white
                        return None
#
                    parent = ded.parent
                    new = ded
                    graph = visualize_tree(root.root)
                    graph.render(filename='rbtree3', format='png', cleanup=True)

                
                elif ded.left == parent:
                    if parent.right == new:
                        ded.left = new
                        parent.right = new.left
                        new.left = parent
                        parent.parent = new
                        new.parent = ded
                        if parent.right:
                            parent.right.parent = parent
                        parent, new = new, parent
                        graph = visualize_tree(root.root)
                        graph.render(filename='rbtree3', format='png', cleanup=True)
                    if ded == self.root:
                        self.root = parent
                    if parent.right:
                        parent.right.parent = ded
                    ded.left = parent.right
                    parent.right = ded
                    parent.parent = ded.parent
                    if ded.parent:
                        if ded.parent.left == ded:
                            ded.parent.left = parent
                        else:
                            ded.parent.right = parent
                    ded.parent = parent
                    parent.color = white
                    ded.color = red
                    graph = visualize_tree(root.root)
                    graph.render(filename='rbtree3', format='png', cleanup=True)
                    return None
                else:
                    if parent.left == new:
                        ded.right = new
                        parent.left = new.right
                        new.right = parent
                        parent.parent = new
                        new.parent = ded
                        if parent.left:
                            parent.left.parent = parent
                        parent, new = new, parent
                        graph = visualize_tree(root.root)
                        graph.render(filename='rbtree3', format='png', cleanup=True)
                    if ded == self.root:
                        self.root = parent
                    if parent.left:
                        parent.left.parent = ded
                    ded.right = parent.left
                    parent.left = ded
                    parent.parent = ded.parent
                    if ded.parent:
                        if ded.parent.right == ded:
                            ded.parent.right = parent
                        else:
                            ded.parent.left = parent
                    ded.parent = parent
                    parent.color = white
                    ded.color = red
                    graph = visualize_tree(root.root)
                    graph.render(filename='rbtree3', format='png', cleanup=True)
                    return None


def visualize_tree(node, graph=None):
    if graph is None:
        graph = Digraph('Tree', node_attr={'style': 'filled', 'fillcolor': 'lightgray'})

    if node:
        graph.node(str(node.val), color=("red" if  not node.color else "white"))
        if node.left:
            graph.edge(str(node.val), str(node.left.val))
            visualize_tree(node.left, graph)
        if node.right:
            graph.edge(str(node.val), str(node.right.val))
            visualize_tree(node.right, graph)

    return graph

# Example usage:
root = RWtree(1)

root.insert(437)
root.insert(244)
root.insert(1379)
root.insert(959)
root.insert(261)
root.insert(162)
root.insert(38)
root.insert(119)
root.insert(444)
root.insert(1637)
root.insert(1034)
root.insert(778)
root.insert(1480)
graph = visualize_tree(root.root)
graph.render(filename='rbtree3', format='png', cleanup=True)
root.insert(289)
root.insert(661)
root.insert(1545)
root.insert(1408)
root.insert(1179)
root.insert(1375)
root.insert(144)
root.insert(1828)
root.insert(473)
root.insert(325)
root.insert(1953)
root.insert(1522)
root.insert(1392)
root.insert(1788)
root.insert(1016)
root.insert(1683)
root.insert(1085)
root.insert(1366)
root.insert(546)
root.insert(765)
root.insert(1231)
root.insert(1564)
root.insert(174)
root.insert(1317)
root.insert(1288)
root.insert(702)
root.insert(1987)
root.insert(1893)
root.insert(1423)
root.insert(288)
root.insert(1463)
root.insert(1138)
root.insert(974)
root.insert(1986)
root.insert(601)
root.insert(1503)
root.insert(678)
root.insert(813)
root.insert(86)
root.insert(1004)
root.insert(251)
root.insert(1182)
root.insert(314)
root.insert(1232)
root.insert(563)
root.insert(326)
root.insert(1081)
root.insert(445)
root.insert(1382)
root.insert(1399)
root.insert(849)
root.insert(507)
root.insert(1369)
root.insert(1599)
root.insert(371)
root.insert(1651)
root.insert(173)
root.insert(830)
root.insert(1462)
root.insert(202)
root.insert(639)
root.insert(185)
root.insert(1431)
root.insert(1872)
root.insert(1862)
root.insert(802)
root.insert(87)
root.insert(1050)
root.insert(1342)
root.insert(1389)
root.insert(1374)
root.insert(1860)
root.insert(585)
root.insert(1170)
root.insert(1828)
root.insert(1874)
root.insert(1778)
root.insert(82)
root.insert(1650)
root.insert(48)
root.insert(137)
root.insert(1021)




# Visualize the tree
graph = visualize_tree(root.root)
graph.render(filename='rbtree3', format='png', cleanup=True)