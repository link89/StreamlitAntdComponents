#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/6 16:50
@Author   : ji hao ran
@File     : tree.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""

from ..utils import *


def tree(
        items: List[Union[str, dict, TreeItem]] = None,
        index: Union[int, List[int]] = None,
        format_func: Union[Formatter, Callable] = None,
        label: str = None,
        description: str = None,
        icon: str = None,
        size: MantineSize = 'md',
        color: Union[MantineColor, str] = None,
        align: Align = 'start',
        width: int = None,
        height: int = None,
        open_index: List[int] = None,
        open_all: bool = False,
        checkbox: bool = False,
        checkbox_strict: bool = False,
        show_line: bool = True,
        return_index: bool = False,
        on_change: Callable = None,
        args: Tuple[Any, ...] = None,
        kwargs: Dict[str, Any] = None,
        key=None
) -> List[Union[str, int]]:
    """antd design tree  https://ant.design/components/tree

    :param items: tree data
    :param index: default selected tree item index
    :param format_func: label formatter function,receive str and return str
    :param label: tree label
    :param description: tree description
    :param icon: bootstrap icon on all tree item. https://icons.getbootstrap.com/
    :param size: tree size
    :param color: tree color,default streamlit primary color,support mantine color, hex and rgb color
    :param align: tree align
    :param width: tree width
    :param height: tree height
    :param open_index: default opened indexes.if none,tree will open default index's parent nodes.
    :param open_all: open all items.priority[open_all>open_index]
    :param checkbox: show checkbox to allow multiple select
    :param checkbox_strict: parent item and children item are not associated
    :param show_line: show line
    :param return_index: if True,return tree item index,default return label
    :param on_change: item change callback
    :param args: callback args
    :param kwargs: callback kwargs
    :param key: component unique identifier
    :return: list of selected item label or index
    """
    # register callback
    register(key, on_change, args, kwargs)
    # parse items
    items, kv = ParseItems(items, format_func).multi()
    # parse index
    if index is None:
        index = []
    # component params
    kw = update_kw(locals(), items=items)
    # component default
    default = get_default(index, return_index, kv)
    # pass component id and params to frontend
    return component(id=get_func_name(), kw=kw, default=default, key=key)
