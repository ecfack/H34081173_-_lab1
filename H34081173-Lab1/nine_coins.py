import random


class Nine_Coins:
    def __init__(self, number):
        if number < 0:
            number *= (-1)

        self.decNum = number % (2**9)
        self.binStr = self.ConvertDecNumtoBinStr()
        self.coinStr = self.ConvertBinStrtoCoinStr()

    def __str__(self):
        return "binary: "+self.binStr+" and decimal: "+str(self.decNum)

    def __repr__(self):
        return "Nine_Coins: "+self.coinStr

    def ConvertDecNumtoBinStr(self):
        binStr=""
        number=self.decNum
        for i in range(0,9):
            if number %2:
                binStr+="1"
            else:
                binStr+="0"
            number//=2
        return binStr[::-1]

    def ConvertBinStrtoCoinStr(self):
        coinStr = ""
        for i in range(0,9):
            if self.binStr[i] == "1":
                coinStr += "T"
            else:
                coinStr += "H"
        return coinStr[::-1]

    def toss(self):
        self.decNum = random.randint(0, (2**9)-1)
        self.binStr = self.ConvertDecNumtoBinStr()
        self.coinStr = self.ConvertBinStrtoCoinStr()
