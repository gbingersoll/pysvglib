from .node import Node
from .style import Style


class Svg(Node):
    def __init__(self, view_box, **kwargs):
        view_box_str = ' '.join([str(i) for i in list(view_box)])
        super().__init__("svg", viewBox=view_box_str, **kwargs)


class StyleNode(Node):
    def __init__(self, styles):
        super().__init__("style")
        self.styles = styles

    @property
    def content(self):
        content = b''
        for i, s in enumerate(self.styles):
            if i > 0:
                content += '\n'.encode('utf-8')
            content += s.to_string()
        return content


class RootSvg(Svg):
    def __init__(self, view_box, **kwargs):
        view_box_str = ' '.join([str(i) for i in list(view_box)])
        super().__init__(view_box,
                         xmlns="http://www.w3.org/2000/svg",
                         **kwargs)
        self.styles = []

    def add_style(self, style):
        self.styles.append(style)

    def to_string(self, indent=0, omit_styles=False):
        omit_styles = omit_styles or len(self.styles) == 0
        if not omit_styles:
            self.insert_child(0, StyleNode(self.styles))

        string = super().to_string(indent=indent)

        if not omit_styles:
            self.delete_child(0)

        return string

    def write(self, filename):
        f = open(filename, 'wb')
        f.write(self.to_string())
        f.close()


class Circle(Node):
    def __init__(self, center, radius, **kwargs):
        super().__init__("circle",
                         cx=center[0],
                         cy=center[1],
                         r=radius,
                         **kwargs)


class Ellipse(Node):
    def __init__(self, center, dims, **kwargs):
        super().__init__("ellipse",
                         cx=center[0],
                         cy=center[1],
                         rx=dims[0],
                         ry=dims[1],
                         **kwargs)


class Group(Node):
    def __init__(self, children=[], **kwargs):
        super().__init__("g", **kwargs)
        if not isinstance(children, list):
            children = [children]
        for c in children:
            self.append_child(c)


class Line(Node):
    def __init__(self, p1, p2, **kwargs):
        super().__init__("line",
                         x1=p1[0],
                         y1=p1[1],
                         x2=p2[0],
                         y2=p2[1],
                         **kwargs)


class Poly(Node):
    def __init__(self, tag, points, **kwargs):
        points_str = ' '.join([f"{p[0]},{p[1]}" for p in points])
        super().__init__(tag, points=points_str, **kwargs)


class Polygon(Poly):
    def __init__(self, points, **kwargs):
        super().__init__("polygon", points, **kwargs)


class PolyLine(Poly):
    def __init__(self, points, **kwargs):
        super().__init__("polyline", points, **kwargs)


class Rectangle(Node):
    def __init__(self, p1=None, p2=None, center=None,
                 width=None, height=None, radius=None, **kwargs):
        if center and width and height:
            x1 = center[0] - width / 2.0
            y1 = center[1] - height / 2.0
        else:
            x1 = p1[0]
            y1 = p1[1]
            width = width or (p2[0] - p1[0])
            height = height or (p2[1] - p1[1])

        if radius:
            if isinstance(radius, tuple):
                kwargs['rx'] = radius[0]
                kwargs['ry'] = radius[1]
            else:
                kwargs['rx'] = radius

        super().__init__("rect",
                         x=x1,
                         y=y1,
                         width=width,
                         height=height,
                         **kwargs)


class Text(Node):
    def __init__(self, xy, text, **kwargs):
        super().__init__("text", x=xy[0], y=xy[1], **kwargs)
        self.text = text

    @property
    def content(self):
        return self.text.encode('utf-8')


if (__name__ == '__main__'):
    svg = RootSvg((0, 0, 300, 100), stroke="purple")
    svg.add_style(Style('.my-class', stroke='gray', stroke_width=10))
    svg.add_style(Style('.other-class', fill='pink'))
    group = Group(Circle((50, 50), 40), stroke='green')
    svg.append_child(group)
    circ = Circle((150, 50), 4)
    circ.add_title('this is a little circle')
    group.append_child(circ)
    group.translate((5, 7))
    child_svg = Svg((0, 0, 10, 10), x=200, width=100)
    child_svg.append_child(Circle((5, 5), 4))
    svg.append_child(child_svg)

    line = Line((5, 15), (27, 10), stroke="blue")
    svg.append_child(line)
    line.rotate(5, (10, 10))

    line = Line((130, 50), (27, 10))
    svg.append_child(line)
    line.append_class('my-class')

    txt = Text((10, 40), 'this is my text', fill='green')
    svg.add_style(Style('.wacky-text',
                        font_family='Comic Sans MS',
                        stroke='none',
                        fill='pink'))
    svg.add_style(Style('.gigantic', font_size=50))
    txt.append_class('wacky-text')
    txt.append_class('gigantic')
    svg.append_child(txt)

    print(svg)
    svg.write('src/svg/my.html')
