# -*- coding: utf-8 -*-

py_entity = """# -*- coding: utf-8 -*-
# created by SQLInterpreter


class {entity_name}(object):
    \"\"\"
    {entity_comment} Entity
    \"\"\"
    def __init__(self, **kwargs):
        \"\"\"
        {doc_string}
        \"\"\"
        {entity_properties}

    def dictify(self):
        d = dict(filter(lambda x: isinstance(x[1], (str, float, int, unicode)), self.__dict__.items()))
        return d
"""