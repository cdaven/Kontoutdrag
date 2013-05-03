# -*- coding: utf-8 -*-

import transaction_classes
import re

class Transaction:
    def __init__(self):
        self.date = None
        self.type = ""
        self.description = ""
        self.amount = 0
        self.classification = ""
    
    def __str__(self):
        return ';'.join([str(self.date), self.classification, self.type, self.description, str(self.amount)])

    def classify(self):
        for classification in classes:
            if (classification.match(self)):
                self.classification = classification.name
                break


class TransactionCollection:
    def __init__(self):
        self.transactions = []
        self.counter = 0

    def __iter__(self):
        return self
    
    def next(self):
        if self.counter >= len(self.transactions):
            raise StopIteration
        else:
            nextItem = self.transactions[self.counter]
            self.counter += 1
            return nextItem
    
    def append(self, transaction):
        transaction.classify()
        self.transactions.append(transaction)
    
    def sort(self, field='date'):
        if (field == 'date'):
            self.transactions = sorted(self.transactions, key=lambda t: t.date)
        elif (field == 'type'):
            self.transactions = sorted(self.transactions, key=lambda t: t.type)
        elif (field == 'amount'):
            self.transactions = sorted(self.transactions, key=lambda t: t.amount)
        elif (field == 'description'):
            self.transactions = sorted(self.transactions, key=lambda t: t.description)
        elif (field == 'classification'):
            self.transactions = sorted(self.transactions, key=lambda t: t.classification)
    
    def reverse(self):
        self.transactions.reverse()
    
    def printCSV(self):
        for transaction in self.transactions:
            print transaction


class TransactionClass:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def match(self, transaction):
        for rule in self.rules:
            if rule.startswith('type:'):
                if re.search(r'\b' + rule[5:] + r'\b', transaction.type, re.IGNORECASE | re.UNICODE):
                    return True
            else:
                if re.search(r'\b' + rule + r'\b', transaction.description, re.IGNORECASE | re.UNICODE):
                    return True
        
        return False


classes = []
for classification in transaction_classes.classes:
    classes.append(TransactionClass(classification, transaction_classes.classes[classification]))
