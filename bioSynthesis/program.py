import sys
from bioSynthesis.Strand import Strand
from bioSynthesis.Dna import Dna
RED_COLOR_CODE = "\u001B[31m"
RESET_CODE = "\u001B[0m"
def affiche(text):
    print(sys.stdout,f"{RED_COLOR_CODE} {text} {RESET_CODE}")
def testsDisplay(text,b):
    affiche(text);
    print(sys.stdout,f"nucleo acid:\t{b}");
    print(sys.stdout,f"type:\t{b.getType()}")

if __name__=="__main__":
    seqSymbol="ACGTCCGGTATTTAATCGT";
    strand=Strand(seqSymbol);
    testsDisplay("test strand generation ",strand);
    d=Dna(seqSymbol);
    testsDisplay("test Dna generation ",d);
    ##testsDisplay("test Dna compl generation ",d.getComplStrand());
    #sys.stdout.println(d.transcriptioh());
    rna=(d).transcriptioh();
    testsDisplay("test Rna generation",rna);
    aminoAcids=rna.traduction();
    affiche("display pseudo protein ");
    print(aminoAcids);
    """"
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>  test strand generation
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> nucleo acid:	'A''C''G''T''C''C''G''G''T''A''T''T''T''A''A''T''C''G''T'
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> type:	Strand
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>  test Dna generation
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> nucleo acid:	ACGTCCGGTATTTAATCGT
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> type:	Dna
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>  test Rna generation
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> nucleo acid:	ACGUCCGGUAUUUAAUCGU
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'> type:	Rna
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>  display pseudo protein
    [théonine, sérine, glycine, isoleucine]
    """
