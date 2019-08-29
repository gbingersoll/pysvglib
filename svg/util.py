import re


def underscore(str):
    # Find a capital letter followed by a string of lowercase letters
    # skipping the beginning of the string.  Insert an underscore.
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', str)

    # Find a lowercase letter or number followed by a capital letter,
    # and insert an underscore.  Convert all to lowercase.
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def css_name(str):
    return re.sub(r'_', '-', underscore(str))
