# -*- coding: utf-8 -*-

import yaml
from collections import OrderedDict
from . import constant

config_data = yaml.load(constant.CONFIG_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
_group_data = yaml.load(constant.GROUP_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
apply_data = yaml.load(constant.APPLY_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)

def resolve_group_data(group_data):
    def resolve_items(_group_data, group_name, items=None):
        if items is None:
            items = OrderedDict()
        for item in _group_data[group_name]:
            # item is a character
            if len(item.split(".")) == 3:
                items[item] = None
            # item is a group name
            elif "." not in item:
                if item not in _group_data:
                    raise ValueError(f"{item} is an undefined group name!")
                resolve_items(_group_data, item, items=items)
            else:
                raise ValueError(f"{group_name}.{item} is not either a character or a group name")
        return items

    group_data_tmp = dict() # type: typing.Dict[str, typing.List[str]]
    for group_name in group_data:
        group_data_tmp[group_name] = OrderedDict()
        group_data_tmp[group_name] = resolve_items(group_data, group_name)

    _all_items = OrderedDict()
    for item_set in group_data_tmp.values():
        for item in item_set:
            _all_items[item] = None
    group_data_tmp["_all"] = _all_items

    group_data_new = {
        group_name: list(group_data_tmp[group_name])
        for group_name in group_data_tmp
    }
    return group_data_new

group_data = resolve_group_data(_group_data)
