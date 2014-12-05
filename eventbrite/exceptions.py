# -*- coding: utf-8 -*-


class IllegalHttpMethod(Exception):
    pass


class InvalidResourcePath(Exception):
    pass


class UnknownEndpoint(Exception):
    pass


class UnsupportedEndpoint(Exception):
    pass
