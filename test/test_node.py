from svg.svg import Circle, Rectangle, Svg
from svg.node import Node


def test_Node_append_child_appends_a_child_to_the_parent_node():
    svg = Svg((5, 15, 35, 55))
    circ = Circle((7, 10), 5)
    svg.append_child(circ)

    outlines = str(svg).split('\n')
    assert len(outlines) == 4
    assert outlines[0] == '<svg viewBox="5 15 35 55">'
    assert outlines[1] == '  <circle cx="7" cy="10" r="5"/>'
    assert outlines[2] == '</svg>'
    assert outlines[3] == ''


def test_Node_append_child_returns_self_for_chaining():
    svg = Svg((5, 15, 35, 55))
    circ = Circle((7, 10), 5)
    assert svg.append_child(circ) == svg


def test_Node_insert_child_inserts_a_child_to_the_parent_node_at_index():
    svg = Svg((5, 15, 35, 55))
    svg.insert_child(0, Circle((7, 10), 5))
    svg.insert_child(0, Circle((17, 20), 15))
    assert svg.insert_child(1, Circle((37, 30), 35)) == svg

    outlines = str(svg).split('\n')
    assert len(outlines) == 6
    assert outlines[0] == '<svg viewBox="5 15 35 55">'
    assert outlines[1] == '  <circle cx="17" cy="20" r="15"/>'
    assert outlines[2] == '  <circle cx="37" cy="30" r="35"/>'
    assert outlines[3] == '  <circle cx="7" cy="10" r="5"/>'
    assert outlines[4] == '</svg>'
    assert outlines[5] == ''


def test_Node_delete_child_removes_child_at_index():
    svg = Svg((5, 15, 35, 55))
    svg.insert_child(0, Circle((7, 10), 5))
    svg.insert_child(0, Circle((17, 20), 15))
    svg.insert_child(1, Circle((37, 30), 35))
    assert svg.delete_child(2) == svg

    outlines = str(svg).split('\n')
    assert len(outlines) == 5
    assert outlines[0] == '<svg viewBox="5 15 35 55">'
    assert outlines[1] == '  <circle cx="17" cy="20" r="15"/>'
    assert outlines[2] == '  <circle cx="37" cy="30" r="35"/>'
    assert outlines[3] == '</svg>'
    assert outlines[4] == ''


def test_Node_translate_adds_translation_transform():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    assert rect.translate((3, -2.5)) == rect
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="translate(3 -2.5)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_rotate_adds_rotation_transform():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    rect.translate((3, -2.5))
    assert rect.rotate(18) == rect
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="translate(3 -2.5) rotate(18)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_rotate_adds_rotation_transform_with_center():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    rect.rotate(18, (5, 7))
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="rotate(18,5,7)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_scale_adds_scale_transform():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    rect.scale((1.4, 2.0)).translate((3, -2.5))
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="scale(1.4,2.0) translate(3 -2.5)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_skew_x_adds_skew_transform():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    assert rect.skew_x(14) == rect
    rect.translate((3, -2.5))
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="skewX(14) translate(3 -2.5)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_skew_y_adds_skew_transform():
    rect = Rectangle((5, 15), p2=(10, 30), style="xyz")
    assert rect.skew_y(18) == rect
    rect.translate((3, -2.5))
    assert(str(rect) == '<rect height="15" style="xyz"' +
                        ' transform="skewY(18) translate(3 -2.5)"'
                        ' width="5" x="5" y="15"/>\n')


def test_Node_converts_subscripts_in_params():
    rect = Rectangle((5, 15), p2=(10, 30), stroke="red", stroke_width=1.2)
    assert(str(rect) == '<rect height="15"' +
                        ' stroke="red" stroke-width="1.2"' +
                        ' width="5" x="5" y="15"/>\n')


def test_Node_stores_and_adds_css_class_names():
    rect = Rectangle((5, 15), p2=(10, 30))
    assert rect.append_class('big') == rect
    assert(str(rect) == '<rect class="big"' +
                        ' height="15" width="5" x="5" y="15"/>\n')
    rect.append_class('bold')
    assert(str(rect) == '<rect class="big bold"' +
                        ' height="15" width="5" x="5" y="15"/>\n')
    assert rect.insert_class(1, 'brassy') == rect
    assert(str(rect) == '<rect class="big brassy bold"' +
                        ' height="15" width="5" x="5" y="15"/>\n')
    assert rect.remove_class('big') == rect
    assert(str(rect) == '<rect class="brassy bold"' +
                        ' height="15" width="5" x="5" y="15"/>\n')


def test_Node_add_title_adds_the_title():
    rect = Rectangle((5, 15), p2=(10, 30))
    assert rect.add_title('this is a rectangle') == rect
    outlines = str(rect).split('\n')
    assert len(outlines) == 6
    assert outlines[0] == '<rect height="15" width="5" x="5" y="15">'
    assert outlines[1] == '  <title>'
    assert outlines[2] == '    this is a rectangle'
    assert outlines[3] == '  </title>'
    assert outlines[4] == '</rect>'
    assert outlines[5] == ''
