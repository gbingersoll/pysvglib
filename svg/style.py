from .node import Node
import re


class Style(object):
    def __init__(self, selector, **kwargs):
        self.selector = selector
        self.params = kwargs

    def to_string(self, indent=0):
        out_str = f"{' '*indent}{self.selector} {{\n"

        keys = list(self.params.keys())
        keys.sort()
        out_str += ''.join([(' '*(indent) + self._param_str(k)) for k in keys])

        out_str += f"{' '*indent}}}"
        out_str = out_str.encode('utf-8')

        return out_str

    def __getitem__(self, key):
        return self.params[key]

    def __setitem__(self, key, item):
        self.params[key] = item

    def __str__(self):
        return self.to_string().decode('utf-8')

    def _param_str(self, key):
        return f"  {re.sub(r'_', '-', key)}: {self.params[key]};\n"


if (__name__ == '__main__'):
    style = Style('.my-class', fill='orange', stroke='black', stroke_width=1.2)

    print(style)
