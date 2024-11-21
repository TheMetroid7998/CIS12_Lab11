
class MindMapLeaf:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def display(self, indent=0):
        print(' ' * indent + str(self))

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
    mml = MindMapLeaf('Conrad', 'hexagon')
    mml.display()
    mml.display(indent=4)

if __name__ == '__main__':
    print('basic test')
    main()
"""