#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: leoatchina
# @Date:   2016-01-02 22:09:36
# @Last Modified by:   leoatchina
# @Last Modified time: 2016-01-02 22:10:36
import re,sys,re,os


test="   - "
print re.sub('\s{3}-','aa',test)