#!/usr/bin/env python3
import re

#variant object holds a row of variant info
class variant:
    def __init__(self, id=None, loc=None, gene=None, gt=None, rs=None, sevartype=None, anvartype=None, clinvartype=None, anpred=None, sepred=None, sig=None, dn=None):
        self.id = id
        self.loc = loc
        self.gene = gene
        self.gt = gt
        self.rs = rs
        self.sevartype = sevartype
        self.anvartype = anvartype
        self.clinvartype = clinvartype
        self.anpred = anpred
        self.sepred = sepred
        self.sig = sig
        self.dn = dn


#checks if the chromosome has "chr" or not and adds if it doesn't
    def check_loc(self, loc):
        m = re.search("chr", loc)
        if m:
            self.loc = loc
        else:
            self.loc = "chr" + loc

    def format_gt(self, gt):
        if gt == "0/1":
            self.gt = "HT"
        if gt == "1/1":
            self.gt = "HM"
        if gt == "2/1":
            self.gt = "CHT"

    def format_dn(self, dn):
        new = dn.replace("|", " | ")
        new2 = new.replace("_", " ")
        self.dn = new2

    def format_sevartype(self, sevartype):
        new = sevartype.replace("_", " ")
        self.sevartype = new

    def format_clinvartype(self, clinvartype):
        new = clinvartype.replace("_", " ")
        self.clinvartype = new

    def format_anvartype(self, anvartype):
        new = anvartype.replace("_", " ")
        self.anvartype = new
        

    def format_anpred(self, anpred):
        if anpred == "A":
            self.anpred = "Automatic_disease_causing"
        if anpred == "D":
            self.anpred = "Disease_causing"
        if anpred == "N":
            self.anpred = "Polymorphism"
        if anpred == "P":
            self.anpred = "Automatic_polymorphism"

