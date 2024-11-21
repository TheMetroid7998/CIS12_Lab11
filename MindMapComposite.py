import os

from MindMapLeaf import MindMapLeaf

class MindMapComposite:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def append(self, child):
        return self.children.append(child)

    def remove(self, child):
        return self.children.remove(child)

    def display(self, indent=0):
        print(' ' * indent + str(self))
        for i, child in enumerate(self.children):
            child.display(indent + 1)

    def __str__(self):
        return self.get_shape_representation().format(self.name)

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, "{name}")

"""
def main():
    root = MindMapComposite("Root", "circle")
    leaf1 = MindMapLeaf("Child 1", "square")
    leaf2 = MindMapLeaf("Child 2", "cloud")
    root.append(leaf1)
    root.append(leaf2)

    print(str(root))
    root.display()

    print("MindMapComposite tests completed!")

if __name__ == '__main__':
    main()
"""