from .node import Node


class Path(Node):
    def __init__(self, starting_xy, **kwargs):
        super().__init__("path", **kwargs)
        self.commands = []
        self.move_to(starting_xy)

    def to_string(self, indent=0):
        self.params['d'] = ' '.join(self.commands)
        return super().to_string(indent)

    def arc_to(self, rx_ry, x_rotation, large_arc,
               sweep_ccw, end_xy, relative=False):
        params = list(rx_ry)
        params.append(x_rotation)
        params.append('1' if large_arc else '0')
        params.append('1' if sweep_ccw else '0')
        params += list(end_xy)
        self._append_command('A', relative, *params)
        return self

    def c_bezier(self, ctrl1, ctrl2, end, relative=False):
        if ctrl1:
            coord_str = f"{ctrl1[0]} {ctrl1[1]}, "
            cmd = 'C'
        else:
            coord_str = ''
            cmd = 'S'
        coord_str += (f"{ctrl2[0]} {ctrl2[1]}, " +
                      f"{end[0]} {end[1]}")
        self._append_command(cmd, relative, coord_str)
        return self

    def close(self):
        self._append_command('Z')
        return self

    def h_line(self, x, relative=False):
        self._append_command('H', relative, x)
        return self

    def line_to(self, xy, relative=False):
        self._append_command('L', relative, *(list(xy)))
        return self

    def move_to(self, xy, relative=False):
        self._append_command('M', relative, *(list(xy)))
        return self

    def q_bezier(self, ctrl, end, relative=False):
        if ctrl:
            coord_str = f"{ctrl[0]} {ctrl[1]}, "
            cmd = 'Q'
        else:
            coord_str = ''
            cmd = 'T'
        coord_str += f"{end[0]} {end[1]}"
        self._append_command(cmd, relative, coord_str)
        return self

    def v_line(self, y, relative=False):
        self._append_command('V', relative, y)
        return self

    def _append_command(self, cmd, relative=False, *args):
        if relative:
            cmd = cmd.lower()
        self.commands.append(' '.join([cmd] + [str(a) for a in args]))


if (__name__ == '__main__'):
    from svg import RootSvg, Rectangle

    svg = RootSvg((-25, -25, 50, 50), stroke='black', width='50%')
    svg.append_child(
        Rectangle(p1=(-50, -50), p2=(50, 50), fill='#cccccc', stroke='none'))
    svg.append_child(
        Rectangle(center=(0, 0), width=1, height=1, fill='red', stroke='none'))
    path = Path((6.7, -10), stroke_width=0.2, fill='none')
    svg.append_child(path)

    path.line_to((0, 20), relative=True)
    path.h_line(-2, relative=True)
    path.arc_to((12.9, 12.9), 0, False, True, (0, -20), relative=True)
    path.close()

    print(svg)
    svg.write('src/svg/path.html')
