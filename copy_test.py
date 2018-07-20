#!/usr/bin/env python
# coding:utf-8
import copy

origin = [[1, 2, 3], 4, 5, {"a": 6}]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)

origin[3].update({"b": 7})

print origin
print cop1, cop2