# -*- coding: utf-8 -*-

import datetime
import transactions

class BaseParser:
    def __init__(self):
        self.transactions = transactions.TransactionCollection()
        self.date_format = '%Y-%m-%d'

    def parse(self, lines):
        for line in lines:
            line = line.rstrip()
            self.transactions.append(self.parseLine(line))
        
        return self.transactions

    def parseLine(self, line):
        """
        Tolka en rad ur kontoutdraget och returnera ett transaktionsobjekt.
        Den h�r metoden m�ste implementeras i subklassen!
        """
        return transactions.Transaction()

    def parseAmount(self, text):
        """
        Tolka en str�ng som ett decimaltal
        """
        text = text.replace(' ', '')
        text = text.replace(',', '.')
        return float(text)

    def parseDate(self, text):
        """
        Tolka en str�ng som ett datum
        """
        return datetime.datetime.strptime(text, self.date_format).date()
