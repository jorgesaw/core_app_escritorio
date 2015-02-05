#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24/01/2015

@author: jorgesaw
'''

from bs4 import BeautifulSoup
import urllib2
import sys
sys.path.append('./')
    
class ScrapBase(object):
    
    BASE_URL = ''
    SEARCH_URL = ''
    
    def __init__(self):
        #uURL de búsqueda
        self.url = '{0}{1}'.format(ScrapBase.BASE_URL, ScrapBase.SEARCH_URL)
        
        self.soup = None
        #uEncontró un resultado?
        self.found = False
        
        print self.url
        
        #self._process()
        
    def _process(self):
        try:
            response = urllib2.urlopen(self.url)
            self.soup = BeautifulSoup(response.read())
        
            print "SCRAP BASE"
        except:
            pass
        