# -*- coding: utf-8 -*-

import os

PASS_KEY = [
    'id',
    'created',
    'modified',
]


def mk_dir(db_name, dir_name):
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/' + db_name):
        os.mkdir('output/' + db_name)
    pth = os.path.join('output', db_name, dir_name)
    if not os.path.exists(pth):
        os.mkdir(pth)
    return pth


def underline_to_camel(underline_format, need_plural=True):
    """
    下划线转驼峰
    :param underline_format: 下划线格式
    :param need_plural: 是否需要转为单数
    :return: camel_format
    """
    camel_format = ''
    shift_sign = True
    for _s_ in underline_format:
        if _s_ == '_':
            shift_sign = True
        else:
            if shift_sign:
                camel_format += _s_.upper()
                shift_sign = False
            else:
                camel_format += _s_
    return plural(camel_format) if need_plural else camel_format


def plural(word):
    # 复数转单数
    if word.endswith('ies'):
        return word[:-3] + 'y'
    elif word.endswith('es'):
        return word[:-2]
    elif word.endswith('s'):
        return word[:-1]
    else:
        return word
