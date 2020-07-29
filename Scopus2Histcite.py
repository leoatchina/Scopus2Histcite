#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Scopus2Histcite.py
# Author            : leoatchina<leoatchina@outlook.com> 
# Date              : 2019.01.01
# Last Modified Date: 2020.07.29
# Last Modified By  : leoatchina <leoatchina@outlook.com>
# coding:utf-8

import os
import sys
import re


def Scopus2HistCite():
    try:
        wrt_lines = []
        if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]):
            print("You are going to convert {}".format(sys.argv[1]))
            Scopus_file = sys.argv[1]
        elif os.path.isfile("./Scopus.ris"):
            print("You are going to convert ./Scopus.ris")
            Scopus_file = './Scopus.ris'
        else:
            raise Exception("No file spcified")
        auth_started = False
        ref_started = False
        LT = [
            'TI',  # title
            'T2',  # jounal
            'AU',  # author
            'VL',  # volumn
            'IS',  # issue
            'SP',  # start page
            'EP',  # end page
            'PY',  # public year
            'DO',  # maybe doi? not important
        ]
        wrt_lines.append('FN Thomson Reuters Web of Knowledge™')
        wrt_lines.append('VR 1.0')
        with open(Scopus_file, 'rb') as Scopus:
            for each in Scopus.readlines():
                line = each.strip()
                line = line.decode().replace('  - ', ' ')
                mark = line[:2]
                if ref_started:
                    if mark == 'ER':
                        wrt_lines.append('ER')
                        wrt_lines.append('')
                        auth_started = False
                        ref_started = False
                    else:
                        wrt_lines.append(line)
                elif re.search("^N1[\s\-]+References:", line):
                    ref_started = True
                    # line = line.replace(line[:14], 'CR')
                    line = re.sub("^N1[\s\-]+References:", 'CR', line)
                    wrt_lines.append(line)
                elif mark in LT:
                    if mark == 'TI':
                        wrt_lines.append('PT J')
                    else:
                        line = line.replace('T2 ', 'SO ').replace('SP ', 'BP ')
                    if not auth_started and mark == 'AU':
                        auth_started = True
                    else:
                        line = line.replace('AU ', '')
                    wrt_lines.append(line)
        with open("./savedres.txt", "w", encoding = "utf-8") as f:
            for line in wrt_lines:
                print(line)
                f.write(line)
                f.write("\n")
    except Exception as e:
        raise e


if __name__ == '__main__':
    Scopus2HistCite()
