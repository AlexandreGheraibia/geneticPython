import sys
from bioSynthesis.Base import Base

class Strand:
    def getType(this):
        return this.type

    def setType(this,type):
        this.type=type

    def getNucleoAcids(this):
        return this.nucleoAcids

    def setNucleoAcids(this,nucleoAcids):
        this.nucleoAcids = nucleoAcids

    def __init__(this):
        this.type="Strand"
        this.nucleoAcids=[]

    def __init__(this,nucleoAcids):
        this.type="Strand"
        this.nucleoAcids=nucleoAcids


    def generateAcid(this, seqSymbol):
        for c in seqSymbol:
            if c=='U'or c=='A'or c=='C'or c=='T'or c=='G':
                if (this.getType()=="Rna" and c!='T') or (this.getType()=="Dna" and c!='U')or(this.getType()=="Strand"):
                    this.nucleoAcids.append(Base(c))
                else:
                    print(sys.stderr,"the symbol "+c+" can't contained by a "+this.getType())
            else:
                print(sys.stderr,"the symbol isn't a base element")

    def __repr__(this):
        accuString=""
        for b in this.nucleoAcids:
            accuString+=f"{b}"
        return accuString


