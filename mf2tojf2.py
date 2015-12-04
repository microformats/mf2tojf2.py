#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mf2 to jf2 converter
# licence cc0
#  2015 Kevin Marks

import logging

def mf2tojf2(mf2):
    """I'm going to have to recurse here"""
    jf2={}
    items = mf2.get("items",[])
    if len(items):
        item = items[0]
        type = item.get("type",["-"])[0].split("-")[1:][0]
        if type: 
            jf2["type"] = type
        properties =  item.get("properties",{})
        for prop in properties:
            jf2[prop] = properties[prop][0] # need to recurse
    #print mf2, jf2
    return jf2