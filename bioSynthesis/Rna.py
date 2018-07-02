import sys

from bioSynthesis.Strand import Strand
from bioSynthesis.AminoAcid import AminoAcid
class Rna(Strand):
    aminoMapExist=False
    aminoAcidMap={"UUU":"phénylanine","UCU":"sérine","UAU":"tyrosine",
                  "UUC":"phénylanine","UCC":"sérine","UAC":"tyrosine",
                  "UUA":"leucine","UCA":"sérine","UAA":"stop",
                  "UUG":"leucine","UCG":"sérine","UAG":"stop","CUU":"leucine",
                  "CCU":"proline","CAU":"histidine",
                  "CUC":"leucine","CCC":"proline","CAC":"histidine",
                  "CUA":"leucine","CCA":"proline","CAA":"glutamine",
                  "CUG":"leucine","CCG":"proline","CAG":"glutamine",
                  "AUU":"isoleucine","ACU":"théonine","AAU":"asparagine",
                  "AUC":"isoleucine","ACC":"théonine","AAC":"asparagine",
                  "AUA":"isoleucine","ACA":"théonine","AAA":"asparagine",
                  "AUG":"méthionine","ACG":"théonine","AAG":"asparagine",
                  "GUU":"valine","GCU":"valine","GAU":"acide","GUC":"valine",
                  "GCC":"valine","GAC":"asparagine","GUA":"valine","GCC":"valine",
                  "GAC":"acide","GUG":"valine","GCG":"valine","GAG":"glutamine",
                  "UGU":"cystéine","CGU":"argine","AGU":"sérine",
                  "UGC":"cystéine","CGC":"argine","AGC":"sérine",
                  "UGA":"stop","CGA":"argine","AGA":"argine",
                  "UGG":"tryptophane","CGG":"argine","AGG":"argine",
                  "GGU":"glycine","GGC":"glycine","GGA":"glycine",
                  "GGG":"glycine"
                  }

    #HashMap<String,String> aminoAcidMap=new HashMap<>();
    def initAminoMap(this):
        aminoMapExist=True;

    def codonToAminoAcid(this,codon):
        if this.aminoMapExist==False:
            this.initAminoMap();
        if codon in this.aminoAcidMap :
            return AminoAcid(this.aminoAcidMap[codon]);
        print("Can't translate the codon do an amino acid");
        return None;

    def __init__(this):
        this.type="Rna"

    def __init__(this,nucleoAcids):
        super().__init__(nucleoAcids)
        this.type="Rna"

    def traduction(this):
        tripletNB=len(this.getNucleoAcids())//3;
        proteins=[]
        i=0;
        fin=False;
        while i<tripletNB and not fin :
            codon=""
            codon+=(this.getNucleoAcids()[i*3]).getSymbol();
            codon+=(this.getNucleoAcids()[i*3+1]).getSymbol();
            codon+=(this.getNucleoAcids()[i*3+2]).getSymbol();
            i+=1
            a=this.codonToAminoAcid(codon);
            if a.getName()!=("stop"):
                 proteins.append(a);
            else:
                fin=True;

        return proteins;
