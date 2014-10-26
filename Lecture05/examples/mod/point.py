#! /usr/bin/env python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __iadd__(self, p):
        self.x += p.x
        self.y += p.y
        return self

    def __isub__(self, p):
        self.x -= p.x
        self.y -= p.y
        return self

