#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function


class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, data_dict):
        return {key: self._traverse_val(val) for key, val in data_dict.iteritems()}

    def _traverse_val(self, val):
        if isinstance(val, ToDictMixin):
            return val.to_dict()
        elif isinstance(val, dict):
            return self._traverse_dict(val)
        elif isinstance(val, list):
            return [self._traverse_val(item) for item in val]
        elif hasattr(val, '__dict__'):
            return self._traverse_dict(val.__dict__)
        else:
            return repr(val)


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def main():
    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(11))
    )
    print(tree.to_dict())


if __name__ == '__main__':
    main()
