import re


class Rotation(object):
    def __init__(self, deg, center=None):
        self.deg = deg
        self.center = center

    def __str__(self):
        params = [self.deg]
        params += list(self.center or [])
        return f"rotate({','.join([str(p) for p in params])})"


class Scale(object):
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __str__(self):
        return f"scale({self.x},{self.y})"


class Skew(object):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"skew{self.axis}({self.val})"


class SkewX(Skew):
    axis = 'X'


class SkewY(Skew):
    axis = 'Y'


class Translation(object):
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __str__(self):
        return f"translate({self.x} {self.y})"


class Node(object):
    def __init__(self, tag, **kwargs):
        self.tag = tag
        self.params = kwargs
        self.children = []
        self.classes = []
        self.transforms = []

    @property
    def content(self):
        return ''

    @property
    def num_children(self):
        return len(self.children)

    def add_title(self, title):
        self.append_child(TitleNode(title))
        return self

    def append_child(self, node):
        self.children.append(node)
        return self

    def insert_child(self, index, node):
        self.children.insert(index, node)
        return self

    def delete_child(self, index):
        del self.children[index]
        return self

    def append_class(self, cls):
        self.classes.append(cls)
        return self

    def insert_class(self, index, cls):
        self.classes.insert(index, cls)
        return self

    def remove_class(self, cls):
        self.classes.remove(cls)
        return self

    def rotate(self, deg, center=None):
        self.transforms.append(Rotation(deg, center))
        return self

    def scale(self, xy):
        self.transforms.append(Scale(xy))
        return self

    def skew_x(self, val):
        self.transforms.append(SkewX(val))
        return self

    def skew_y(self, val):
        self.transforms.append(SkewY(val))
        return self

    def translate(self, xy):
        self.transforms.append(Translation(xy))
        return self

    def to_string(self, indent=0):
        out_str = f"{' '*indent}<{self.tag}"

        params = dict(self.params)
        if len(self.classes) != 0:
            params['class'] = ' '.join([c for c in self.classes])

        if len(self.transforms) != 0:
            params['transform'] = ' '.join([str(t) for t in self.transforms])

        keys = list(params.keys())
        if len(keys) > 0:
            out_str += ' '
            keys.sort()
            out_str += ' '.join(
                [f'{re.sub(r"_", "-", k)}="{params[k]}"' for k in keys]
            ).strip()

        out_str = out_str.encode('utf-8')

        if len(self.children) == 0 and len(self.content) == 0:
            out_str += '/>\n'.encode('utf-8')
        else:
            out_str += '>\n'.encode('utf-8')
            if len(self.content) != 0:
                indented_content = self.content.decode('utf-8').split('\n')
                indented_content = \
                    [' '*(indent+2) + c for c in indented_content]
                out_str += '\n'.join(indented_content).encode('utf-8')
                out_str += '\n'.encode('utf-8')
            else:
                for c in self.children:
                    out_str += c.to_string(indent=(indent+2))
            out_str += f"{' '*indent}</{self.tag}>\n".encode('utf-8')

        return out_str

    def __str__(self):
        return self.to_string().decode('utf-8')


class TitleNode(Node):
    def __init__(self, title):
        super().__init__('title')
        self.title = title

    @property
    def content(self):
        return self.title.encode('utf-8')
