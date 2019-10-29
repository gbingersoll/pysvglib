from svg.path import Path


def test_Path_init_makes_path_tag_with_starting_point_and_additional_params():
    path = Path((5, 15), style="xyz")
    assert str(path) == '<path d="M 5 15" style="xyz"/>\n'


def test_Path_move_to_adds_a_move_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.move_to((2, 3))
    assert str(path) == '<path d="M 0 1 M 2 3" style="xyz"/>\n'


def test_Path_move_to_adds_a_relative_move_command_to_the_path():
    path = Path((0, 1), style="xyz").move_to((2, 3), relative=True)
    assert str(path) == '<path d="M 0 1 m 2 3" style="xyz"/>\n'


def test_Path_line_to_adds_a_line_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.line_to((2, 3))
    assert str(path) == '<path d="M 0 1 L 2 3" style="xyz"/>\n'


def test_Path_line_to_adds_a_relative_line_command_to_the_path():
    path = Path((0, 1), style="xyz").line_to((2, 3), relative=True)
    assert str(path) == '<path d="M 0 1 l 2 3" style="xyz"/>\n'


def test_Path_h_line_to_adds_a_horizontal_line_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.h_line(5)
    assert str(path) == '<path d="M 0 1 H 5" style="xyz"/>\n'


def test_Path_h_line_to_adds_a_relative_horizontal_line_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.h_line(7, relative=True)
    assert str(path) == '<path d="M 0 1 h 7" style="xyz"/>\n'


def test_Path_v_line_to_adds_a_vertical_line_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.v_line(3.11)
    assert str(path) == '<path d="M 0 1 V 3.11" style="xyz"/>\n'


def test_Path_v_line_to_adds_a_relative_vertical_line_command_to_the_path():
    path = Path((0, 1), style="xyz")
    path.v_line(-1.2, relative=True)
    assert str(path) == '<path d="M 0 1 v -1.2" style="xyz"/>\n'


def test_Path_close_adds_a_close_path_command_to_the_path():
    path = Path((0, 1)).v_line(-1.2, relative=True)
    path.h_line(2.5, relative=True)
    path.close()
    assert str(path) == '<path d="M 0 1 v -1.2 h 2.5 Z"/>\n'

    path = Path((0, 2)).h_line(2.5, relative=True).close()
    assert str(path) == '<path d="M 0 2 h 2.5 Z"/>\n'


def test_Path_c_bezier_adds_a_cubic_bezier_command_to_the_path():
    path = Path((0, 1), style='xyz')
    path.c_bezier((1, 2), (3, 4), (5, 6))
    assert str(path) == '<path d="M 0 1 C 1 2, 3 4, 5 6" style="xyz"/>\n'


def test_Path_c_bezier_adds_a_relative_cubic_bezier_command_to_the_path():
    path = Path((0, 1), style='xyz')
    path.c_bezier((1, 2), (3, 4), (5, 6), relative=True)
    assert str(path) == '<path d="M 0 1 c 1 2, 3 4, 5 6" style="xyz"/>\n'


def test_Path_c_bezier_adds_smooth_bezier_command_if_no_first_point():
    path = Path((0, 1), style='xyz')
    path.c_bezier(None, (3, 4), (5, 6))
    assert str(path) == '<path d="M 0 1 S 3 4, 5 6" style="xyz"/>\n'


def test_Path_c_bezier_adds_relative_smooth_bezier_command_if_no_first_point():
    path = Path((0, 1), style='xyz').c_bezier(
        None, (3, 4), (5, 6), relative=True)
    assert str(path) == '<path d="M 0 1 s 3 4, 5 6" style="xyz"/>\n'


def test_Path_q_bezier_adds_quadratic_bezier_command():
    path = Path((0, 1), style='xyz')
    path.q_bezier((3, 4), (5, 6))
    assert str(path) == '<path d="M 0 1 Q 3 4, 5 6" style="xyz"/>\n'


def test_Path_q_bezier_adds_relative_quadratic_bezier_command():
    path = Path((0, 1), style='xyz')
    path.q_bezier((3, 4), (5, 6), relative=True)
    assert str(path) == '<path d="M 0 1 q 3 4, 5 6" style="xyz"/>\n'


def test_Path_q_bezier_adds_smooth_quadratic_bezier_command_if_no_ctrl_pt():
    path = Path((0, 1), style='xyz')
    path.q_bezier(None, (5, 6))
    assert str(path) == '<path d="M 0 1 T 5 6" style="xyz"/>\n'


def test_Path_q_bezier_adds_relative_smooth_quad_bezier_cmd_if_no_ctrl_pt():
    path = Path((0, 1), style='xyz').q_bezier(None, (5, 6), relative=True)
    assert str(path) == '<path d="M 0 1 t 5 6" style="xyz"/>\n'


def test_Path_arc_to_adds_arc_command_to_the_path():
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, False, False, (15, 16), relative=False)
    assert str(path) == '<path d="M 0 1 A 13 14 -30 0 0 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, False, True, (15, 16), relative=False)
    assert str(path) == '<path d="M 0 1 A 13 14 -30 0 1 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, True, False, (15, 16), relative=False)
    assert str(path) == '<path d="M 0 1 A 13 14 -30 1 0 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, True, True, (15, 16), relative=False)
    assert str(path) == '<path d="M 0 1 A 13 14 -30 1 1 15 16" style="xyz"/>\n'


def test_Path_arc_to_adds_relative_arc_command_to_the_path():
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, False, False, (15, 16), relative=True)
    assert str(path) == '<path d="M 0 1 a 13 14 -30 0 0 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, False, True, (15, 16), relative=True)
    assert str(path) == '<path d="M 0 1 a 13 14 -30 0 1 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz')
    path.arc_to((13, 14), -30, True, False, (15, 16), relative=True)
    assert str(path) == '<path d="M 0 1 a 13 14 -30 1 0 15 16" style="xyz"/>\n'
    path = Path((0, 1), style='xyz').arc_to(
        (13, 14), -30, True, True, (15, 16), relative=True)
    assert str(path) == '<path d="M 0 1 a 13 14 -30 1 1 15 16" style="xyz"/>\n'
