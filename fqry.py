#!/usr/bin/env python3

import mysql.connector
import fobjects
import fparse

def create_db(sefile, anfile, snpfile):

    conn = mysql.connector.connect(user="chall84", password="Diapers3", host="localhost", database="chall84_f")
    curs = conn.cursor()

    se = SEparse(sefile)
    an = ANparse(anfile)
    snp = snpparse(snpfile)

    setable = ("CREATE TABLE se (id int not null primary key, loc varchar(100) not null, ref varchar(100) null, alt varchar(100) null, gene varchar(100) null, gt varchar(3) null, rs varchar(100) null, vartype varchar(250) null, pred varchar(100) null)")
    curs.execute(setable, )

    for i in se:
        seinsert = ("INSERT INTO se VALUES(i.id, i.loc, i.ref, i.alt, i.gene, i.gt, i.rs, i.vartype, i.sepred)")
        curs.execute(seinsert, )

    antable = ("CREATE TABLE an (id int not null primary key, loc varchar(100) not null, ref varchar(100) null, alt varchar(100) null, gene varchar(100) null, gt varchar(3) null, rs varchar(100) null, vartype varchar(250) null, pred varchar(100) null)")
    curs.execute(antable, )

    for i in an:
        aninsert = ("INSERT INTO an VALUES(i.id, i.loc, i.ref, i.alt, i.gene, i.gt, i.rs, i.vartype, i.anpred)")
        curs.execute(aninsert, )

    snptable = ("CREATE TABLE snp(rs varchar(100) not null primary key, change varchar(100) null)")
    curs.execute(snptable, )

    for i in snp:
        snpinsert = ("INSERT INTO snp VALUES(i.rs, i.change)")
        curs.execute(snpinsert, )

    conn.commit()
    curs.close()
    conn.close()

def queries(usergene, usergt, userrs, uservartype, usersepred, useranpred):
    
    conn = mysql.connector.connect(user="chall84", password="Diapers3", host="localhost", database="chall84_f")
    curs = conn.cursor()

    rowlist = []
    qry = ("SELECT se.loc, se.ref, se.alt, se.gene, se.gt, an.rs, se.vartype, se.sepred, an.anpred FROM se JOIN an on se.id = an.id WHERE se.gene=%s AND se.gt=%s, AND an.rs=%s, AND se.vartype=%s AND se.sepred=%s AND an.anpred=%s")
    curs.execute(qry, usergene, usergt, userrs, uservartype, usersepred, useranpred, )

    for (loc, ref, alt, gene, gt, vartype, rs, anpred, sepred) in curs:
        row = fobjects.variant(loc=loc, gene=gene, ref=ref, alt=alt, gt=gt, vartype=vartype, rs=rs, anpred=anpred, sepred=sepred)
        rowlist.append(row)
    return rowlist

    conn.commit()
    curs.close()
    conn.close()



create_db("22snpeff.vcf", "22annovar.vcf", "snp_result.txt")

