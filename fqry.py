#!/usr/bin/env python3

import mysql.connector
import fobjects
import fparse

def create_db(sefile, anfile, clinfile):

    conn = mysql.connector.connect(user="chall84", password="Diapers3", host="localhost", database="chall84")
    curs = conn.cursor()

    drop = ("DROP TABLE IF EXISTS se, an, clin")
    curs.execute(drop, )

    se = fparse.SEparse(sefile)        
    an = fparse.ANparse(anfile)
    clin = fparse.CLINparse(clinfile)

    setable = ("CREATE TABLE se (id int not null primary key, loc varchar(250) not null,  gene varchar(100) not null, gt varchar(3) not null, vartype varchar(250) null, pred varchar(100) null)")
    curs.execute(setable, )
    
    seinsert = ("INSERT INTO se (id, loc, gene, gt, vartype, pred) VALUES(%s, %s, %s, %s, %s, %s)")
    for i in se:
        i.check_loc(i.loc)
        i.format_gt(i.gt)
        i.format_sevartype(i.sevartype)
        curs.execute(seinsert, (i.id, i.loc, i.gene, i.gt, i.sevartype, i.sepred,))

    antable = ("CREATE TABLE an (id int not null primary key, loc varchar(250) not null, gene varchar(100) null, gt varchar(3) not  null, rs varchar(100) null, vartype varchar(250) null, pred varchar(100) null)")
    curs.execute(antable, )

    aninsert = ("INSERT INTO an (id, loc, gene, gt, rs, vartype, pred) VALUES(%s, %s, %s, %s, %s, %s, %s)")
    for i in an:
        i.check_loc(i.loc)
        i.format_gt(i.gt)
        i.format_anvartype(i.anvartype)
        i.format_anpred(i.anpred)
        curs.execute(aninsert, (i.id, i.loc, i.gene, i.gt, i.rs, i.anvartype, i.anpred,))

    clintable = ("CREATE TABLE clin(id int not null primary key, loc varchar(250) not null, vartype varchar(250) null, sig varchar(100) null, dn varchar(250) null)")
    curs.execute(clintable, )

    clininsert = ("INSERT INTO clin (id, loc, vartype, sig, dn) VALUES(%s, %s, %s, %s, %s)")
    for i in clin:
        i.check_loc(i.loc)
        i.format_dn(i.dn)
        i.format_clinvartype(i.clinvartype)
        curs.execute(clininsert, (i.id, i.loc, i.clinvartype, i.sig, i.dn,))

    conn.commit()
    curs.close()
    conn.close()



#create_db("22snpeff.vcf", "22annovar.vcf", "22clinvar.vcf")

