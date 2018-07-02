import sys
from bioSynthesis.Strand import Strand
from bioSynthesis.Dna import Dna
RED_COLOR_CODE = "\u001B[31m"
RESET_CODE = "\u001B[0m"
def affiche(text):
    print(f"{RED_COLOR_CODE} {text} {RESET_CODE}")
def testsDisplay(text,b):
    affiche(text);
    print(f"nucleo acid:\t{b}");
    print(f"type:\t{b.getType()}")

if __name__=="__main__":
    seqSymbol="ACGTCCGGTATTTAATCGT";
    strand=Strand(seqSymbol);
    testsDisplay("test strand generation ",strand);
    d=Dna(seqSymbol);
    testsDisplay("test Dna generation ",d);
    testsDisplay("test Dna compl generation ",d.getComplStrand());
    #sys.stdout.println(d.transcriptioh());
    rna=(d).transcriptioh();
    testsDisplay("test Rna generation",rna);
    aminoAcids=rna.traduction();
    affiche("display pseudo protein ");
    print(aminoAcids);
    """"
     test strand generation  
    nucleo acid:	ACGTCCGGTATTTAATCGT
    type:	Strand
     test Dna generation  
    nucleo acid:	ACGTCCGGTATTTAATCGT
    type:	Dna
     test Dna compl generation  
    nucleo acid:	ACGTCCGGTATTTAATCGT
    type:	Strand
     test Rna generation 
    nucleo acid:	ACGUCCGGUAUUUAAUCGU
    type:	Rna
     display pseudo protein  
    [théonine, sérine, glycine, isoleucine]
    
    Process finished with exit code 0
    """
