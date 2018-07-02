from bioSynthesis.Strand import Strand
from bioSynthesis.Base import Base
from bioSynthesis.Rna import Rna
class Dna(Strand):

    def __init__(this):

        this.type="Dna"

    def __init__(this,symbol):
        super().__init__([])
        this.type="Dna"
        this.generateAcid(symbol)

    def transcriptioh(this):
        bases=[]
        for elem in this.getNucleoAcids():
            if elem.isThymine():
                bases.append(Base("U"));

            else:
                bases.append(elem);
        return Rna(bases)

    def getComplStrand(this):
        strand=Strand
        for elem in this.nucleoAcids:
            strand.getNucleoAcids().append(elem)
        return strand;
