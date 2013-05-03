Kontoutdrag.py
==============

Skriptet läser in ett textbaserat kontoutdrag från din bank och skriver ut en klassificerad fil för inläsning till OpenOffice Calc eller Excel.

För tillfället har skriptet stöd för kontoutdrag från Länsförsäkringar Bank.


Klassificera transaktioner
--------------------------

Transaktionerna klassificeras genom regler som anges i filen `transaction_classes.py`.


Skriv ny parser
---------------

Du kan skriva en ny parser för din banks kontoutdrag genom att kopiera `parser/lansforsakringar.py` till en ny fil och göra lämpliga ändringar. Du måste också aktivera möjligheten att välja parser i huvudfilen.
