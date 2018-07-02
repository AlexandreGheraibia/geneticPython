class Base:
#Constructeur
    def __init__(this,symbol):
        this.initBaseElement(symbol)

    def initBaseElement(this,symbol):
        this.symbol=symbol;
        if symbol=="A":
            this.name="adénine";
            this.family="purine";
        elif "T":
            this.name="thymine";
            this.family="pyrimidines";
        elif "U":
            this.name="uracile";
            this.family="pyrimidines";
        elif "G":
            this.name="adénine";
            this.family="purine";

        elif "C":
            this.name="cytosine";
            this.family="pyrimidines";

    def compl(this):
        select=Base("C");
        if this.symbol=="A":
            select=Base("T");
        elif "T":
            select=Base("A")
        elif "C":
            select= Base("G")
        return select

    def isAdenine(this):
        return this.symbol=="A"

    def isCytosine(this):
        return this.symbol=="C";

    def isGuamine(this):
        return this.symbol==("G");

    def isThymine(this):
        return this.symbol==("T");

    def isUracile(this):
        return this.symbol==("U");

    def getSymbol(this):
        return this.symbol;

    def __repr__(this):
        return this.symbol;



