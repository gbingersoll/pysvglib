from svg.util import underscore, css_name


def test_underscore_converts_camelcase_to_underscore():
    assert underscore("CamelCase") == "camel_case"
    assert underscore("CamelCase2") == "camel_case2"
    assert underscore("CamelCaseB") == "camel_case_b"
    assert underscore("_1234CamelCase") == "_1234_camel_case"


def test_css_name_converts_class_name_to_css_style():
    assert css_name("Thing") == "thing"
    assert css_name("MyClass") == "my-class"
