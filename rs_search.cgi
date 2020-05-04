#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector
import fobjects
import fparse

print("Content-Type: application/json\n\n")
form = cgi.FieldStorage()
term = form.getvalue('rs_term')


conn = mysql.connector.connect(user="chall84", password="Diapers3", host="localhost", database="chall84")
curs = conn.cursor()

rowlist = []
qry = ("SELECT se.loc as loc, se.gene as gene, se.gt as gt, clin.dn as dn, an.rs as rs, clin.sig as sig, clin.vartype as clinvartype, an.pred as anpred, an.vartype as anvartype, se.pred as sepred, se.vartype as sevartype FROM an JOIN se on an.loc = se.loc LEFT OUTER JOIN clin on an.loc=clin.loc LEFT OUTER JOIN clin clin1 on se.loc = clin1.loc WHERE an.rs = %s ")
curs.execute(qry, ("" + term + "",))

for (loc, gene, gt, dn, rs, sig, clinvartype, anpred, anvartype, sepred, sevartype) in curs:
    row = fobjects.variant(loc=loc, gene=gene, gt=gt, dn=dn, rs=rs, sig=sig, clinvartype=clinvartype, anpred=anpred, anvartype=anvartype, sepred=sepred, sevartype=sevartype)
    rowlist.append(row)

conn.commit()
curs.close()
conn.close()


results = { 'match_count': 0, 'matches': list() }
for i in rowlist:
    results['matches'].append({'loc': i.loc, 'gene': i.gene, 'gt': i.gt, 'dn': i.dn, 'rs': i.rs, 'sig': i.sig, 'clinvartype': i.clinvartype, 'sepred': i.sepred, 'sevartype': i.sevartype, 'anpred': i.anpred, 'anvartype': i.anvartype})
    results['match_count'] += 1



print(json.dumps(results))
