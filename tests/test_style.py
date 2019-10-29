from svg.style import Style


def test_Style_init_makes_empty_style():
    style = Style('.my-class')
    lines = str(style).split('\n')
    assert len(lines) == 2
    assert lines[0] == '.my-class {'
    assert lines[1] == '}'


def test_Style_to_string_returns_bytes():
    style = Style('.my-class')
    lines = style.to_string().decode('utf-8').split('\n')
    assert lines[0] == '.my-class {'
    assert lines[1] == '}'


def test_Style_to_string_indents():
    style = Style('.my-class', stroke='orange')
    lines = style.to_string(indent=2).decode('utf-8').split('\n')
    assert lines[0] == '  .my-class {'
    assert lines[1] == '    stroke: orange;'
    assert lines[2] == '  }'
    lines = style.to_string(indent=4).decode('utf-8').split('\n')
    assert lines[0] == '    .my-class {'
    assert lines[1] == '      stroke: orange;'
    assert lines[2] == '    }'


def test_Style_init_makes_style_with_params():
    style = Style('.my-class', stroke='orange', stroke_width=1.5)
    lines = str(style).split('\n')
    assert len(lines) == 4
    assert lines[0] == '.my-class {'
    assert lines[1] == '  stroke: orange;'
    assert lines[2] == '  stroke-width: 1.5;'
    assert lines[3] == '}'


def test_Style_allows_reading_parameter():
    style = Style('.my-class', stroke='orange', fill='black')
    assert style['stroke'] == 'orange'
    assert style['fill'] == 'black'


def test_Style_allows_writing_parameter():
    style = Style('.my-class', stroke='orange', fill='black')
    assert style['stroke'] == 'orange'
    assert style['fill'] == 'black'
    style['stroke'] = 'blue'
    style['stroke-width'] = 10
    assert style['stroke'] == 'blue'
    assert style['stroke-width'] == 10
