# pysvglib

A Python-based SVG graphics library for programmatically generating SVG diagrams
from basic shapes.

# Example

Import the library

```python
import svg
```

Create a "root" SVG object and define the view box.  Keyword arguments define
other parameters that will be passed to the fundamental `svg` node.

```python
root = svg.RootSvg((-25, -25, 50, 50), width='50%', height='50%')
```

Add style definitions that will affect the entire graphic.  Keyword arguments
become css style parameters.

```python
root.add_style(svg.Style('.glass', fill='#bbf7f4', fill_opacity=0.5))
root.add_style(svg.Style('.outline', stroke='black'))
```

Add child nodes and groups of nodes.  These can be rectangles, circles, complex
paths, etc.

```python
root.append_child(svg.Rectangle(p1=(-10, -15), p2=(30, 85), fill='#cccccc', stroke='none'))

mygroup = svg.Group(id='mygroup')
mygroup.append_child(svg.Rectangle(center=(0, 0), width=5, height=10).append_class('glass'))
mygroup.append_child(svg.Rectangle(center=(3, 2), width=10, height=5).append_class('glass'))
root.append_child(mygroup)

path = svg.Path((6.7, -10), stroke_width=0.2, fill='none')
path.line_to((0, 20), relative=True).h_line(-2, relative=True) \
    .arc_to((12.9, 12.9), 0, False, True, (0, -20), relative=True) \
    .close()
path.append_class('outline')
root.append_child(path)
```

Apply transformations to nodes and groups.

```python
mygroup.rotate(37, center=(4, 7))
mygroup.translate((2, -4))
path.skew_x(10)
```

Output the SVG markup as a string.

```python
print(root)
```

Which results in:
```xml
<svg height="100%" viewBox="-25 -25 50 50" width="100%" xmlns="http://www.w3.org/2000/svg">
  <style>
    .glass {
      fill: #bbf7f4;
      fill-opacity: 0.5;
    }
  </style>
  <g id="mygroup">
    <rect fill="#cccccc" height="100" stroke="none" width="100" x="-50" y="-50"/>
    <rect class="glass" height="10" width="5" x="-2.5" y="-5.0"/>
  </g>
  <path d="M 6.7 -10 l 0 20 h -2 a 12.9 12.9 0 0 1 0 -20 Z" fill="none" stroke-width="0.2"/>
</svg>
```

...or output it to a file:

```python
root.write('my_picture.svg')
```

which results in:

![Simple SVG](https://raw.githubusercontent.com/gbingersoll/pysvglib/master/my_picture.svg)

# Development

Use [`pipenv`](https://docs.pipenv.org/) for local environment management.
After cloning the repository:

```shell
$ cd <project-repo>
$ pipenv install -e .[dev]
$ pipenv shell
```

Run tests by just executing `pytest` at the root of the local virtual
environment.  Likewise enforce code style by running `pycodestyle .` from the
root of the local virtual environment.

To package and release, from within the virtual environment:

```shell
$ python setup.py sdist bdist_wheel
```

See also [this page](https://packaging.python.org/tutorials/packaging-projects/).
