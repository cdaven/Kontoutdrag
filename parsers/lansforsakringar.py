# -*- coding: utf-8 -*-

from parsers.base import BaseParser
import transactions

class LansforsakringarParser(BaseParser):
    def parseLine(self, line):
        transaction = transactions.Transaction()
        fields = line.split('\t')
        transaction.date = self.parseDate(fields[0])
        transaction.type = fields[2]
        transaction.description = fields[3]
        transaction.amount = self.parseAmount(fields[4])
        return transaction
