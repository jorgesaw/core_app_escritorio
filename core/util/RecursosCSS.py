#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 22/01/2015

@author: jorgesaw
'''

class RecursosCSS(object):
    
    CSS = ''
    
    @staticmethod
    def cargarRecursoCss(file):
        with open(file, 'r') as fh:
            RecursosCSS.CSS = fh.read()
            