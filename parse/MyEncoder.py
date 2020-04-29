#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/29 11:32
# @Author: xk
# @File  : MyEncoder.py.py
import json
from time import time

import numpy as np


def default(self, obj):
    if isinstance(obj, bytes):
        return str(obj, encoding='utf-8')
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, time):
        return obj.__str__()

    return json.JSONEncoder.default(self, obj)
