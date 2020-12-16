# -*- coding: utf-8 -*-

import yaml
from . import constant

config_data = yaml.load(constant.CONFIG_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
group_data = yaml.load(constant.GROUP_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
apply_data = yaml.load(constant.APPLY_YML_FILE.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
