#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Tools:

    def __init__(self):
        self.data = []

    def make7bitclean(self, s):
        s = str(s)
        s = s.replace(u'ä', '{')
        s = s.replace(u'ö', '|')
        s = s.replace(u'ü', '}')
        s = s.replace(u'Ä', '[')
        s = s.replace(u'Ö', '\\')
        s = s.replace(u'Ü', ']')
        s = s.replace(u'ß', '~')
        return s
