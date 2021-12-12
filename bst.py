class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Tree(data)

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()

        return elements

    def search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def tree_max(self):
        if self.right is None:
            return self.data
        return self.right.tree_max()

    def tree_min(self):
        if self.left is None:
            return self.data
        return self.left.tree_min()

    def tree_sum(self):
        s = self.data
        if self.left:
            s += self.left.tree_sum()
        if self.right:
            s += self.right.tree_sum()
        return s

    def postorder(self):
        elements = []
        if self.left:
            elements += (self.left.postorder())
        if self.right:
            elements += (self.right.postorder())
        elements.append(self.data)
        return elements

    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            """
            min_val = self.right.tree_min()
            self.root = min_val
            self.right = self.right.delete(min_val)
            """
            max_val = self.left.tree_max()
            self.data = max_val
            self.left.delete(max_val)
        return self




def build_tree(elements):
    root = Tree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    elements = [17,300,4,1,20,9,50,80,2,69,1,4,189]
    root = build_tree(elements)
    print(root.inorder())
    print(root.search(69))
    print(root.tree_max())
    print(root.tree_min())
    print(root.tree_sum())
    print(root.postorder())
    print(root.preorder())
    (root.delete(17))
    print(root.inorder())
