from svg.svg import Circle, Ellipse, Group, Line, \
                    Polygon, PolyLine, Rectangle, \
                    RootSvg, Svg, Text
from svg.style import Style


def test_Circle_makes_circle_tag_with_additional_params():
    circ = Circle((5, 15), 27, style="xyz")
    assert str(circ) == '<circle cx="5" cy="15" r="27" style="xyz"/>\n'


def test_Ellipse_makes_ellipse_tag_with_additional_params():
    ellipse = Ellipse((5, 15), (27, 10), style="xyz")
    assert(str(ellipse) ==
           '<ellipse cx="5" cy="15" rx="27" ry="10" style="xyz"/>\n')


def test_Group_makes_group_tag_with_additional_params():
    group = Group(fill="white", stroke="green")
    assert(str(group) == '<g fill="white" stroke="green"/>\n')


def test_Group_can_take_children_at_creation_time():
    circ = Circle((5, 15), 27)
    ellipse = Ellipse((5, 15), (27, 10))
    group = Group([circ, ellipse], fill="white", stroke="green")
    outlines = str(group).split('\n')
    assert len(outlines) == 5
    assert outlines[0] == '<g fill="white" stroke="green">'
    assert outlines[1] == '  <circle cx="5" cy="15" r="27"/>'
    assert outlines[2] == '  <ellipse cx="5" cy="15" rx="27" ry="10"/>'
    assert outlines[3] == '</g>'
    assert outlines[4] == ''


def test_Group_can_take_single_child_at_creation_time():
    circ = Circle((5, 15), 27)
    group = Group(circ, fill="white", stroke="green")
    outlines = str(group).split('\n')
    assert len(outlines) == 4
    assert outlines[0] == '<g fill="white" stroke="green">'
    assert outlines[1] == '  <circle cx="5" cy="15" r="27"/>'
    assert outlines[2] == '</g>'
    assert outlines[3] == ''


def test_Line_makes_line_tag_with_additional_params():
    line = Line((5, 15), (27, 10), stroke="black")
    assert(str(line) ==
           '<line stroke="black" x1="5" x2="27" y1="15" y2="10"/>\n')


def test_Polygon_makes_polygon_tag_with_additional_params():
    polygon = Polygon([(0, 100), (50, 25), (50, 75)], stroke="black")
    assert(str(polygon) ==
           '<polygon points="0,100 50,25 50,75" stroke="black"/>\n')


def test_PolyLine_makes_polyline_tag_with_additional_params():
    polyline = PolyLine([(0, 100), (50, 25), (50, 75)], stroke="black")
    assert(str(polyline) ==
           '<polyline points="0,100 50,25 50,75" stroke="black"/>\n')


def test_Rectangle_makes_rectangle_tag_with_pts_dims_and_additional_params():
    rect = Rectangle((5, 15), width=5, height=15, style="xyz")
    assert(str(rect) == '<rect height="15" style="xyz" width="5"' +
                        ' x="5" y="15"/>\n')


def test_Rectangle_makes_rectangle_tag_with_two_points_and_additional_params():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    assert(str(rect) == '<rect height="15" style="xyz" width="5"' +
                        ' x="5" y="15"/>\n')


def test_Rectangle_makes_rectangle_tag_with_center_dims_and_addl_params():
    rect = Rectangle(center=(5, 15), width=10, height=7, style="xyz")
    assert(str(rect) == '<rect height="7" style="xyz" width="10"' +
                        ' x="0.0" y="11.5"/>\n')


def test_Rectangle_makes_rectangle_tag_with_corner_radius():
    rect = Rectangle((5, 15), width=5, height=15, radius=3)
    assert(str(rect) == '<rect height="15" rx="3" width="5"' +
                        ' x="5" y="15"/>\n')
    rect = Rectangle((5, 15), width=5, height=15, radius=(7, 3))
    assert(str(rect) == '<rect height="15" rx="7" ry="3" width="5"' +
                        ' x="5" y="15"/>\n')


def test_RootSvg_makes_svg_tag_with_viewbox_and_xmlns():
    svg = RootSvg((0, 10, 30, 50))
    assert(str(svg) ==
           '<svg viewBox="0 10 30 50" xmlns="http://www.w3.org/2000/svg"/>\n')


def test_RootSvg_takes_additional_params():
    svg = RootSvg((0, 10, 30, 50), stroke="green")
    assert(str(svg) == '<svg stroke="green" viewBox="0 10 30 50"' +
                       ' xmlns="http://www.w3.org/2000/svg"/>\n')


def test_Svg_makes_svg_tag_with_additional_params():
    svg = Svg((5, 15, 35, 55), fill="blue")
    assert str(svg) == '<svg fill="blue" viewBox="5 15 35 55"/>\n'


def test_RootSvg_add_style_adds_styles():
    svg = RootSvg((0, 10, 30, 50))
    assert svg.num_children == 0
    svg.add_style(Style('.my-class', stroke='black'))
    svg.add_style(Style('.other-class', fill='pink'))
    lines = str(svg).split('\n')
    assert len(lines) == 11
    assert(lines[0] == '<svg viewBox="0 10 30 50"' +
                       ' xmlns="http://www.w3.org/2000/svg">')
    assert(lines[1] == '  <style>')
    assert(lines[2] == '    .my-class {')
    assert(lines[3] == '      stroke: black;')
    assert(lines[4] == '    }')
    assert(lines[5] == '    .other-class {')
    assert(lines[6] == '      fill: pink;')
    assert(lines[7] == '    }')
    assert(lines[8] == '  </style>')
    assert(lines[9] == '</svg>')
    assert(lines[10] == '')
    assert svg.num_children == 0


def test_RootSvg_to_string_can_omit_styles():
    svg = RootSvg((0, 10, 30, 50))
    svg.add_style(Style('.my-class', stroke='black'))
    svg.add_style(Style('.other-class', fill='pink'))
    lines = svg.to_string().decode('utf-8').split('\n')
    assert len(lines) == 11
    assert(lines[0] == '<svg viewBox="0 10 30 50"' +
                       ' xmlns="http://www.w3.org/2000/svg">')
    assert(lines[1] == '  <style>')
    assert(lines[2] == '    .my-class {')
    assert(lines[3] == '      stroke: black;')
    assert(lines[4] == '    }')

    lines = svg.to_string(omit_styles=True).decode('utf-8').split('\n')
    assert len(lines) == 2
    assert(lines[0] == '<svg viewBox="0 10 30 50"' +
                       ' xmlns="http://www.w3.org/2000/svg"/>')
    assert(lines[1] == '')


def test_Text_makes_text_tag_with_additional_params():
    txt = Text((5, 7), 'this is my text', fill='green')
    txt.append_class('gigantic')
    lines = txt.to_string().decode('utf-8').split('\n')
    assert len(lines) == 4
    assert lines[0] == '<text class="gigantic" fill="green" x="5" y="7">'
    assert lines[1] == '  this is my text'
    assert lines[2] == '</text>'
    assert lines[3] == ''
