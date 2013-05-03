#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from parsers.lansforsakringar import LansforsakringarParser
import transactions

argparser = argparse.ArgumentParser()
argparser.add_argument('--parser', default='Länsforsakringar', choices=['Länsförsäkringar'])
argparser.add_argument('file')
args = argparser.parse_args()

try:
    f = open(args.file, 'r')
except IOError:
    print 'Filen kan inte öppnas'
    sys.exit()

lines = f.readlines()
f.close()


parser = LansforsakringarParser()
transactions = parser.parse(lines)
transactions.sort('classification')
transactions.printCSV()
