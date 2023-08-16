#!/usr/bin/python3
'''The Module for Student class.'''


class Student:
    '''The Class for jsonification.'''
    def __init__(self, first_name, last_name, age):
        '''A Constructor.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Dictionary with filter is retrieved.'''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''The actual Loads attributes from json.'''
        for key, value in json.items():
            self.__dict__[key] = value