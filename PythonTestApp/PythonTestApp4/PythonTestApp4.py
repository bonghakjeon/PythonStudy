class MyClass:
    def __init__(self, *args, **kwangs):
        self.attribute = 123

    def print_me(self):
        print(self.attribute)

    def am_i_bigger_than(self, other_value):
        current = int(self.attribute)
        other = int(other_value)
        return current > other

MyClass().am_i_bigger_than('100')
