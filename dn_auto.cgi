#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

print("Content-Type:application/json\n\n")
form = cgi.FieldStorage()
term = form.getvalue('term')

conn = mysql.connector.connect(user='chall84', password='Diapers3', host='localhost', database='chall84')
cursor = conn.cursor()

qry = "SELECT DISTINCT dn FROM clin WHERE dn LIKE %s"

cursor.execute(qry, ('%' + term + '%',))

results = []
terms = {}
count = 0
for gene in cursor:
    if count < 10:
        terms = {'value':"".join(gene), 'label':"".join(gene)}
        results.append(terms)
        count+=1

conn.close()

print(json.dumps(results))